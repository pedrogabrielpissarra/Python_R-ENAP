# carregar a biblioteca

library(cluster)

# código para gerar cluster

data <- iris[, -5]

clusters <- kmeans(data, centers = 3)

plot(data, col = clusters$cluster)