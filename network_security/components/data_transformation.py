import sys,os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from network_security.constants.training_pipeline import TARGET_COLUMN
from network_security.constants.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS
from network_security.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from network_security.entity.config import DataTransformationConfig
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.utils.main_utils.utils import save_numpy_array_data,save_object


class DataTransformation:
    def __init__(self,data_validation_artifact: DataValidationArtifact,
                 data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact = data_validation_artifact
            self.data_transformation_config:DataTransformationConfig = data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    @staticmethod ## dont need to initialize any objects. directly with the help of class name we can call it
    def read_data(file_path) ->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def get_data_transformer_object(cls)-> Pipeline:
        """
        It initialises a KNNImputer object with the parameters specified in the training_pipeline.py file
        and returns a Pipeline object with the KNNImputer object as the first step

        args:
            cls: DataTransformation

        Returns:
            A Pipeline Object
        """
        logging.info("Entered get_data_transformer_object method of transformation class")
        try:
           imputer:KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
           logging.info(f"Initialise KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
           processor:Pipeline = Pipeline([("imputer",imputer)])
           return processor
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def initiate_data_transformation(self)-> DataTransformationArtifact:
        logging.info("Entered the initiate_data_transformation method of Data Transformation class")
        try:
            logging.info("Starting data transformation")
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_dat(self.data_validation_artifact.valid_test_file_path)

            ## training dataframe
            ## independent features
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN],axis=1)
            ## dependent feature
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1,0)

            ## testing dataframe
             ## independent features
            input_feature_test_df  = test_df.drop(columns=[TARGET_COLUMN],axis=1)
            ## dependent feature
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1,0)
            preprocessor = self.get_data_transformer_object()
            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature = preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature = preprocessor_object.transform(input_feature_test_df)

            train_arr = np.c_[transformed_input_train_feature,np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_feature,np.array(target_feature_test_df)]

            ## save numpy array data
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,array=train_arr, )
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,array= test_arr,)
            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor_object,)

            ## Preparing artifacts
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )

        except Exception as e:
            raise NetworkSecurityException(e,sys)