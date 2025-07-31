#carregando as bibliotecas 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay 
from sklearn.model_selection import train_test_split 
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt 

# Gerando dados sintéticos 
x, y = make_classification(n_samples=200, n_features=4, n_classes=2, random_state=42) 

# Dividindo os dados em treino e teste 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42) 

# Ajustando o modelo Random Forest 
model = RandomForestClassifier(random_state=42) 

model.fit(x_train, y_train) 

# Previsões e matriz de confusão 
y_pred = model.predict(x_test) 

cm = confusion_matrix(y_test, y_pred) 

# Visualizando a matriz de confusão 
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_) 

disp.plot(cmap="Blues") 

plt.title('Matriz de Confusão - Random Forest') 

plt.show()