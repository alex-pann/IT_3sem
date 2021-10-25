import pandas as pd
import matplotlib.pyplot as plt

print("Введите путь до файла с данными: ") 
path = str(input())

# cчитывание данных из файла
data = pd.read_csv(path)

n = len(data.CARGO.unique()) # количество различных авиакомпаний

# списки данных о количестве полетов, стоимости и массе
# для построения графиков
flights = []
prices = []
weight = []
for i in range (n):
    name = data.CARGO.unique()[i] # название авиакомании
    data_sep = data[data.CARGO == name] # отделяем данные только по выбраной компании
    print(
        'Авиакомпания', name, '\n', 'Количество рейсов:', data_sep.CARGO.count(), '\n',
        'Полная стоимость перевезенных грузов:', data_sep.PRICE.sum(), '\n','Полная масса перевезенных грузов:', data_sep.WEIGHT.sum(), '\n')
    flights.append(data_sep.CARGO.count())
    prices.append(data_sep.PRICE.sum())
    weight.append(data_sep.WEIGHT.sum())

# построение графиков
fig, ax = plt.subplots(3, 1)
ax[0].pie(flights, labels = data.CARGO.unique(), autopct='%1.1f%%', radius = 1.2)
ax[0].set_title('Количество рейсов')

ax[1].pie(prices, labels = data.CARGO.unique(), autopct='%1.1f%%', radius = 1.2)
ax[1].set_title('Полная стоимость')

ax[2].pie(weight, labels = data.CARGO.unique(), autopct='%1.1f%%', radius = 1.2)
ax[2].set_title('Полная масса грузов')

plt.show()
