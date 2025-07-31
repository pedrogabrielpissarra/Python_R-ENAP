import numpy as np 
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram, linkage 

# Gerando dados simulados 
np.random.seed(42) 
data = np.random.rand(10, 2)  # 10 pontos com 2 variáveis 

# Calculando o linkage (método aglomerativo com linkagem completa) 
linked = linkage(data, method='complete') 

 
# Plotando o dendrograma 
plt.figure(figsize=(8, 5)) 
dendrogram(linked, labels=range(1, 11), leaf_rotation=45, leaf_font_size=10) 
plt.title('Dendrograma - Agrupamento Hierárquico') 
plt.xlabel('Amostras') 
plt.ylabel('Distância Euclidiana') 
plt.show() 