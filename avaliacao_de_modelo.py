import numpy as np 
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score 
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split 

# Gerando um exemplo fictício de dados 

np.random.seed(42) 

X = np.random.rand(100, 1) * 10  # Variável independente (feature) 

y = 3 *  X.flatten() + np.random.randn(100) * 5   # Variável dependente (alvo) 

# Dividindo os dados em treino e teste 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

# Treinando um modelo de regressão linear 

model = LinearRegression() 

model.fit(X_train, y_train) 

# Fazendo previsões no conjunto de teste 

y_pred = model.predict(X_test) 

# Calculando as métricas de avaliação 

mae = mean_absolute_error(y_test, y_pred) 

mse = mean_squared_error(y_test, y_pred) 

rmse = np.sqrt(mse) 

r2 = r2_score(y_test, y_pred) 

# Exibindo os resultados 

print("Avaliação do Modelo de Regressão:") 

print(f"Erro Absoluto Médio (MAE): {mae:.2f}") 

print(f"Erro Quadrático Médio (MSE): {mse:.2f}") 

print(f"Raiz do Erro Quadrático Médio (RMSE): {rmse:.2f}") 

print(f"Coeficiente de Determinação (R²): {r2:.2f}")