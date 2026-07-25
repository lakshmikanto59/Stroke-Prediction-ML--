# 🧠 Stroke Prediction Using Machine Learning

## 📌 Project Overview

This project predicts whether a patient is at risk of stroke using a Machine Learning model trained on the Kaggle Healthcare Stroke Prediction Dataset.

The application includes:

- FastAPI REST API for prediction
- Streamlit web interface
- Machine Learning model using Scikit-learn/XGBoost
- Docker support for containerization

---

## 📊 Dataset

- **Dataset:** Healthcare Stroke Prediction Dataset
- **Source:** Kaggle
- **Target Variable:** `stroke`

---

## 🚀 Features

- Data preprocessing
- Missing value handling
- Feature encoding
- Feature scaling
- Machine Learning prediction
- REST API using FastAPI
- Interactive UI using Streamlit
- Dockerized application

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- Streamlit
- Joblib
- Docker

---

## 📁 Project Structure

```
Stroke-prediction/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
├── stroke_model.joblib
├── healthcare-dataset-stroke-data.csv
└── screenshots/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Stroke-Prediction.git
```

### Move into the project

```bash
cd Stroke-Prediction
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the FastAPI Application

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run the Streamlit Application

```bash
streamlit run streamlit_app.py
```

---

## 📡 API Endpoint

### POST `/predict`

Accepts patient information and returns the predicted stroke risk.

---

## 🤖 Machine Learning Pipeline

- Data Cleaning
- Missing Value Imputation
- Feature Encoding
- Feature Scaling
- Model Training
- Model Evaluation
- Model Serialization using Joblib
- Prediction using FastAPI

---

## 📈 Model Performance

**Model:** _(Update with your final model name, e.g., XGBoost Classifier or Random Forest)_

Add your evaluation metrics here, for example:

- Accuracy:
- Precision:
- Recall:
- F1-score:
- ROC-AUC:

---

## 📸 Screenshots

Add screenshots after deployment.

Example:

- Home Page
- Prediction Result
- FastAPI Swagger UI

---

## 🔮 Future Improvements

- Deploy FastAPI to Render
- Deploy Streamlit to Streamlit Community Cloud
- Add user authentication
- Monitor model performance
- Improve UI/UX

---

## 👤 Author

**Lakshmikanto Mondal**

Aspiring Data Scientist | Machine Learning Enthusiast

---

## 📄 License

This project is for educational and portfolio purposes.
