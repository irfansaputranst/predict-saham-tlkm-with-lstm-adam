# -*- coding: utf-8 -*-
"""Prediction - Saham PT. Telekomunikasi Indonesia dengan LSTM dan Adam.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ehVIJy-RnxpjFMYDXGIPIJ6ew1q9MtJV

## Pengumpulan Data

## Import Required Libraries
"""

# Import library pandas
import pandas as pd

# Import library numpy
import numpy as np

# Import library matplotlib untuk visualisasi
import matplotlib.pyplot as plt

# Import library untuk pembuatan model
from keras.layers import Dense, Dropout, LSTM, BatchNormalization
from keras.models import Sequential

# Import library untuk pre-processing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error

"""## Load Data"""

# Panggil file (load file bernama SAHAM - PT Telekomunikasi Indonesia Tbk (TLKM)) dan simpan dalam dataframe
data = pd.read_csv('/content/SAHAM - PT Telekomunikasi Indonesia Tbk (TLKM.JK) - Sheet1.csv')

# Tampilkan 5 baris data
data

"""## Informasi Dataset"""

data.info()

# Kolom 'Close' yang akan kita gunakan dalam membangun model
# Slice kolom 'Close'
data_price = data.iloc[:,1:2].values

# Cek Output data_price
data_price

"""## Visualisasi Data"""

fig = plt.figure(figsize=(14,10))
plt.plot(data_price, c="red")
plt.title("Harga Saham TLKM", fontsize=16)
plt.xlabel("Tanggal", fontsize=14)
plt.ylabel("Harga", fontsize=14)
plt.grid()
plt.show()

"""## Pre-Processing"""

# Men-skalakan data antara 1 dan 0 (scaling) pada data_price
scaler = MinMaxScaler(feature_range=(0,1))

price_scaled = scaler.fit_transform(data_price)

# Definisikan Variabel Step dan Train
step_size = 21
train_x = []
train_y = []

# Membuat Fitur dan List Label
for i in range(step_size, 1212):
  train_x.append(price_scaled[i-step_size:i, 0])
  train_y.append(price_scaled[i, 0])

price_scaled

# Mengonversikan List yang Telah Dibuat Sebelumnya Ke Array
train_x = np.array(train_x)
train_y = np.array(train_y)

# Cek Dimensi Data dengan Function .shape
print("Dimensi dari variabel bebas adalah: ", train_x.shape)
print("Dimensi dari variabel terikat adalah: ", train_y.shape)

# 238 hari terakhir akan digunakan sebagai pengujian
# 953 hari pertama akan digunakan sebagai pelatihan

test_x = train_x[953:]
train_x = train_x[:953]
test_y = train_y[953:]
train_y = train_y[:953]

# Reshape data untuk dimasukkan kedalam keras model
train_x = np.reshape(train_x, (953, step_size, 1))
test_x = np.reshape(test_x, (238, step_size, 1))

# Check kembali dimensi data yang telah di reshape dengan function .shape
print(train_x.shape)
print(test_x.shape)

"""## Build Model - LSTM"""

# Buat Variabel Penampung Model LSTM
lstm_model = Sequential()

# Add a LSTM layer with BatchNormalization and Dropout
lstm_model.add(LSTM(64, activation="tanh", return_sequences=True, input_shape=(train_x.shape[1], 1)))
lstm_model.add(Dropout(0.30))
lstm_model.add(BatchNormalization())

lstm_model.add(LSTM(64, activation="tanh", return_sequences=True))
lstm_model.add(Dropout(0.30))

lstm_model.add(LSTM(64, activation="tanh", return_sequences=False))
lstm_model.add(Dropout(0.30))

# Add a Dense layer with 1 unit
lstm_model.add(Dense(1))

# menambahkan loss function kedalam model lstm dengan tipe MSE

lstm_model.compile(
    optimizer="adam",
    loss="MSE"
)

lstm_model.summary()

# fit lstm model, dengan epoch 100 dan batch size 32
lstm_model.fit(train_x,train_y,epochs=100,batch_size=32)

# Prediksi Model LSTM
lstm_predictions = lstm_model.predict(test_x)

# Check Evaluasi
lstm_score_1 = mean_absolute_percentage_error(test_y, lstm_predictions)
lstm_score_2 = mean_squared_error(test_y, lstm_predictions)
lstm_score_3 = mean_absolute_error(test_y, lstm_predictions)

print("Mean Absolute Percentage Error (MAPE): ", lstm_score_1)
print("Mean Squared Error (MSE): ", lstm_score_2)
print("Mean Absolute Error (MAE): ", lstm_score_3)

"""## Visualisasi Hasil Prediksi dengan Data Original"""

lstm_predictions = scaler.inverse_transform(lstm_predictions)
test_y = scaler.inverse_transform(test_y.reshape(-1,1))

plt.figure(figsize=(16,12))

plt.plot(test_y, c="blue",linewidth=  2, label="original")
plt.plot(lstm_predictions, c="green",linewidth=2, label="LSTM")
plt.legend()
plt.title("PERBANDINGAN",fontsize=20)
plt.grid()
plt.show()