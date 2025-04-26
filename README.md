
```markdown
# Network Intrusion Detection System (NIDS) – CICIDS2017 Dataset

🚧 This project is currently under active development.  
🧠 Looking for contributors and professional guidance to improve model performance and deployment.

This repository provides a machine learning pipeline to train a Network Intrusion Detection System (NIDS) using the CICIDS2017 dataset. It uses XGBoost for multiclass classification and includes full data processing, balancing, and model training.

---

## 📌 Features

- Full pipeline for attack detection using machine learning
- CICIDS2017 dataset-based training
- Preprocessing and feature scaling
- Class imbalance handled using SMOTE
- XGBoost models for:
  - Attack Type Classification (8 classes)
  - Threat Level Classification (6 classes)

---

## 🛠️ Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/NIDS-Training.git
   cd NIDS-Training
   ```

2. Install required packages manually:

   ```bash
   pip install pandas numpy scikit-learn imbalanced-learn xgboost joblib
   ```

---

## 🔁 Pipeline Overview

1. Load and label data → load_data.py  
2. Preprocess and scale → preprocess.py  
3. Balance with SMOTE → balance_data.py  
4. Train XGBoost models → train_model.py

---

## 📦 Outputs

- X_scaled.csv, y_labels.csv — preprocessed features and labels
- X_resampled.parquet, y_resampled.parquet — SMOTE-balanced data
- scaler.pkl — saved StandardScaler object
- ids_xgboost_multiclass.pkl — model for attack type
- ids_xgboost_threat.pkl — model for threat level

---

## 🤝 Contributing

This project is a work in progress. Contributions, feedback, or expert advice are highly appreciated!

Steps to contribute:
1. Fork the repo
2. Create a new branch: git checkout -b feature/your-feature
3. Commit changes: git commit -m 'Add feature'
4. Push to branch: git push origin feature/your-feature
5. Open a pull request

---

## 📫 Contact

- Developer: Devendra Mahesh Chaurasiya  
- LinkedIn: https://linkedin.com/in/devendra-chaurasia-20a5542b5  
- Email: devendrachaurasiya2004@gmail.com  

---
