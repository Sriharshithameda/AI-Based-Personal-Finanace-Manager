import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("../data/transactions.csv")

X = df["text"]
y = df["category"]

# Encode labels (convert text → numbers)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Convert text to numeric features
vectorizer = TfidfVectorizer(
    ngram_range=(1,2),   # unigrams + bigrams
    stop_words="english",
    max_features=5000
)

X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y_encoded, test_size=0.2, random_state=42
)

# Model
model = XGBClassifier(
    use_label_encoder=False,
    eval_metric='mlogloss'
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Save everything
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("Model and encoder saved successfully!")
