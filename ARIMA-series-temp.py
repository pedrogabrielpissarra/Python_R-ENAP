#carregar bibliotecas 
from statsmodels.tsa.arima.model import ARIMA 
import matplotlib.pyplot as plt 
import numpy as np 

# Gerando dados sintéticos 
np.random.seed(42) 

data = np.cumsum(np.random.randn(100))  # Série temporal acumulada 

# Ajustando o modelo ARIMA 
model = ARIMA(data, order=(2, 1, 2)) 

fit = model.fit() 

# Fazendo previsões 
forecast = fit.forecast(steps=10) 

# Visualizando a série e a previsão 
plt.figure(figsize=(8, 6)) 

plt.plot(data, label="Dados Originais") 

plt.plot(range(len(data), len(data) + len(forecast)), forecast, label="Previsão", color="red") 

plt.legend() 

plt.title("Previsão com ARIMA") 

plt.xlabel("Tempo") 

plt.ylabel("Valor") 

plt.show() 