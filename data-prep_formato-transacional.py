# Importando bibliotecas necessárias 

import pandas as pd 

# Dados simulados (transações) 

data = {'Transação': [1, 1, 1, 2, 2, 3, 4, 4], 

       'Item': ['Pão', 'Leite', 'Café', 'Pão', 'Queijo', 'Café', 'Leite', 'Café']} 

# Criando um DataFrame 

df = pd.DataFrame(data) 

# Transformando os dados para o formato transacional (one-hot encoding) 

df_transacional = df.pivot_table(index='Transação', columns='Item', aggfunc=lambda x: 1, fill_value=0) 

# Exibindo o DataFrame transacional 

print("Dados preparados no formato transacional:") 

print(df_transacional)