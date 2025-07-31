import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.cluster import DBSCAN 
from sklearn.datasets import make_moons 

 

# Gerando dados de exemplo 
data, _ = make_moons(n_samples=300, noise=0.05, random_state=42) 

 

# Aplicando o DBSCAN 
dbscan = DBSCAN(eps=0.2, min_samples=5) 

labels = dbscan.fit_predict(data) 

 

# Visualizando os resultados 
plt.figure(figsize=(8, 6)) 

plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=50, edgecolor='k') 

plt.title('Clustering com DBSCAN') 

plt.xlabel('Feature 1') 

plt.ylabel('Feature 2') 

plt.colorbar(label='Cluster') 

plt.show() 