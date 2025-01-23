from src.ConciseAI.logging import logger
from src.ConciseAI.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.ConciseAI.pipeline.stage_2_data_transformtion_pipeline import DataTransformationTrainingPipeline
from src.ConciseAI.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"stage{STAGE_NAME} Initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"stage{STAGE_NAME} Initiated")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"

try:
    logger.info(f"stage{STAGE_NAME} Initiated")
    modeltraining_pipeline = ModelTrainerTrainingPipeline()
    modeltraining_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e
