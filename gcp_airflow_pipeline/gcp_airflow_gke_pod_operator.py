# DAG file should be hosted on GCP Airflow environment (Composer)
import datetime

from airflow import models
from airflow.contrib.kubernetes import secret
from airflow.contrib.operators import kubernetes_pod_operator

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

with models.DAG(
        dag_id='gcp_airflow_test',
        schedule_interval=datetime.timedelta(days=1),
        start_date=YESTERDAY) as dag:
    
    kubernetes_min_pod = kubernetes_pod_operator.KubernetesPodOperator(
    task_id='test_sklearn_pipeline',
    name='test_sklearn_pipeline',
    namespace='default',
    image='{image_in_gcp_container_registry}')
