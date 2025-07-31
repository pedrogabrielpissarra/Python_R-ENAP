# importando bibliotecas 
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity 

# Dados de exemplo: matriz de usuários e preferências de itens 
data = {'Filme A': [5, 4, 0, 0], 

       'Filme B': [4, 0, 0, 3], 

       'Filme C': [0, 0, 4, 5], 

       'Filme D': [0, 3, 5, 4]} 

# Criando um DataFrame 
ratings = pd.DataFrame(data, index=['Usuário 1', 'Usuário 2', 'Usuário 3', 'Usuário 4']) 

# Calculando similaridade de usuários 
similarity = cosine_similarity(ratings.fillna(0)) 

# Exibindo a matriz de similaridade 
similarity_df = pd.DataFrame(similarity, index=ratings.index, columns=ratings.index) 

print("Matriz de Similaridade:\n", similarity_df)