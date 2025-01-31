import sys
from exception import  imdbException
from logger import  logging
from constants import  HOST,USER ,DATABASE_NAME ,PASSWORD 





import os
import pymysql

class DatabaseConnection:
    def __init__(self):
        self.host = HOST 
        self.user = USER 
        self.database = DATABASE_NAME 
        self.password = PASSWORD 
        
        self.conn = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            logging.info("Connected to the database successfully.")
            return self.conn
        except pymysql.MySQLError as e:
            logging.error(f"Database connection error: {e}")
            raise imdbException(str(e))



    

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            logging.info("Database connection closed.")

