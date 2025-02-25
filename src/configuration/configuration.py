from pathlib import Path
from src.utils.common import read_yml

CONFIG_FILEPATH = "/opt/airflow/config/config.yml"
SCHEMA_FILEPATH = "/opt/airflow/config/schema.yml"
PARAMS_FILEPATH = "/opt/airflow/config/model_params.yml"


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILEPATH, schema_filepath=SCHEMA_FILEPATH, params_filepath=PARAMS_FILEPATH):
        self.config = read_yml(config_filepath)
        self.schema = read_yml(schema_filepath)
        self.params = read_yml(params_filepath)
                
        # Create root artifact directory
        artifacts_root = self.config.get("artifacts_root", "artifacts")
        Path(artifacts_root).mkdir(parents=True, exist_ok=True)
    
    def get_data_ingestion_config(self):
        ingestion_config = self.config.get("data_ingestion")
        
        return {
            "root_dir": Path(ingestion_config.get("root_dir")), 
            "database_table_name": str(ingestion_config.get("database_table_name")),
            "data_save_path": Path(ingestion_config.get("data_save_path"))
            }