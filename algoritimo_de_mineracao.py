import pandas as pd 
from itertools import combinations 

# Dados simulados (transacional) 

data = {'Café': [1, 0, 1, 1], 

       'Leite': [1, 1, 0, 1], 

       'Pão': [1, 1, 0, 0], 

       'Queijo': [0, 1, 1, 0]} 

# Criando o DataFrame 

df = pd.DataFrame(data) 

# Função para calcular suporte 

def calculate_support(itemset, data): 

   return data[list(itemset)].all(axis=1).mean() 

# Função para calcular confiança 

def calculate_confidence(antecedent, consequent, data): 

   antecedent_support = calculate_support(antecedent, data) 

   rule_support = calculate_support(antecedent.union(consequent), data) 

   return rule_support / antecedent_support 

# Gerando regras 

min_support = 0.5 

min_confidence = 0.7 

frequent_items = [] 

# Encontrando itens frequentes (suporte mínimo) 

for i in range(1, len(data) + 1): 

   for combination in combinations(data.keys(), i): 

       support = calculate_support(set(combination), df) 

       if support >= min_support: 

           frequent_items.append((set(combination), support)) 

# Gerando as regras a partir dos itens frequentes 

rules = [] 

for itemset, support in frequent_items: 

   if len(itemset) > 1: 

       for antecedent in combinations(itemset, len(itemset) - 1): 

           antecedent = set(antecedent) 

           consequent = itemset - antecedent 

           confidence = calculate_confidence(antecedent, consequent, df) 

           if confidence >= min_confidence: 

               rules.append((antecedent, consequent, support, confidence)) 

# Exibindo os resultados 

print("Itens frequentes:") 

for itemset, support in frequent_items: 

   print(f"Itemset: {itemset}, Suporte: {support:.2f}") 

print("\nRegras de associação:") 

for antecedent, consequent, support, confidence in rules: 

   print(f"Regra: {antecedent} -> {consequent}, Suporte: {support:.2f}, Confiança: {confidence:.2f}") 