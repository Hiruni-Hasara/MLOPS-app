import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
url = "https://raw.githubusercontent.com/Hiruni-Hasara/hosted-datasets/refs/heads/main/heart.csv"
df = pd.read_csv(url)

# Features and target
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
