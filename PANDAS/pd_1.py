import pandas as pd

print("Введите путь до файлов с данными: ") 
path = str(input())

# cчитывание данных из файла
data = pd.read_csv(path)
n = data.shape[0] #количество строк в файле

# задача №1: ищем три крупнейшик платежа (max SUM)
# выбираем платежи из STATUS = OK
data_ok = data.loc[data.STATUS == 'OK']
print("#1: 3 самых крупных платежа: ")
print(data_ok.sort_values(by = 'SUM', ascending = False).iloc[0:3, :])

# задача №2: ищем полную сумму платежей в Umbrella, Inc
data_ok_umbr = data_ok.loc[data_ok.CONTRACTOR == "Umbrella, Inc"]
print("#2: полная сумма платежей в Umbrella, Inc:")
print(data_ok_umbr.SUM.sum())