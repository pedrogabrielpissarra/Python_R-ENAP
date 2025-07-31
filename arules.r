#Instalar e carregar o pacote 

install.packages("arules") 

library(arules) 

data <- as(data.frame(Titanic), "transactions") 

rules <- apriori(data, parameter = list(supp = 0.1, conf = 0.8)) 

inspect(rules)