import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error 

# Dados fictícios (variável independente X e dependente Y) 
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) 

Y = np.array([1.5, 3.8, 3.2, 5.5, 7.0]) 

# Criando o modelo de regressão linear 
modelo = LinearRegression() 

modelo.fit(X, Y) 

# Predições 
Y_pred = modelo.predict(X) 

# Visualização gráfica 
plt.scatter(X, Y, color='blue', label='Dados Originais')  # Dados reais 

plt.plot(X, Y_pred, color='red', label='Linha de Regressão')  # Linha ajustada 

plt.title('Regressão Linear Simples') 

plt.xlabel('X - Variável Independente') 

plt.ylabel('Y - Variável Dependente') 

plt.legend() 

plt.show() 

# Avaliação do modelo 
print(f"Coeficiente Angular (Beta 1): {modelo.coef_[0]}") 

print(f"Intercepto (Beta 0): {modelo.intercept_}") 

print(f"Erro Quadrático Médio: {mean_squared_error(Y, Y_pred):.2f}")