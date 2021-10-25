import pandas as pd
import matplotlib.pyplot as plt

print("Введите путь до файла xslx: ")
path_1 = str(input())
print("Введите путь до файла html: ")
path_2 = str(input())

# cчитывание данных из файла
stud = pd.read_excel(path_1)
res = pd.read_html(path_2)[0]

stud = stud.rename(columns={'login': 'User'})

# объединяем данные в один DataFrame
data = pd.merge(stud, res, on = 'User')

# задача 1:
gr_faculty = data.group_faculty.unique() # факультетские группы
gr_out = data.group_out.unique() # группы по информатике

fig, ax = plt.subplots(1, 2)
ax[0].bar(gr_faculty, data.groupby('group_faculty').Solved.mean())
ax[1].bar(sorted(gr_out), data.groupby('group_out').Solved.mean())
plt.show()

# задача 2:
data_2  = data.loc[(data.G >= 10) | (data.H >= 10)]
print(data_2.loc[:, ["group_faculty", "group_out" ]])