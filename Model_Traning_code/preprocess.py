import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

# Define filenames
filename = "cicids2017_merged.csv"
X_file = "X_scaled.csv"
y_file = "y_labels.csv"
scaler_file = "scaler.pkl"

print(f"Processing {filename}...")

# Load dataset
df = pd.read_csv(filename, low_memory=False)

# Remove leading spaces from column names
df.columns = df.columns.str.strip()

# Drop unnecessary columns
drop_cols = ["Flow ID", "Src IP", "Dst IP", "Timestamp", "Label"]
df.drop(columns=[col for col in drop_cols if col in df.columns], errors="ignore", inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Convert categorical features to numerical values
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = pd.factorize(df[col])[0]

# Separate features (X) and labels (y)
X = df.drop(columns=["Attack_Type", "Threat_Level"])
y = df[["Attack_Type", "Threat_Level"]]

# ✅ Fix: Remove infinities and clip extreme values
X.replace([np.inf, -np.inf], np.nan, inplace=True)
X.fillna(0, inplace=True)
X = X.clip(lower=X.quantile(0.01), upper=X.quantile(0.99), axis=1)

# ✅ Initialize and fit scaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ✅ Save the fitted scaler
joblib.dump(scaler, scaler_file)
print(f"✅ Scaler saved as {scaler_file}")

# Save preprocessed data
pd.DataFrame(X_scaled, columns=X.columns).to_csv(X_file, index=False)
y.to_csv(y_file, index=False)

print("✅ Preprocessed data saved successfully!")
