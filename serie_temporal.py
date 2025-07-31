#Carregando os pacotes
import pandas as pd
import matplotlib.pyplot as plt
# Criando uma série temporal fictícia
data = {'Data': pd.date_range(start='2023-01-01', periods=24, freq='M'),
    'Valores': [20, 22, 19, 18, 21, 24, 25, 27, 29, 30, 31, 35,
        20, 23, 22, 24, 25, 28, 30, 33, 34, 36, 40, 42]}
serie = pd.DataFrame(data)
# Verificando a série
plt.figure(figsize=(10, 5))
plt.plot(serie['Data'], serie['Valores'], marker='o')
plt.title("Série Temporal: Verificação Visual")
plt.xlabel("Data")
plt.ylabel("Valores")
plt.grid()
plt.show()