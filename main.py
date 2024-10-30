from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
from network_security.components.model_trainer import ModelTrainer
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config import DataIngestionConfig, DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from network_security.entity.config import TrainingPipelineConfig
import sys


if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate Data Ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)
        data_validation_config =DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiatte the Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info(" Data Validation Completed")
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("Initiatte the Data Transformation")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info(" Data Transformation Completed")
        print(data_transformation_artifact)
        logging.info("Model Training Started")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info(" Model Training Completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
