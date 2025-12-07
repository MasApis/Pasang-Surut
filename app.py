from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
from datetime import datetime, timedelta
import pytz  # Library wajib untuk handle Zona Waktu

app = Flask(__name__)

# --- 1. LOAD MODELS & SETTINGS ---
# Pastikan file .pkl ada di folder 'models/'
try:
    model_linear = joblib.load('models/model_linear.pkl')
    model_poly = joblib.load('models/model_poly.pkl')
    model_harmonic = joblib.load('models/model_harmonic.pkl')
    start_time_ref = joblib.load('models/start_time_ref.pkl')
    print("✅ Model berhasil dimuat!")
except Exception as e:
    print(f"⚠️ Error loading models: {e}")
    # Dummy load biar server gak crash saat debug tanpa model
    start_time_ref = 0 

# Periode pasang surut (Konstanta Harmonik)
tide_periods = [
    12.4206012 * 3600, 12.0000000 * 3600,
    23.9344721 * 3600, 24.0658877 * 3600,
    25.8193387 * 3600, 26.868350 * 3600,
    14.765 * 24 * 3600, 27.32 * 24 * 3600,
    365.2425 * 24 * 3600
]

# --- 2. FUNGSI BANTUAN ---
def get_harmonic_features(t_values):
    """Membuat fitur Sin/Cos untuk model Harmonic"""
    X_harm = pd.DataFrame({'t': t_values})
    for p in tide_periods:
        k = 2 * np.pi / p
        X_harm[f'sin_{p}'] = np.sin(k * t_values)
        X_harm[f'cos_{p}'] = np.cos(k * t_values)
    return X_harm.values

def analyze_safety(height):
    """Menerjemahkan ketinggian air ke bahasa manusia"""
    if height > 1.2:
        return "🌊 PASANG TINGGI: Waspada banjir rob di pesisir rendah."
    elif height < -1.0:
        return "🪸 SURUT EKSTREM: Bahaya karang muncul! Jangan melintas."
    elif height > 0:
        return "✅ AMAN: Kondisi air cukup untuk aktivitas standar."
    else:
        return "⚠️ SURUT: Hati-hati saat menepikan perahu."

# --- 3. ROUTE FLASK ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        date_str = data['date']   # Format: 'YYYY-MM-DD'
        model_type = data['model'] # 'linear', 'poly', atau 'harmonic'
        
        # --- PERBAIKAN TIMEZONE (KUNCI UTAMA) ---
        # Kita set zona waktu target ke WIB
        wib = pytz.timezone('Asia/Jakarta')
        
        # Parse tanggal dari string (awalnya naive/polos)
        naive_date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Tempelkan timezone WIB. 
        # Ini memastikan 00:00 dianggap 00:00 WIB, bukan UTC.
        selected_date = wib.localize(naive_date)
        
        # Generate 24 jam ke depan
        time_points = [selected_date + timedelta(hours=i) for i in range(24)]
        
        # Hitung detik (timestamp) untuk input ke model
        # .timestamp() sudah otomatis handle konversi ke UTC untuk hitungan internal
        t_input = np.array([(t.timestamp() - start_time_ref) for t in time_points])
        
        predictions = []
        
        # Pilih Model
        if model_type == 'linear':
            predictions = model_linear.predict(t_input.reshape(-1, 1)).tolist()
        elif model_type == 'poly':
            predictions = model_poly.predict(t_input.reshape(-1, 1)).tolist()
        elif model_type == 'harmonic':
            predictions = model_harmonic.predict(get_harmonic_features(t_input)).tolist()
        else:
            return jsonify({'error': 'Model type not found'}), 400

        # --- DATA UNTUK FRONTEND ---
        # Label Jam: Kita format string-nya biar rapi (misal "07:00", "08:00")
        labels = [t.strftime('%H:00') for t in time_points]
        
        # Cari Puncak Pasang & Surut Harian
        max_tide = max(predictions)
        min_tide = min(predictions)
        
        # Ambil index-nya untuk cari jam kejadiannya
        idx_max = predictions.index(max_tide)
        idx_min = predictions.index(min_tide)
        
        daily_analysis = {
            'max_val': round(max_tide, 2),
            'max_time': labels[idx_max],
            'max_desc': analyze_safety(max_tide),
            'min_val': round(min_tide, 2),
            'min_time': labels[idx_min],
            'min_desc': analyze_safety(min_tide)
        }

        return jsonify({
            'labels': labels,
            'values': predictions,
            'model': model_type,
            'analysis': daily_analysis
        })
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # matikan debug saat production nanti
    app.run(debug=True)