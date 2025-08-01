import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/Hiruni-Hasara/hosted-datasets/refs/heads/main/heart.csv")

# Split features and target
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
