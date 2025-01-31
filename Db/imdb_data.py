import pandas as pd
import numpy as np
from config.db_setupt import DatabaseConnection
from exception import imdbException
from logger import logging
import sys

class imdbdata:
    def __init__(self):
        """Initialize the database connection."""
        self.db = DatabaseConnection()
        self.conn = None

    def fetch_movies(self):
        """Fetch all movies data from the database and return as a Pandas DataFrame."""
        try:
            self.conn = self.db.connect()
            query = "SELECT * FROM movies;"  # Fetch all records from the movies table
            df = pd.read_sql(query, self.conn)
            logging.info("Data fetched successfully from movies table.")
            return df
        except Exception as e:
            # Log the error message
            error_message = f"Error fetching data: {e}"
            logging.error(error_message)
            
            # Raise your custom exception and pass sys to provide detailed traceback info
            raise imdbException(error_message, sys)
        finally:
            # Ensure the database connection is closed
            if self.conn:
                self.db.close()
