import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE

# Load preprocessed data
X = pd.read_csv("X_scaled.csv", dtype="float32")
y = pd.read_csv("y_labels.csv", dtype="int32")

# Separate Attack_Type and Threat_Level
attack_type = y["Attack_Type"].values.ravel()
threat_level = y["Threat_Level"].values.ravel()

# Check unique attack classes before applying SMOTE
unique_classes = np.unique(attack_type)
if len(unique_classes) < 2:
    print(f"⚠ Warning: Only one attack class found ({unique_classes[0]}). Skipping SMOTE.")
    X_resampled = X
    attack_type_resampled = attack_type
    threat_level_resampled = threat_level
else:
    # Apply SMOTE to balance attack types
    smote = SMOTE(sampling_strategy="auto", random_state=42)
    X_resampled, attack_type_resampled = smote.fit_resample(X, attack_type)

    # Ensure threat level is mapped correctly
    threat_level_dict = {label: np.median(threat_level[attack_type == label]) for label in unique_classes}
    threat_level_resampled = np.array([threat_level_dict[label] for label in attack_type_resampled])

# Save balanced data
X_resampled_df = pd.DataFrame(X_resampled, columns=X.columns)
y_resampled_df = pd.DataFrame({"Attack_Type": attack_type_resampled, "Threat_Level": threat_level_resampled})

X_resampled_df.to_parquet("X_resampled.parquet", index=False)
y_resampled_df.to_parquet("y_resampled.parquet", index=False)

print("✅ Balanced data saved successfully!")
