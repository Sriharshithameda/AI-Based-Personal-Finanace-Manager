from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# Initialize FastAPI
app = FastAPI(title="AI Financial Manager API")

# Load saved models
model = joblib.load(os.path.join("..", "ml", "model.pkl"))
vectorizer = joblib.load(os.path.join("..", "ml", "vectorizer.pkl"))
label_encoder = joblib.load(os.path.join("..", "ml", "label_encoder.pkl"))

# Request Schema
class TransactionRequest(BaseModel):
    transaction: str

# Root endpoint
@app.get("/")
def home():
    return {"message": "AI Financial Manager API is running 🚀"}

# Prediction endpoint
@app.post("/predict")
def predict_category(data: TransactionRequest):
    # Convert text to vector
    text_vector = vectorizer.transform([data.transaction])

    # Predict category (numeric)
    prediction = model.predict(text_vector)

    # Convert numeric back to original label
    category = label_encoder.inverse_transform(prediction)[0]

    return {
        "transaction": data.transaction,
        "predicted_category": category
    }
