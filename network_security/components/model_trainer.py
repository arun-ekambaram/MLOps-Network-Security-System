import os,sys
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from network_security.entity.config import ModelTrainerConfig
from network_security.utils.ml_utils.model.estimator import NetworkModel
from network_security.utils.main_utils.utils import save_object,load_object
from network_security.utils.main_utils.utils import load_numpy_array_data
from network_security.utils.ml_utils.metric.classification_metric import get_classification_score


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig,data_transformation_artifact: DataTransformationArtifact ):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def train_model(self,X_train,y_train):

        
    def initiate_model_trainer(self)-> ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            ## loading training array and testing array
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            x_train, y_train, x_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1],

            )
            model = self.train_model(x_train,y_train)
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)