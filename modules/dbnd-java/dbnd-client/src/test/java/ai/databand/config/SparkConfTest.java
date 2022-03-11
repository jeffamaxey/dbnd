package ai.databand.config;

import org.apache.spark.sql.SparkSession;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

import static ai.databand.DbndPropertyNames.AIRFLOW_CTX_DAG_ID;
import static ai.databand.DbndPropertyNames.AIRFLOW_CTX_EXECUTION_DATE;
import static ai.databand.DbndPropertyNames.AIRFLOW_CTX_TASK_ID;
import static ai.databand.DbndPropertyNames.AIRFLOW_CTX_TRY_NUMBER;
import static org.hamcrest.MatcherAssert.assertThat;

class SparkConfTest {

    @Test
    public void testParseCmdLine() {
        Map<String, String> parentProps = new HashMap<>(1);
        parentProps.put(AIRFLOW_CTX_DAG_ID, "wrong_process_data");
        parentProps.put("SOME_VAR", "correct_process_data");

        SparkSession sparkSession = SparkSession.builder()
            .master("local[*]")
            .config("spark.env.AIRFLOW_CTX_TRY_NUMBER", "1")
            .config("spark.env.DBND__CORE__DATABAND_ACCESS_TOKEN", "")
            .config("spark.env.AIRFLOW_CTX_TASK_ID", "spark_driver")
            .config("spark.env.AIRFLOW_CTX_DAG_ID", "process_data_spark")
            .config("spark.env.AIRFLOW_CTX_EXECUTION_DATE", "2020-08-03T00:00:00+00:00")
            .config("spark.env.DBND__CORE__DATABAND_URL", "http://webserver:8080")
            .config("spark.env.AIRFLOW_CTX_DAG_ID", "process_data_spark")
            .getOrCreate();

        SparkConf cmd = new SparkConf(new SimpleProps(parentProps));

        Map<String, String> env = cmd.values();
        assertThat("Parsed spark env should not be empty", env.isEmpty(), Matchers.equalTo(false));

        assertThat("Airflow context contains incorrect values. Property should be overridden", env.get(AIRFLOW_CTX_DAG_ID), Matchers.equalTo("process_data_spark"));
        assertThat("Airflow context contains incorrect values", env.get(AIRFLOW_CTX_TASK_ID), Matchers.equalTo("spark_driver"));
        assertThat("Airflow context contains incorrect values", env.get(AIRFLOW_CTX_TRY_NUMBER), Matchers.equalTo("1"));
        assertThat("Airflow context contains incorrect values", env.get(AIRFLOW_CTX_EXECUTION_DATE), Matchers.equalTo("2020-08-03T00:00:00+00:00"));

        // override check
        assertThat("Propety should be inherited from parent property source", env.get("SOME_VAR"), Matchers.equalTo("correct_process_data"));
        sparkSession.stop();
    }

}
