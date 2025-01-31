🎭 IMDB Sentiment Analysis 🎥🎭

📌 Project Overview
        
This project analyzes IMDB movie reviews to classify them as positive or negative using machine learning. The system performs data ingestion, preprocessing, model training, and sentiment prediction, and 
provides a user-friendly interface for interaction.

🚀 Features

     Data Ingestion: Loads IMDB dataset into a structured format.
     
     Data Preprocessing: Cleans and vectorizes text using TF-IDF.
     
     Model Training: Uses Machine Learning (Logistic Regression, SVM, etc.) to classify sentiments.
     
     Database Integration: Stores processed data in MySQL.
     
     Web Interface: Flask-based UI for user interaction.
     
     Logging & Exception Handling: Monitors process execution.


🛠 Installation & Setup

1️⃣ Create a Virtual Environment

     conda create -p venv python==3.8

     conda activate venv/

2️⃣ Install Dependencies

     pip install -r requirements.txt

3️⃣ Set Up Database (MySQL)
  
    Update config/db_setupt.py with database credentials.
    python config/db_setupt.py

4️⃣ Run the Application

    python app.py

📊 Model Training

   To train a new model, execute:
       
    python components/model_training.py

📡 API Endpoints

       Endpoint	Method	Description
         /predict	POST	Predicts sentiment for user input.
         /history	GET	Retrieves past predictions.

🔍 Example Usage
     
       After starting the Flask app, visit:
         
         🔗 http://127.0.0.1:5000
     
     Enter a movie review, and the app will predict its sentiment.

📝 Notes

     Make sure MySQL is running before executing database-related scripts.
     If any package is missing, install it using pip install <package_name>.
     Model predictions are stored in the database for reference.

🎯 Future Enhancements

          🔹 Deep Learning Model (LSTM, BERT) for better accuracy.
          🔹 Deploy on Cloud (AWS, GCP, or Heroku).
          🔹 Interactive Dashboard for sentiment analysis insights.

🏆 Credits
Developed by Kolchelma Sai Kiran 🎯



📂 Folder Structure
bash
Copy
Edit
IMDB_Sentiment_Analysis/
│── app.py                  # Main script to run the application  
│── demo.py                 # Demo script for testing  
│── requirements.txt        # Dependencies list  
│── setup.py                # Setup script  
│── sentiment_model.pkl     # Trained sentiment analysis model  
│── tfidf_vectorizer.pkl    # TF-IDF vectorizer for text transformation  
│── label_encoder.pkl       # Label encoder for sentiment classes  
│  
├── components/             # Core components  
│   │── data_ingestion.py   # Data ingestion and preprocessing  
│   │── model_training.py   # Model training and evaluation  
│   │── __init__.py         # Init file for module  
│   └── __pycache__/        # Cached Python files  
│  
├── config/                 # Database configuration  
│   │── db_setupt.py        # Database setup  
│   │── __init__.py         # Init file  
│   └── __pycache__/        # Cached Python files  
│  
├── constants/              # Project constants  
│   │── __init__.py         # Constants definitions  
│   └── __pycache__/        # Cached Python files  
│  
├── Db/                     # Database operations  
│   │── imdb_data.py        # Handles database interactions  
│   │── __init__.py         # Init file  
│   └── __pycache__/        # Cached Python files  
│  
├── exception/              # Exception handling module  
│   │── __init__.py         # Exception handlers  
│   └── __pycache__/        # Cached Python files  
│  
├── imdb_sentiments_analysis.egg-info/  # Metadata  
│  
├── logger/                 # Logging setup  
│   │── __init__.py         # Logger configuration  
│   └── __pycache__/        # Cached Python files  
│  
├── logs/                   # Log files directory  
│  
├── notebook/               # Jupyter Notebooks for EDA & training  
│   │── EDA.ipynb           # Exploratory Data Analysis  
│   │── model_training.ipynb # Model training and testing  
│  
├── templates/              # Web UI templates  
│   │── index.html          # Frontend HTML for the app  






