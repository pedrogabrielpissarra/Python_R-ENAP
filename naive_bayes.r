# carregar o pacote 

library(e1071) 

#aplicar algoritmo 

model <- naiveBayes(Species ~ ., data = iris) 

predict(model, iris[, -5]) 