import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

# Dados de exemplo
data = np.array([

   [1, 2], [2, 3], [3, 4],

   [8, 8], [9, 9], [10, 10]

])

# Função para encontrar o medoid
def find_medoid(cluster):

   distances = cdist(cluster, cluster, metric='euclidean')

   medoid_index = np.argmin(distances.sum(axis=0))

   return cluster[medoid_index]

# Função K-Medoids simples
def k_medoids(data, k, max_iter=100):

   np.random.seed(42)

   medoids = data[np.random.choice(len(data), k, replace=False)]

   for _ in range(max_iter):

       # Atribuir pontos ao medoid mais próximo

       clusters = {i: [] for i in range(k)}

       for point in data:

           closest_medoid = np.argmin([np.linalg.norm(point - medoid) for medoid in medoids])

           clusters[closest_medoid].append(point)

       # Atualizar medoids

       new_medoids = []

       for i in range(k):

           cluster = np.array(clusters[i])

           if len(cluster) > 0:

               new_medoids.append(find_medoid(cluster))

           else:

               new_medoids.append(medoids[i])  # Manter o medoid original se o cluster estiver vazio

       if np.allclose(medoids, new_medoids):  # Se não houver mudança, pare

           break

       medoids = np.array(new_medoids)

   return medoids, clusters

# Aplicar K-Medoids
k = 2

medoids, clusters = k_medoids(data, k)

# Visualização
colors = ['r', 'b']

plt.figure(figsize=(8, 6))

for i, cluster in clusters.items():

   cluster = np.array(cluster)

   plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Cluster {i+1}', color=colors[i])

   plt.scatter(medoids[i, 0], medoids[i, 1], marker='X', s=200, color=colors[i], edgecolor='k', label=f'Medoid {i+1}')

plt.legend()

plt.title('K-Medoids Clustering')

plt.show()

# Atualizar medoids
new_medoids = []

for i in range(k):

   cluster = np.array(clusters[i])

   if len(cluster) > 0:

       new_medoids.append(find_medoid(cluster))

   else:

       new_medoids.append(medoids[i])  # Manter o medoid original se o cluster estiver vazio

if np.allclose(medoids, new_medoids):  # Se não houver mudança, pare

   pass

medoids = np.array(new_medoids)

# Aplicar K-Medoids novamente
k = 2

medoids, clusters = k_medoids(data, k)

# Visualização
colors = ['r', 'b']

plt.figure(figsize=(8, 6))

for i, cluster in clusters.items():

   cluster = np.array(cluster)

   plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Cluster {i+1}', color=colors[i])

   plt.scatter(medoids[i, 0], medoids[i, 1], marker='X', s=200, color=colors[i], edgecolor='k', label=f'Medoid {i+1}')

plt.legend()

plt.title('K-Medoids Clustering')

plt.show()