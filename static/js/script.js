let currentModel = 'harmonic';
let myChart = null;

function selectModel(model) {
    currentModel = model;
    document.querySelectorAll('.model-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(`btn-${model}`).classList.add('active');
}

async function getPrediction() {
    const date = document.getElementById('dateInput').value;
    if(!date) return alert("Pilih tanggal dulu bro!");

    document.getElementById('resultCard').style.display = 'block';
    
    // Loading state (biar user tau lagi mikir)
    document.querySelector('.predict-btn').innerText = "Sedang Menghitung...";
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ date: date, model: currentModel })
        });
        
        const data = await response.json();
        
        // Update Info Edukasi
        updateInfo(data);
        
        // Render Grafik
        renderChart(data.labels, data.values, currentModel);
        
    } catch (e) {
        alert("Gagal koneksi ke server python!");
    }
    
    document.querySelector('.predict-btn').innerText = "ANALISIS SEKARANG";
}

function updateInfo(data) {
    const info = data.analysis;
    
    // Update Badge & Title
    const badge = document.getElementById('accuracyBadge');
    document.getElementById('modelTitle').innerText = "Metode " + data.model.charAt(0).toUpperCase() + data.model.slice(1);

    // Update Kartu Pintar (Pasang/Surut)
    document.getElementById('maxVal').innerText = info.max_val;
    document.getElementById('maxTime').innerText = info.max_time;
    document.getElementById('maxDesc').innerText = info.max_desc;

    document.getElementById('minVal').innerText = info.min_val;
    document.getElementById('minTime').innerText = info.min_time;
    document.getElementById('minDesc').innerText = info.min_desc;

    // Update Catatan Bawah
    const eduNote = document.getElementById('eduNote');
    if(data.model === 'harmonic') {
        badge.className = "badge badge-success";
        badge.innerText = "AKURAT";
        eduNote.innerText = "Metode ini menghitung gravitasi Bulan & Matahari. Sangat disarankan untuk navigasi laut karena polanya mengikuti alam.";
    } else {
        badge.className = "badge badge-danger";
        badge.innerText = "TIDAK AKURAT";
        eduNote.innerText = "Metode ini hanya menarik garis rata-rata. Data pasang surut asli hilang. SANGAT BERBAHAYA jika dipakai nelayan!";
    }
}

function renderChart(labels, values, model) {
    const ctx = document.getElementById('tideChart').getContext('2d');
    
    if (myChart) myChart.destroy();

    // Warna Grafik (Sesuai Palet Sultan)
    let color = '#E83C91'; // Magenta Utama
    if (model !== 'harmonic') color = '#43334C'; // Gelap buat yang salah

    myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Tinggi Air (Meter)',
                data: values,
                borderColor: color,
                backgroundColor: color + '20', // Transparan dikit
                borderWidth: 3,
                pointRadius: 0, // Titik dihilangkan biar bersih di HP
                pointHitRadius: 10, // Tapi kalau disentuh tetep kena
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // WAJIB BUAT RESPONSIVE HP
            plugins: {
                legend: { display: false },
                tooltip: {
                    mode: 'index',
                    intersect: false,
                }
            },
            scales: {
                y: { 
                    grid: { color: '#f0f0f0' },
                    ticks: { color: '#43334C' }
                },
                x: { 
                    grid: { display: false },
                    ticks: { 
                        color: '#43334C',
                        maxTicksLimit: 6 // Biar jamnya gak dempet di HP
                    } 
                }
            }
        }
    });
}