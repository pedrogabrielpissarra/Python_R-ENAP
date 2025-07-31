install.packages("forecast") 

library(forecast) 

data <- ts(rnorm(100), frequency = 12) 

model <- auto.arima(data) 

forecast(model, h = 12)