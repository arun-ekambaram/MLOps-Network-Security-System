from network_security.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from network_security.entity.config import DataValidationConfig
from network_security.exception.exception import NetworkSecurityException
from network_security.constants.training_pipeline import SCHEMA_FILE_PATH
from network_security.logging.logger import logging
from scipy.stats import ks_2samp #check two samples to find wheather data drift is there or not
import pandas as pd
import os, sys

class DataValidation:
    def __init__(self,data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig)
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)