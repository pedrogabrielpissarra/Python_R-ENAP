# Instalando a biblioteca apyori (caso ainda não esteja instalada) descomentar a linha 

# !pip install apyori 

from apyori import apriori 

# Criando um conjunto de transações fictício 

transactions = [ 

  ['leite', 'pão', 'manteiga'], 

  ['pão', 'manteiga', 'queijo'], 

  ['leite', 'café'], 

  ['leite', 'pão', 'manteiga', 'queijo'], 

  ['queijo', 'café'] 

] 

# Aplicando o algoritmo Apriori 

rules = apriori(transactions, min_support=0.5, min_confidence=0.7, min_lift=1.2, min_length=2) 

# Convertendo as regras em uma lista para exibição 

results = list(rules) 

# Exibindo as regras geradas 

for result in results: 

  print(f"Regra: {result.items}") 

  print(f" - Suporte: {result.support}") 

  for ordered_stat in result.ordered_statistics: 

      print(f" - Regra: {ordered_stat.items_base} => {ordered_stat.items_add}") 

      print(f"   - Confiança: {ordered_stat.confidence}") 

      print(f"   - Lift: {ordered_stat.lift}") 

  print("-" * 40) 