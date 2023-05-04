def show_run_url(run_url):
    import IPython

    html = f'Databand Run is <a href="{run_url}" target="_blank" >at this link</a>'
    IPython.display.display(IPython.display.HTML(html))
