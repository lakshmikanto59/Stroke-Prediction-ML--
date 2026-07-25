# 🧠 Stroke Prediction Web Application

An end-to-end Machine Learning web application that predicts the likelihood of stroke using patient health information.

## 🚀 Live Demo

- **Frontend (Streamlit):** https://jqwbugwrw8ffnsxeubyqjg.streamlit.app
- **Backend API (Render):** https://stroke-prediction-ml-si29.onrender.com
- **API Documentation (Swagger):** https://stroke-prediction-ml-si29.onrender.com/docs

---

## 📌 Features

- Predicts stroke risk using a trained Machine Learning model
- Interactive Streamlit user interface
- FastAPI REST API backend
- Real-time predictions
- Cloud deployment

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- Streamlit
- Git & GitHub
- Render
- Streamlit Community Cloud

---

## 📂 Project Structure

```text
Stroke-Prediction/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── stroke_model.joblib
├── healthcare-dataset-stroke-data.csv
├── README.md
├── .gitignore
└── Dockerfile
```

## 📊 Dataset

- Healthcare Stroke Dataset
- Source: Kaggle

---

## ⚙️ Installation

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
pip install -r requirements.txt
uvicorn app:app --reload
```

Run Streamlit:

```bash
streamlit run streamlit_app.py
```

---

## 📡 API Endpoint

### POST `/predict`

Returns the predicted stroke risk.

---

## 📸 Screenshots

Add screenshots here after uploading them to a `screenshots/` folder.

---

## 👨‍💻 Author

**Lakshmikanto Mondal**

GitHub: https://github.com/lakshmikanto59
