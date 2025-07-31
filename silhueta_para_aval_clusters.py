from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score, silhouette_samples 
from sklearn.datasets import make_blobs 
import matplotlib.pyplot as plt 
import numpy as np 

# Gerando dados de exemplo 
data, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42) 

 

# Aplicando K-means 
kmeans = KMeans(n_clusters=4, random_state=42) 

labels = kmeans.fit_predict(data) 

# Calculando o coeficiente de silhueta 
silhouette_avg = silhouette_score(data, labels) 

sample_silhouette_values = silhouette_samples(data, labels) 

 
# Visualizando a análise de silhueta 
y_lower = 10 

plt.figure(figsize=(10, 6)) 

for i in range(4): 

   ith_cluster_silhouette_values = sample_silhouette_values[labels == i] 

   ith_cluster_silhouette_values.sort() 

   size_cluster = ith_cluster_silhouette_values.shape[0] 

   y_upper = y_lower + size_cluster 

   plt.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values) 

   y_lower = y_upper + 10 

plt.axvline(x=silhouette_avg, color="red", linestyle="--") 

plt.title("Gráfico de Silhueta para Avaliação de Clusters") 

plt.xlabel("Coeficiente de Silhueta") 

plt.ylabel("Amostras") 

plt.show() 