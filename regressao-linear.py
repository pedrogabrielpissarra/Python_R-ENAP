# Importando as bibliotecas
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# Gerando dados sintéticos
np.random.seed(42)

x = np.random.rand(100, 1) * 10  # Feature

y = 3 * x + np.random.randn(100, 1) * 2 + 5  # Resposta com ruído

# Dividindo os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Ajustando o modelo de regressão linear
model = LinearRegression()

model.fit(x_train, y_train)

# Previsões
y_pred = model.predict(x_test)

# Visualizando o ajuste
plt.figure(figsize=(8, 6))

plt.scatter(x_test, y_test, label='Dados Reais', color='blue')

plt.plot(x_test, y_pred, color='red', label='Regressão Linear')

plt.title('Ajuste da Regressão Linear')

plt.xlabel('Variável Independente (x)')

plt.ylabel('Variável Dependente (y)')

plt.legend()

plt.show()