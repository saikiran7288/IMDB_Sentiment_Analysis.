import os
import logging
from datetime import datetime
from exception import imdbException
import sys

# Create logs directory if it doesn't exist
log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)  # Ensure the logs folder exists

# Generate a log filename with a timestamp
log_filename = os.path.join(log_directory, f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Configure logging to write to a file
logging.basicConfig(
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    handlers=[
        logging.FileHandler(log_filename),  # Write logs to a file
        logging.StreamHandler()  # Also print logs to the console
    ]
)

