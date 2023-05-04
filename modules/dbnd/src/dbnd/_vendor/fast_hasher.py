"""
Fast cryptographic hash of Python objects, with a special case for fast
hashing of numpy arrays.
"""


# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# Copyright (c) 2009 Gael Varoquaux
# License: BSD Style, 3 clauses.

import decimal
import hashlib
import io
import pickle
import struct
import sys
import types

import six


Pickler = pickle._Pickler if six.PY3 else pickle.Pickler


class _ConsistentSet(object):
    """ Class used to ensure the hash of Sets is preserved
        whatever the order of its items.
    """

    def __init__(self, set_sequence):
        # Forces order of elements in set to ensure consistent hash.
        try:
            # Trying first to order the set assuming the type of elements is
            # consistent and orderable.
            # This fails on python 3 when elements are unorderable
            # but we keep it in a try as it's faster.
            self._sequence = sorted(set_sequence)
        except (TypeError, decimal.InvalidOperation):
            # If elements are unorderable, sorting them using their hash.
            # This is slower but works in any case.
            self._sequence = sorted((hash(e) for e in set_sequence))


class _MyHash(object):
    """ Class used to hash objects that won't normally pickle """

    def __init__(self, *args):
        self.args = args


class Hasher(Pickler):
    """ A subclass of pickler, to do cryptographic hashing, rather than
        pickling.
    """

    def __init__(self, hash_name="md5"):
        self.stream = io.BytesIO()
        # By default we want a pickle protocol that only changes with
        # the major python version and not the minor one
        protocol = pickle.DEFAULT_PROTOCOL if six.PY3 else pickle.HIGHEST_PROTOCOL
        Pickler.__init__(self, self.stream, protocol=protocol)
        # Initialise the hash obj
        self._hash = hashlib.new(hash_name)

    def hash(self, obj, return_digest=True):
        try:
            self.dump(obj)
        except pickle.PicklingError as e:
            e.args += ("PicklingError while hashing %r: %r" % (obj, e),)
            raise
        dumps = self.stream.getvalue()
        self._hash.update(dumps)
        if return_digest:
            return self._hash.hexdigest()

    def save(self, obj):
        if isinstance(obj, (types.MethodType, type({}.pop))):
            # the Pickler cannot pickle instance methods; here we decompose
            # them into components that make them uniquely identifiable
            func_name = obj.__func__.__name__ if hasattr(obj, "__func__") else obj.__name__
            inst = obj.__self__
            if type(inst) == type(pickle):
                obj = _MyHash(func_name, inst.__name__)
            elif inst is None:
                # type(None) or type(module) do not pickle
                obj = _MyHash(func_name, inst)
            else:
                cls = obj.__self__.__class__
                obj = _MyHash(func_name, inst, cls)
        Pickler.save(self, obj)

    def memoize(self, obj):
        # We want hashing to be sensitive to value instead of reference.
        # For example we want ['aa', 'aa'] and ['aa', 'aaZ'[:2]]
        # to hash to the same value and that's why we disable memoization
        # for strings
        if isinstance(obj, (six.string_types, six.text_type)):
            return
        Pickler.memoize(self, obj)

    # The dispatch table of the pickler is not accessible in Python
    # 3, as these lines are only bugware for IPython, we skip them.
    def save_global(self, obj, name=None, pack=struct.pack):
        # We have to override this method in order to deal with objects
        # defined interactively in IPython that are not injected in
        # __main__
        kwargs = dict(name=name, pack=pack)
        if sys.version_info >= (3, 4):
            del kwargs["pack"]
        try:
            Pickler.save_global(self, obj, **kwargs)
        except pickle.PicklingError:
            Pickler.save_global(self, obj, **kwargs)
            module = getattr(obj, "__module__", None)
            if module == "__main__":
                my_name = name
                if my_name is None:
                    my_name = obj.__name__
                mod = sys.modules[module]
                if not hasattr(mod, my_name):
                    # IPython doesn't inject the variables define
                    # interactively in __main__
                    setattr(mod, my_name, obj)

    dispatch = Pickler.dispatch.copy()
    # builtin
    dispatch[type(len)] = save_global
    # type
    dispatch[type(object)] = save_global
    # classobj
    dispatch[type(Pickler)] = save_global
    # function
    dispatch[type(pickle.dump)] = save_global

    def _batch_setitems(self, items):
        # forces order of keys in dict to ensure consistent hash.
        try:
            # Trying first to compare dict assuming the type of keys is
            # consistent and orderable.
            # This fails on python 3 when keys are unorderable
            # but we keep it in a try as it's faster.
            Pickler._batch_setitems(self, iter(sorted(items)))
        except TypeError:
            # If keys are unorderable, sorting them using their hash. This is
            # slower but works in any case.
            Pickler._batch_setitems(self, iter(sorted((hash(k), v) for k, v in items)))

    def save_set(self, set_items):
        # forces order of items in Set to ensure consistent hash
        Pickler.save(self, _ConsistentSet(set_items))

    dispatch[type(set())] = save_set


class NumpyHasher(Hasher):
    """ Special case the hasher for when numpy is loaded.
    """

    def __init__(self, hash_name="md5", coerce_mmap=False):
        """
            Parameters
            ----------
            hash_name: string
                The hash algorithm to be used
            coerce_mmap: boolean
                Make no difference between np.memmap and np.ndarray
                objects.
        """
        self.coerce_mmap = coerce_mmap
        Hasher.__init__(self, hash_name=hash_name)
        # delayed import of numpy, to avoid tight coupling
        import numpy as np

        self.np = np
        self._getbuffer = np.getbuffer if hasattr(np, "getbuffer") else memoryview

    def save(self, obj):
        """ Subclass the save method, to hash ndarray subclass, rather
            than pickling them. Off course, this is a total abuse of
            the Pickler class.
        """
        if isinstance(obj, self.np.ndarray) and not obj.dtype.hasobject:
            # Compute a hash of the object
            # The update function of the hash requires a c_contiguous buffer.
            if (
                obj.shape == ()
                or not obj.flags.c_contiguous
                and not obj.flags.f_contiguous
            ):
                # 0d arrays need to be flattened because viewing them as bytes
                # raises a ValueError exception.
                obj_c_contiguous = obj.flatten()
            elif obj.flags.c_contiguous:
                obj_c_contiguous = obj
            else:
                obj_c_contiguous = obj.T
            # memoryview is not supported for some dtypes, e.g. datetime64, see
            # https://github.com/numpy/numpy/issues/4983. The
            # workaround is to view the array as bytes before
            # taking the memoryview.
            self._hash.update(self._getbuffer(obj_c_contiguous.view(self.np.uint8)))

            # We store the class, to be able to distinguish between
            # Objects with the same binary content, but different
            # classes.
            if self.coerce_mmap and isinstance(obj, self.np.memmap):
                # We don't make the difference between memmap and
                # normal ndarrays, to be able to reload previously
                # computed results with memmap.
                klass = self.np.ndarray
            else:
                klass = obj.__class__
            # We also return the dtype and the shape, to distinguish
            # different views on the same data with different dtypes.

            # The object will be pickled by the pickler hashed at the end.
            obj = (klass, ("HASHED", obj.dtype, obj.shape, obj.strides))
        elif isinstance(obj, self.np.dtype):
            # Atomic dtype objects are interned by their default constructor:
            # np.dtype('f8') is np.dtype('f8')
            # This interning is not maintained by a
            # pickle.loads + pickle.dumps cycle, because __reduce__
            # uses copy=True in the dtype constructor. This
            # non-deterministic behavior causes the internal memoizer
            # of the hasher to generate different hash values
            # depending on the history of the dtype object.
            # To prevent the hash from being sensitive to this, we use
            # .descr which is a full (and never interned) description of
            # the array dtype according to the numpy doc.
            klass = obj.__class__
            obj = (klass, ("HASHED", obj.descr))
        Hasher.save(self, obj)


cache = {}


def hash(obj, hash_name="md5", coerce_mmap=False):
    """ Quick calculation of a hash to identify uniquely Python objects
        containing numpy arrays.


        Parameters
        -----------
        hash_name: 'md5' or 'sha1'
            Hashing algorithm used. sha1 is supposedly safer, but md5 is
            faster.
        coerce_mmap: boolean
            Make no difference between np.memmap and np.ndarray
    """
    obj_id = id(obj)

    if obj_id not in cache:
        cache[obj_id] = {}

    if hash_name not in cache[obj_id]:
        if "numpy" in sys.modules:
            hasher = NumpyHasher(hash_name=hash_name, coerce_mmap=coerce_mmap)
        else:
            hasher = Hasher(hash_name=hash_name)
        cache[obj_id][hash_name] = hasher.hash(obj)

    return cache[obj_id][hash_name]
