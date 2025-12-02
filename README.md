# 🌍 Digital Nomad Salary Predictor

Live App: https://co22327-digital-nomad-salary-predictor.onrender.com

Predict salary based on job role, location, productivity, burnout levels, and remote-friendly lifestyle choices.

This project uses a trained machine learning model to estimate a digital nomad’s expected annual salary in USD.
It includes a **clean luxury-themed frontend (HTML + Bootstrap)** and a **Python Flask backend** that serves predictions through a REST API.

The dataset, preprocessing scripts, and trained model (`joblib` file) are included for transparency and reproducibility.

---

## 🚀 Features

### 🔮 Salary Prediction

Predicts salary based on:

* **Job Role**
* **Location (City, Country)**
* **Productivity Score (1–10)**
* **Burnout Level (1–10)**
* **Remote-friendly company**
* **Nomad visa availability**

---

### 🤖 Machine Learning

Uses a trained regression model (`nomad_salary_model.joblib`) built using:

* **Pandas**
* **Scikit-Learn**
* **Feature encoding pipeline**
* **Custom preprocessing**

---

### 🌐 Flask Backend API

The backend exposes a single route:

```
POST /predict
```

The API returns:

* **Predicted salary (USD)**
* **Processed input features**

---

## 📁 Project Structure

```
digital-nomad-salary-predictor/
│
├── templates/
│   ├── index.html                  
│   └── background.avif             
│
├── app.py                          # Flask backend API
├── train_model.py                  # Script to train and export ML model
├── nomad_salary_model.joblib       # Trained regression model
├── digital_nomad_salaries.csv      # Dataset used for training
├── requirements.txt                # Python dependencies
├── .gitignore
└── README.md                       # Project documentation
```

---

## 🧠 How the Model Works

1. Reads and preprocesses dataset (`digital_nomad_salaries.csv`)
2. Encodes categorical features (job role, location, etc.)
3. Trains a regression model (RandomForest or similar)
4. Saves the trained model to `nomad_salary_model.joblib`
5. Flask backend loads the model and returns predictions

---

## ▶️ Running the Project Locally

### **1. Clone the repository**

```bash
git clone https://github.com/divyansh-manro/digital-nomad-salary-predictor.git
cd digital-nomad-salary-predictor
```

### **2. Install dependencies**

```bash
pip install -r requirements.txt
```

### **3. Start the Flask server**

```bash
python app.py
```

### **4. Open in browser**

```
http://127.0.0.1:5000
```

---

## 🖥️ Frontend Preview

The UI includes:

* A hero section inspired by premium branding websites
* A glass-morphism input card
* Smooth animations
* Clean feature list after prediction

**Background used in hero:**
https://share.google/images/zSnCftZceK0XBnhfA

<img src="templates/background.avif" width="650"/>

---

## 📡 API Usage

### **POST /predict**

#### Request Body

```json
{
  "job_role": "Web Developer",
  "location": "Lisbon, Portugal",
  "productivity": 8,
  "burnout_level": 3,
  "company_remote": "Y",
  "nomad_visa": "N"
}
```

#### Response Format

```json
{
  "predicted_salary_usd": 84210,
  "input_features": {
    "job_role": "Web Developer",
    "location": "Lisbon, Portugal",
    "productivity": 8,
    "burnout_level": 3,
    "company_remote": "Y",
    "nomad_visa": "N"
  }
}
```

---

## 🎯 Future Improvements

* Currency conversion (USD → local currencies)
* Integrate NomadList API for cost-of-living score
* Suggest job roles using NLP
* UI dark mode toggle

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you'd like to modify.

---

## 📜 License

This project is open-source under the **MIT License**.

