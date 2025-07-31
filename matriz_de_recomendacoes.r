#instale e carregue o pacote 

install.packages("recommenderlab") 

library(recommenderlab) 

data <- matrix(runif(100, 0, 5), nrow = 10) 

rec <- Recommender(as(data, "realRatingMatrix"), method = "UBCF") 

predict(rec, as(data, "realRatingMatrix"), n = 2) 