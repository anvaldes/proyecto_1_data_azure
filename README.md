# 🧬 Data Preprocessing Pipeline on Azure Functions with Docker

This repository contains a lightweight data pipeline for Azure, containerized with Docker and executed via **Azure Functions**.  
The function reads CSV files from **Azure Blob Storage**, applies feature transformations and splits using `scikit-learn`, and saves the resulting datasets back to Blob Storage.

---

## 🚀 Features

- Executed as an Azure Function using a custom **Python Docker image**
- Reads multiple CSV files from **Azure Blob Storage**
- Combines raw data into a single DataFrame
- Applies column-wise preprocessing (imputation, scaling, encoding)
- Performs data splits: train, validation, test
- Saves processed datasets back to **Blob Storage**
- Fully compatible with `scikit-learn` and `category-encoders`

---

## ⚙️ Function Execution Flow

### 1. Trigger

The Azure Function is invoked via HTTP with query parameters:

```bash
GET /api/main_function?year=2025&month=06
```

### 2. Inside the Function

Downloads the following files from Blob Storage:

```bash
source_data/2025_06/credit_risk_1.csv
source_data/2025_06/credit_risk_2.csv
source_data/2025_06/credit_risk_3.csv
```

- Combines them into a single DataFrame
- Applies preprocessing and feature engineering
- Splits the data into:
- X_train, y_train
- X_val, y_val
- X_test, y_test
- Saves each result to:

```bash
datasets/2025_06/X_train.csv
datasets/2025_06/y_train.csv
datasets/2025_06/X_val.csv
datasets/2025_06/y_val.csv
datasets/2025_06/X_test.csv
datasets/2025_06/y_test.csv
```

---
