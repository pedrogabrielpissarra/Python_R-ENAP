# carregando pacotes
import numpy as np
from scipy.sparse.linalg import svds

# Matriz de classificações (exemplo fictício)
ratings_matrix = np.array([

   [5, 3, 0, 1],

   [4, 0, 0, 1],

   [1, 1, 0, 5],

   [0, 0, 0, 4],

   [0, 0, 5, 4],

])

# Subtraindo a média do usuário para normalização
user_mean = np.mean(ratings_matrix, axis=1, keepdims=True)

normalized_matrix = ratings_matrix - user_mean

# Decomposição em valores singulares (SVD)
u, sigma, vt = svds(normalized_matrix, k=2)

# Reconstruindo a matriz com aproximação SVD
sigma_matrix = np.diag(sigma)

predicted_ratings = np.dot(np.dot(u, sigma_matrix), vt) + user_mean

print("Classificações previstas (após otimização):")

print(np.round(predicted_ratings, 2))