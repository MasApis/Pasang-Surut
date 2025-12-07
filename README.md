# 🌊 AI Marine Predictor – Sistem Prediksi Pasang Surut Air Laut

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange?style=for-the-badge&logo=scikitlearn)

AI Marine Predictor adalah aplikasi web untuk memprediksi pasang surut air laut menggunakan Machine Learning. Proyek ini berfungsi sebagai media edukasi visual untuk memahami bagaimana algoritma bekerja pada data alam periodik.

==================================================

✨ FITUR UTAMA
- Prediksi pasang surut berbasis data historis
- Visualisasi grafik aktual vs prediksi
- Komparasi model secara langsung
- Edukasi underfitting & overfitting
- Evaluasi nilai akurasi (R² Score)

==================================================

🤖 MODEL YANG DIGUNAKAN
- Linear Regression (Underfitting)
- Polynomial Regression (Overfitting)
- Harmonic Regression (Paling Stabil)

==================================================

📁 STRUKTUR PROYEK

PESUT_APP/
├── start_time_ref.pkl
├── static/
│   ├── css/style.css
│   ├── img/
│   └── js/script.js
├── templates/index.html
├── venv/
├── app.py
├── requirements.txt
└── README.md

==================================================

⚙ CARA INSTALL WINDOWS 11

cd path\to\PESUT_APP
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

Jika error:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

==================================================

🚀 MENJALANKAN APLIKASI

python app.py

Buka di browser:
http://127.0.0.1:5000

==================================================

🧭 CARA MENGGUNAKAN
Pilih tanggal → pilih model → klik prediksi → bandingkan grafik → cek nilai R²

==================================================

👨‍💻 AUTHOR
Tim Pengembang AI Marine Predictor
Teknik Informatika
