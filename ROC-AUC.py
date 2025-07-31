# Importando bibliotecas necessárias 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.datasets import make_classification 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import roc_curve, auc 

# Gerando um conjunto de dados sintético para classificação 
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15,  

                         n_redundant=5, random_state=42) 

# Dividindo os dados em treinamento e teste 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 

# Treinando um modelo de classificação 
model = RandomForestClassifier(random_state=42) 

model.fit(X_train, y_train) 

# Calculando as probabilidades para a classe positiva 
y_scores = model.predict_proba(X_test)[:, 1] 

# Calculando a curva ROC e a área sob a curva (AUC) 
fpr, tpr, thresholds = roc_curve(y_test, y_scores) 

roc_auc = auc(fpr, tpr) 

# Gerando o gráfico da curva ROC 
plt.figure(figsize=(8, 6)) 

plt.plot(fpr, tpr, color='blue', label=f'ROC Curve (AUC = {roc_auc:.2f})') 

plt.plot([0, 1], [0, 1], color='gray', linestyle='--', label='Random Guess') 

plt.xlabel('False Positive Rate (FPR)') 

plt.ylabel('True Positive Rate (TPR)') 

plt.title('Receiver Operating Characteristic (ROC) Curve') 

plt.legend(loc='lower right') 

plt.grid(alpha=0.3) 

plt.show() 