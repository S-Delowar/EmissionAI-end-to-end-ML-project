from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from datetime import datetime, timedelta
import sys
import os

from src.component.data_ingestion import DataIngestion
import mlflow


# Define default_args
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 17),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}



with DAG(
    "emissionAI_ml_pipeline",
    default_args=default_args,
    description="ETL pipeline that extracts from MongoDB and PostgreSQL, transforms, and loads to S3 using @task",
    schedule_interval="@daily",
    catchup=False,
) as dag:
    
    @task
    def ingest_data():
        data_ingestion = DataIngestion()
        data_ingestion.ingest_data_from_pg_db()


        # mlflow.set_tracking_uri("http://mlflow:5000")
        # mlflow.set_experiment("new_exp")
        # with mlflow.start_run():
        #     mlflow.log_metric("result", r)
        print("ingestion task finished")
   
       
    @task
    def validation():
        print("hello2") 
    
    @task
    def preprocessing():
        print("hello2") 
    
    @task
    def model_training_and_evaluating():
        print("hello2")
    
    @task
    def versioning():
        """Data, Model And Preprocessor Versioning"""
        print("hello2")
    
    
    
    # dag dependencies
    ingest_data() >> validation() >> preprocessing() >> model_training_and_evaluating() >> versioning()