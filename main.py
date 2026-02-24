## from src.ChestDiseaseClassification import logger
## from ChestDiseaseClassification import logger

## logger.info("Welcome to Chest Disease Classification Project")

from ChestDiseaseClassification import logger
from ChestDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChestDiseaseClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from ChestDiseaseClassification.pipeline.stage_03_model_trainer import ModelTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"********************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
       logger.exception(e)
       raise e


STAGE_NAME = "Training"
try:
    logger.info(f"*************************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n \nx=============x")

except Exception as e:
    logger.exception(e)
    raise e