import os
import pandas as pd

# Define dataset directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../cicids2017"))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "cicids2017_merged.csv")

# Attack mapping
attack_mapping = {
    "BENIGN": (0, "Safe", 1),
    "DDoS": (1, "DDoS Attack", 4),
    "PortScan": (2, "Port Scan", 2),
    "Bot": (3, "Botnet Activity", 5),
    "Infiltration": (4, "Infiltration", 5),
    "Web Attack � Brute Force": (5, "Web Attack", 3),
    "Web Attack � XSS": (5, "Web Attack", 3),
    "Web Attack � Sql Injection": (5, "Web Attack", 3),
    "FTP-Patator": (6, "Brute Force", 3),
    "SSH-Patator": (6, "Brute Force", 3),
    "DoS slowloris": (7, "DoS Attack", 4),
    "DoS Slowhttptest": (7, "DoS Attack", 4),
    "DoS Hulk": (7, "DoS Attack", 4),
    "DoS GoldenEye": (7, "DoS Attack", 4),
}

df_list = []
for file in os.listdir(DATASET_DIR):
    file_path = os.path.join(DATASET_DIR, file)
    
    if file.endswith(".csv"):
        print(f"Loading {file} ...")
        df = pd.read_csv(file_path, low_memory=False)

        # Clean column names (remove leading spaces)
        df.columns = df.columns.str.strip()

        if "Label" in df.columns:
            df["Attack_Type"] = df["Label"].map(lambda x: attack_mapping.get(x, (8, "Unknown", 5))[0])
            df["Threat_Level"] = df["Label"].map(lambda x: attack_mapping.get(x, (8, "Unknown", 5))[2])
            df_list.append(df)
        else:
            print(f"⚠ Warning: 'Label' column missing in {file}, skipping.")

if df_list:
    df = pd.concat(df_list, ignore_index=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Data merged successfully! Shape: {df.shape}")
else:
    print("❌ No valid datasets were loaded. Check the dataset files.")
