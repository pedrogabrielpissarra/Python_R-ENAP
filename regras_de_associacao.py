# Importando bibliotecas necessárias 
import pandas as pd 
from itertools import combinations 

# Criando um dataset fictício 
data = {'Café': [1, 0, 1, 1, 0], 

       'Leite': [1, 1, 1, 0, 1], 

       'Pão': [0, 1, 0, 1, 1], 

       'Manteiga': [0, 1, 1, 0, 1]} 

# Convertendo em DataFrame 
df = pd.DataFrame(data) 

# Calculando suporte para itens únicos 
def calculate_support(itemset, data): 

   filtered_data = data.loc[:, itemset] 

   return (filtered_data.all(axis=1).sum()) / len(data) 

# Gerando todas as combinações de pares 
items = df.columns 

combinations_list = list(combinations(items, 2)) 

# Calculando suporte e confiança 
results = [] 

for pair in combinations_list: 

   antecedent, consequent = pair[0], pair[1] 

   support_pair = calculate_support(pair, df) 

   support_antecedent = calculate_support([antecedent], df) 

   confidence = support_pair / support_antecedent if support_antecedent > 0 else 0 

   results.append({ 

       "antecedent": antecedent, 

       "consequent": consequent, 

       "support": support_pair, 

       "confidence": confidence 

   }) 

 
# Convertendo os resultados para um DataFrame 
rules = pd.DataFrame(results) 

 # Exibindo as regras de associação 
print(rules)