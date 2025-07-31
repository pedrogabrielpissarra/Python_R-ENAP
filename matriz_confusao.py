import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay 

# Dados reais (valores verdadeiros) e predições do modelo 
y_true = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]  # Classes reais 

y_pred = [0, 1, 0, 1, 1, 1, 0, 0, 1, 0]  # Classes previstas pelo modelo 

# Gerar a matriz de confusão 
cm = confusion_matrix(y_true, y_pred, labels=[0, 1]) 

# Exibir a matriz de confusão de forma textual 
print("Matriz de Confusão:") 

print(cm) 

# Visualizar a matriz de confusão 
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1]) 

disp.plot(cmap=plt.cm.Blues) 

plt.title("Matriz de Confusão") 

plt.show() 