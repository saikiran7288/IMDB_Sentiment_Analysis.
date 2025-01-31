import logging
from components.model_training import TextClassificationPipeline
from components.data_ingestion import DataIngestionCleaning


# Initialize logging configuration
logging.basicConfig(level=logging.INFO)

def run_demo():
    """Run the demo to execute the text classification pipeline."""
    try:
        # Initialize the text classification pipeline
        pipeline = TextClassificationPipeline()
        logging.info("Starting the text classification pipeline...")

        # Run the full pipeline (data ingestion, transformation, model training, and saving)
        pipeline.run_pipeline()
        logging.info("Pipeline executed successfully!")
        
    except Exception as e:
        logging.error(f"An error occurred while running the pipeline: {e}")
        
if __name__ == "__main__":
    run_demo()
