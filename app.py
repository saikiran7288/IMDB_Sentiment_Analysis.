from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model, vectorizer, and label encoder
model = pickle.load(open('sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # A simple form to take user input

@app.route('/predict', methods=['POST'])
def predict():
    # Get the review from the form input
    review_text = request.form['review']

    # Transform the review text using TF-IDF vectorizer
    review_vectorized = vectorizer.transform([review_text])

    # Predict sentiment
    sentiment = model.predict(review_vectorized)

    # Decode the sentiment (0 = Negative, 1 = Positive)
    sentiment_label = label_encoder.inverse_transform(sentiment)

    return render_template('index.html', prediction_text=f"Sentiment: {sentiment_label[0]}")

if __name__ == "__main__":
    app.run(debug=True)
