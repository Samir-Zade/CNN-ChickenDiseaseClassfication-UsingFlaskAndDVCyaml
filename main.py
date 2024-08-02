from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


# Define the name of the stage we are currently working on. This will help in logging and debugging purposes.
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
