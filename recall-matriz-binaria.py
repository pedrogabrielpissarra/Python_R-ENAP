# carregando o pacote
from sklearn.metrics import precision_score, recall_score

# Matriz binária: 1 para itens recomendados, 0 para não recomendados
# Verdadeiros (o que o usuário realmente gostou)
true_labels = [1, 0, 1, 1, 0, 0, 1]

# Predições (o que o sistema recomendou)
predicted_labels = [1, 0, 1, 0, 0, 1, 1]

# Calculando precisão e recall
precision = precision_score(true_labels, predicted_labels)

recall = recall_score(true_labels, predicted_labels)

print(f"Precisão: {precision:.2f}")

print(f"Recall: {recall:.2f}")