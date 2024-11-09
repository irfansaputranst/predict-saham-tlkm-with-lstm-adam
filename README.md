# Prediksi Saham PT Telekomunikasi Indonesia dengan LSTM dan Adam Optimizer

Proyek ini bertujuan untuk memprediksi harga saham PT Telekomunikasi Indonesia menggunakan model jaringan saraf Long Short-Term Memory (LSTM) dan optimizer Adam. Dengan memanfaatkan data historis, model ini mencoba mengidentifikasi pola tren saham untuk menghasilkan prediksi yang akurat.

## 📂 Deskripsi Proyek

Saham perusahaan memiliki pola fluktuasi yang kompleks. Dengan menggunakan teknik deep learning, khususnya model LSTM, proyek ini mencoba menangkap pola temporal dalam data saham PT Telekomunikasi Indonesia. Optimizer Adam dipilih untuk melatih model karena kemampuannya dalam mengoptimalkan proses pembelajaran.

## 🔍 Tujuan

1. Menganalisis data harga saham PT Telekomunikasi Indonesia.
2. Mengembangkan model LSTM untuk memprediksi harga saham di masa depan.
3. Mengukur kinerja model menggunakan metrik error seperti:
   - Mean Absolute Percentage Error (MAPE)
   - Mean Squared Error (MSE)
   - Mean Absolute Error (MAE)

## 📊 Hasil Evaluasi Model

| Metrik | Nilai |
|--------|-------|
| MAPE   | 0.0924 (9.24%) |
| MSE    | 0.00298 |
| MAE    | 0.0484 |

### Interpretasi
- **MAPE** di bawah 10% menunjukkan prediksi model cukup akurat.
- **MSE** yang rendah menunjukkan kesalahan kuadrat rata-rata yang kecil, mengurangi dampak kesalahan besar.
- **MAE** rendah mengindikasikan kesalahan absolut yang kecil, dengan rata-rata deviasi sekitar 4.84%.
