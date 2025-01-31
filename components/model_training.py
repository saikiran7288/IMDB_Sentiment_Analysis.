import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from exception import imdbException
from logger import logging
from components.data_ingestion import DataIngestionCleaning



class TextClassificationPipeline:
    def __init__(self):
        """Initialize the pipeline with the cleaned dataset path."""
        try:
            self.tfidf_vectorizer = TfidfVectorizer(max_features=5000)
            self.label_encoder = LabelEncoder()
            self.model = LogisticRegression()
            self.data_ingestion_cleaning = DataIngestionCleaning()  # Instantiate the data cleaning class
            logging.info("TextClassificationPipeline initialized.")
        except Exception as e:
            logging.error(f"Error initializing TextClassificationPipeline: {e}")
            raise imdbException(e)

    def load_and_clean_data(self):
        """Load and clean the data using the DataIngestionCleaning class."""
        try:
            # Load and clean the data from the database
            df = self.data_ingestion_cleaning.load_data()
            df = self.data_ingestion_cleaning.clean_data(df)
            logging.info(f"Data loaded and cleaned with shape: {df.shape}")
            return df
        except Exception as e:
            logging.error(f"Error in data loading or cleaning: {e}")
            raise imdbException(e)

    def transform_data(self, df):
        """Apply TF-IDF vectorization to text and label encoding to sentiment."""
        try:
            if 'review' in df.columns:
                df['review'] = df['review'].astype(str)  # Ensure it's a string
                X = self.tfidf_vectorizer.fit_transform(df['review']).toarray()  # Text features
                logging.info("TF-IDF Vectorization applied on reviews.")
            else:
                logging.error("'review' column not found.")
                raise imdbException("Missing 'review' column")

            if 'sentiment' in df.columns:
                y = self.label_encoder.fit_transform(df['sentiment'])
                logging.info("Label encoding applied on sentiment.")
            else:
                logging.error("'sentiment' column not found.")
                raise imdbException("Missing 'sentiment' column")

            return X, y
        except Exception as e:
            logging.error(f"Error in data transformation: {e}")
            raise imdbException(e)

    def train_model(self, X, y):
        """Train the machine learning model."""
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            logging.info("Data split into train and test sets.")
            self.model.fit(X_train, y_train)
            logging.info("Model training completed.")
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)
            logging.info(f"Model Accuracy: {accuracy * 100:.2f}%")
            logging.info(f"Classification Report:\n{report}")
        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise imdbException(e)

    def save_model(self, model_filename="sentiment_model.pkl", vectorizer_filename="tfidf_vectorizer.pkl", encoder_filename="label_encoder.pkl"):
        """Save the trained model, TF-IDF vectorizer, and label encoder."""
        try:
            with open(model_filename, "wb") as f:
                pickle.dump(self.model, f)
            logging.info(f"Model saved successfully to {model_filename}")

            with open(vectorizer_filename, "wb") as f:
                pickle.dump(self.tfidf_vectorizer, f)
            logging.info(f"TF-IDF vectorizer saved successfully to {vectorizer_filename}")

            with open(encoder_filename, "wb") as f:
                pickle.dump(self.label_encoder, f)
            logging.info(f"Label encoder saved successfully to {encoder_filename}")
        except Exception as e:
            logging.error(f"Error saving model or components: {e}")
            raise imdbException(e)

    def run_pipeline(self):
        """Execute the full pipeline: load, transform, train, and save the model."""
        try:
            df = self.load_and_clean_data()
            X, y = self.transform_data(df)
            self.train_model(X, y)
            self.save_model()
            logging.info("Pipeline executed successfully.")
        except Exception as e:
            logging.error(f"Error in the pipeline: {e}")
            raise imdbException(e)

# Run the pipeline if the script is executed directly
if __name__ == "__main__":
    pipeline = TextClassificationPipeline()
    pipeline.run_pipeline()
