from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import classification_report 

# Carregando o dataset Iris 
data = load_iris() 

X, y = data.data, data.target 

# Dividindo em treino e teste 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 

# Treinando o modelo 
rf_model = RandomForestClassifier(n_estimators=100, random_state=42) 

rf_model.fit(X_train, y_train) 

# Predição e avaliação 
y_pred = rf_model.predict(X_test) 

print("Relatório de Classificação:\n", classification_report(y_test, y_pred)) 