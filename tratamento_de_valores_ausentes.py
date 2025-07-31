# carregando os pacotes
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Exemplo de dados de recomendação
data = {

   'Filme A': [5, None, 4, 3],

   'Filme B': [7, 8, None, 5],

   'Filme C': [2, 5, 3, None]

}

# Criando o DataFrame
ratings = pd.DataFrame(data, index=['Usuário 1', 'Usuário 2', 'Usuário 3', 'Usuário 4'])

# Preenchendo valores ausentes com a média da coluna
ratings_filled = ratings.apply(lambda col: col.fillna(col.mean()), axis=0)

# Normalizando os dados para o intervalo [0, 1]
scaler = MinMaxScaler()

ratings_normalized = pd.DataFrame(

   scaler.fit_transform(ratings_filled),

   columns=ratings.columns,

   index=ratings.index

)

print("Dados Originais:\n", ratings)

print("\nDados Preenchidos:\n", ratings_filled)

print("\nDados Normalizados:\n", ratings_normalized)