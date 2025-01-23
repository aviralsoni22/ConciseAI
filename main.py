from src.ConciseAI.logging import logger
from src.ConciseAI.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"stage{STAGE_NAME} Initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e