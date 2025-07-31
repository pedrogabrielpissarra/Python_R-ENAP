# Importando as bibliotecas
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Gerando dados sintéticos para agrupamento
np.random.seed(42)

x1 = np.random.normal(10, 3, 100)

x2 = np.random.normal(20, 5, 100)

x3 = np.random.normal(30, 2, 100)

data = np.array(list(zip(np.concatenate([x1, x2, x3]), np.concatenate([x3, x1, x2]))))

# Aplicando o K-means
kmeans = KMeans(n_clusters=3, random_state=42)

labels = kmeans.fit_predict(data)

# Visualizando os clusters
plt.figure(figsize=(8, 6))

for i in range(3):  # Para cada cluster

   plt.scatter(data[labels == i, 0], data[labels == i, 1], label=f'Cluster {i+1}')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],

           s=200, c='red', marker='x', label='Centroids')

plt.title('Clusters formados pelo K-means')

plt.xlabel('Feature 1')

plt.ylabel('Feature 2')

plt.legend()

plt.show()