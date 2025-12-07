🌊 AI Marine Predictor: Kepulauan Riau

Sistem Prediksi Pasang Surut Air Laut Menggunakan Komparasi Model Machine Learning

📖 Deskripsi Proyek

AI Marine Predictor adalah aplikasi berbasis web yang dikembangkan sebagai bagian dari Skripsi/Tugas Akhir. Proyek ini bertujuan memprediksi ketinggian pasang surut air laut di wilayah perairan Kepulauan Riau.

Selain memberikan prediksi, sistem ini berfungsi sebagai media edukasi interaktif untuk memvisualisasikan mengapa algoritma regresi standar seringkali gagal menangani data alam yang bersifat periodik, dan bagaimana pendekatan Harmonic Regression menjadi solusi terbaik.

🔬 Analisis & Perbandingan Model (Edukasi)

Terdapat 3 model Machine Learning yang diuji dan dibandingkan dalam aplikasi ini:

1. Linear Regression (Garis Lurus)

Performa: ❌ Buruk (Underfitting).

Analisis Teknis: Algoritma ini memaksakan hubungan linear ($y = mx + c$) pada data. Karena pasang surut air laut bersifat fluktuatif (naik-turun), model ini gagal menangkap pola dan hanya menghasilkan garis datar (rata-rata nilai).

2. Polynomial Regression (Garis Lengkung)

Performa: ⚠️ Tidak Stabil (Overfitting Potential).

Analisis Teknis: Menggunakan derajat polinomial tinggi memungkinkan garis melengkung mengikuti data latih. Namun, kelemahan fatalnya adalah pada ekstrapolasi (prediksi masa depan). Garis cenderung menukik tajam ke arah tak hingga positif atau negatif, yang tidak masuk akal secara fisika untuk level air laut.

3. Harmonic Regression (✅ Best Model)

Performa: 🏆 Sangat Akurat (Good Fit).

Analisis Teknis: Model ini memodifikasi fitur waktu menjadi komponen gelombang menggunakan fungsi trigonometri Sinus & Cosinus (Fourier Series).

Kenapa Juara? Karena pasang surut adalah fenomena siklik (berulang), pendekatan harmonik mampu meniru pola gelombang alamiah tersebut dengan presisi tinggi, baik untuk data masa lalu maupun prediksi masa depan.

📂 Struktur Direktori

Berikut adalah struktur folder proyek PESUT_APP:

PESUT_APP/
├── models/                  # Folder penyimpanan Model ML (.pkl)
│   ├── model_linear.pkl     # Model Linear Regression
│   ├── model_poly.pkl       # Model Polynomial Regression
│   ├── model_harmonic.pkl   # Model Harmonic Regression
│   └── start_time_ref.pkl   # Referensi waktu awal training
├── static/                  # Aset Frontend
│   ├── css/                 # Styling tambahan
│   │   └── style.css
│   ├── img/                 # Gambar/Logo
│   └── js/                  # Interaktivitas JavaScript
│       └── script.js
├── templates/               # Template HTML
│   └── index.html
├── venv/                    # Virtual Environment Python
├── app.py                   # File Utama Aplikasi (Streamlit Entry Point)
├── requirements.txt         # Daftar pustaka/library yang digunakan
└── README.md                # Dokumentasi Proyek


⚙️ Panduan Instalasi (Windows 11)

Ikuti langkah-langkah berikut secara berurutan menggunakan PowerShell untuk menyiapkan lingkungan pengembangan dari nol.

Langkah 1: Masuk ke Folder Proyek

Buka terminal PowerShell, lalu arahkan ke direktori proyek Anda:

cd path\to\PESUT_APP


Langkah 2: Membuat Virtual Environment

Buat lingkungan isolasi Python agar library tidak tercampur dengan sistem utama:

python -m venv venv


Langkah 3: Mengaktifkan Environment

Jalankan perintah berikut:

.\venv\Scripts\activate


Indikator Berhasil: Akan muncul tulisan (venv) berwarna hijau di sebelah kiri baris perintah Anda.

⚠️ TROUBLESHOOTING: Jika muncul error "Scripts is disabled"

Jika Anda melihat pesan error merah: "cannot be loaded because running scripts is disabled on this system", lakukan hal berikut:

Tetap di terminal yang sama, jalankan perintah ini untuk mengizinkan script sementara:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process


Ketik Y atau A jika diminta konfirmasi.

Coba jalankan perintah aktivasi (.\venv\Scripts\activate) kembali.

Langkah 4: Install Dependencies

Install seluruh library yang dibutuhkan (Streamlit, Scikit-learn, dll) dari file requirements:

pip install -r requirements.txt


🚀 Cara Menjalankan Aplikasi

Pastikan virtual environment sudah aktif (ada tanda (venv)), lalu jalankan perintah:

streamlit run app.py


Tunggu beberapa saat. Browser default Anda akan otomatis terbuka dan menampilkan aplikasi di alamat:
http://localhost:8501

📊 Panduan Pengujian & Eksplorasi

Saat aplikasi berjalan, ikuti langkah ini untuk melakukan validasi model:

Navigasi Sidebar:

Lihat panel sebelah kiri. Tentukan rentang tanggal prediksi yang ingin dilihat.

Pilih Model (Model Selector):

Ubah pilihan dropdown model antara Linear, Polynomial, dan Harmonic.

Analisis Visual (Grafik Utama):

🔵 Garis Biru (Ground Truth): Data aktual pasang surut.

🔴 Garis Merah (Prediction): Hasil prediksi algoritma.

Uji Coba: Perhatikan bagaimana garis merah pada model Harmonic menempel ketat pada garis biru, sedangkan model lain melenceng.

Evaluasi Metrik:

Lihat skor R² (R-Squared) di bagian bawah grafik.

Nilai mendekati 1.0 (misal: 0.95) menunjukkan akurasi tinggi.

Nilai rendah atau negatif menunjukkan model gagal memprediksi pola.

👨‍💻 Author

Tim Pengembang AI Marine Predictor
Teknik Informatika - Skripsi/Tugas Akhir