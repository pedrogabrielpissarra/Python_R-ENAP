#carregar pacotes 
from sklearn.neighbors import NearestNeighbors 
import numpy as np 

# Criando dados de exemplo (usuários x itens) 
user_item_matrix = np.array([[5, 3, 0, 1], 

                            [4, 0, 0, 1], 

                            [1, 1, 0, 5], 

                            [0, 0, 5, 4], 

                            [0, 3, 4, 0]]) 

# Ajustando o modelo KNN 
knn = NearestNeighbors(metric='cosine', algorithm='brute') 

knn.fit(user_item_matrix) 

# Encontrando os vizinhos mais próximos do usuário 0 
distances, indices = knn.kneighbors(user_item_matrix[0].reshape(1, -1), n_neighbors=2) 

# Exibindo os resultados 
print("Vizinhos mais próximos:", indices) 

print("Distâncias:", distances) 