import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from exception import imdbException
from logger import logging
from Db.imdb_data import  imdbdata
# Ensure required nltk data files are downloaded
nltk.download('stopwords')

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from exception import imdbException
from logger import logging
from Db.imdb_data import imdbdata  # Import the imdbdata class to fetch data from the database

# Ensure required nltk data files are downloaded
nltk.download('stopwords')

class DataIngestionCleaning:
    def __init__(self):
        """Initialize the class without a data path (since we are using DB)."""
        self.stop_words = set(stopwords.words('english'))  # Set of English stop words
        self.stemmer = PorterStemmer()  # Initialize PorterStemmer for stemming

    def load_data(self):
        """Load raw data from the database using the imdbdata class."""
        try:
            # Instantiate the imdbdata class to fetch data from the DB
            db = imdbdata()
            df = db.fetch_movies()  # Fetch the movies data from the database
            logging.info(f"Loaded raw dataset from the database with shape: {df.shape}")
            return df
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise imdbException(e)

    def clean_data(self, df):
        """Clean the data (e.g., remove duplicates, handle missing values)."""
        try:
            # Example: Remove duplicates and handle missing values
            df = df.drop_duplicates()
            df = df.dropna(subset=['review', 'sentiment'])  # Ensure necessary columns are present
            logging.info("Data cleaned.")

            # Apply text cleaning and preprocessing on the 'review' column
            df['review'] = df['review'].apply(self._process_single_text)

            return df
        except Exception as e:
            logging.error(f"Error cleaning data: {e}")
            raise imdbException(e)

    def _process_single_text(self, text):
        """
        Process a single text string by:
        - Lowercasing the text.
        - Removing content inside square brackets.
        - Removing punctuation and specific special characters.
        - Removing words containing digits.
        - Removing newline characters.
        - Removing stop words.
        - Stemming words.
        
        Args:
        text (str): The text string to be cleaned.

        Returns:
        str: The cleaned and preprocessed text.
        """
        if not isinstance(text, str):
            text = str(text)  # Ensure the text is a string

        text = text.lower()  # Convert text to lowercase

        # Remove text inside square brackets
        text = re.sub(r'\[.*?\]', '', text)

        # Remove punctuation marks
        text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)

        # Remove words that contain digits
        text = re.sub(r'\w*\d\w*', '', text)

        # Remove specific special characters
        text = re.sub(r'[‘’“”…]', '', text)

        # Remove newline characters
        text = re.sub(r'\n', '', text)

        # Remove stop words
        words = text.split()
        words = [word for word in words if word not in self.stop_words]
        text = ' '.join(words)

        # Apply stemming
        text = ' '.join([self.stemmer.stem(word) for word in text.split()])

        return text
