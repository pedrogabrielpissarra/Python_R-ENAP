# carregando pacotes
from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import numpy as np
# Criando uma série temporal fictícia
np.random.seed(42)
data = {'Data': pd.date_range(start='2023-01-01', periods=100, freq='M'),
      'Valores': np.cumsum(np.random.randn(100) + 0.5)}
serie = pd.DataFrame(data)
# Ajustando o modelo ARIMA
modelo = ARIMA(serie['Valores'], order=(1, 1, 1))
ajuste = modelo.fit()
# Resumo do modelo
print(ajuste.summary())