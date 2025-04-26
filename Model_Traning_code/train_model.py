import os
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

BASE_DIR = "C:/Users/Lenovo/Desktop/Dev_Traning/code"
X_FILE = os.path.join(BASE_DIR, "X_resampled.parquet")
Y_FILE = os.path.join(BASE_DIR, "y_resampled.parquet")

# Load balanced data
X = pd.read_parquet(X_FILE).values
y = pd.read_parquet(Y_FILE)

# Split into features and labels
y_attack = y["Attack_Type"].values
y_threat = (y["Threat_Level"] - 1).astype(int).values



# Split data for intrusion detection model (Attack Type)
X_train, X_test, y_train, y_test = train_test_split(X, y_attack, test_size=0.2, random_state=42)

# Train Attack Type Model
attack_model = XGBClassifier(n_estimators=200, learning_rate=0.1, max_depth=6, objective="multi:softmax", num_class=8, random_state=42)
attack_model.fit(X_train, y_train)

# Evaluate Attack Type Model
y_pred = attack_model.predict(X_test)
print(f"🔍 Attack Type Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(classification_report(y_test, y_pred))

# Save Attack Type Model
ATTACK_MODEL_PATH = os.path.join(BASE_DIR, "ids_xgboost_multiclass.pkl")
joblib.dump(attack_model, ATTACK_MODEL_PATH)
print(f"✅ Attack Type Model saved as {ATTACK_MODEL_PATH}")

# --- Train Threat Level Model ---
X_train, X_test, y_train, y_test = train_test_split(X, y_threat, test_size=0.2, random_state=42)

# Train Threat Level Model
threat_model = XGBClassifier(n_estimators=200, learning_rate=0.1, max_depth=6, objective="multi:softmax", num_class=6, random_state=42)
threat_model.fit(X_train, y_train)

# Evaluate Threat Level Model
y_pred = threat_model.predict(X_test)
print(f"🔍 Threat Level Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(classification_report(y_test, y_pred))

# Save Threat Level Model
THREAT_MODEL_PATH = os.path.join(BASE_DIR, "ids_xgboost_threat.pkl")
joblib.dump(threat_model, THREAT_MODEL_PATH)
print(f"✅ Threat Level Model saved as {THREAT_MODEL_PATH}")
