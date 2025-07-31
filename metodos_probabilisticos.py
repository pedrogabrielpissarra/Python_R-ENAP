from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Dados simulados 
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=4, random_state=42)

# Dividindo em treino e teste 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinando o modelo 
model = LogisticRegression()

model.fit(X_train, y_train)

# Predição e avaliação 
y_pred = model.predict(X_test)

print("Acurácia:", accuracy_score(y_test, y_pred))

print("Relatório de Classificação:\n", classification_report(y_test, y_pred))