import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


hisse_kodu = 'AMZN'
veri = yf.download(hisse_kodu, start="2022-01-01", end="2022-12-31")


veri['50_SMA'] = veri['Close'].rolling(window=50).mean()


veri['200_SMA'] = veri['Close'].rolling(window=200).mean()


plt.figure(figsize=(12, 6))
plt.plot(veri.index, veri['Close'], label=hisse_kodu + ' Kapanış Fiyatı', alpha=0.6)
plt.plot(veri.index, veri['50_SMA'], label='50 Günlük Hareketli Ortalama', linestyle='--')
plt.plot(veri.index, veri['200_SMA'], label='200 Günlük Hareketli Ortalama', linestyle='--')
plt.title(hisse_kodu + ' Hareketli Ortalama Analizi')
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.grid(True)
plt.show()

