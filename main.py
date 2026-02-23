## from src.ChestDiseaseClassification import logger
## from ChestDiseaseClassification import logger

## logger.info("Welcome to Chest Disease Classification Project")

from ChestDiseaseClassification import logger
from ChestDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e