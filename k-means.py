# carregando as bibliotecas 
from sklearn.cluster import KMeans 
import numpy as np 
import matplotlib.pyplot as plt 

# Gerando dados simulados 
np.random.seed(42) 

data = np.random.rand(100, 2)  # 100 pontos com 2 variáveis 

# Aplicando o K-means 
kmeans = KMeans(n_clusters=3, random_state=42) 

kmeans.fit(data) 

# Obtendo os centroides e os rótulos 
centroids = kmeans.cluster_centers_ 

labels = kmeans.labels_ 

# Visualizando os resultados 
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', marker='o') 

plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroides') 

plt.title('Resultados do K-means') 

plt.xlabel('Variável 1') 

plt.ylabel('Variável 2') 

plt.legend() 

plt.show() 