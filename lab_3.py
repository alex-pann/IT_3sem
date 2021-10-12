import matplotlib.pyplot as plt

print("Введите путь до файлов с данными: ") 
path = str(input())

preps = set()
groups = set()

with open(path, 'r') as f:

    # считываем имена всех преподавателей и номера всех групп
    for l in f.readlines(): 
        preps.add(l.split(";")[0])
        groups.add(l.split(";")[1])

    # создаем словари для marks per prep и marks per group
    data1 = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}}
    data2 = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}}

    # заполняем словари нулями
    for i in range(1, 11):
        for p in preps:
            data1[i][p] = 0
        for g in groups:
            data2[i][g] = 0
f.close()


with open(path, 'r') as f:
    # в каждой строке файла считываем преподавателя, группу, оценку
    for l in f.readlines():
        line = l.split(';')
        pr = line[0]
        gr = line[1]
        mark = int(line[2])

        data1[mark][pr] += 1
        data2[mark][gr] += 1

f.close()

fig, ax = plt.subplots(2, 1)

# список имен преподавателей
s = len(preps)
prep_lb = []
for i in range(0, s):
    prep_lb.append("prep" + str(i+1))

# сортировка словаря marks per prep
# (создание нового отсортированного словаря, 
# потому что у исходного нет метода сортировки)
sort_dict = {}
for k in prep_lb:
    sort_dict[k] = data1[1][k]

ax[0].bar(prep_lb, sort_dict.values(), 0.6, label='1') # вне цикла строим диаграмму для первой оценки
data = [d for d in sort_dict.values()]
for i in range(2, 11):
    sort_dict = {} # сортировка словаря повтаряется для каждой оценки i
    for k in prep_lb:
        sort_dict[k] = data1[i][k]

    sort_dict_prev = {} # также сортируем данные предыдущей оценки
    for k in prep_lb:
        sort_dict_prev[k] = data1[i-1][k]
    
    data_prev = [d for d in sort_dict_prev.values()]
    for j in range(0, len(data_prev)):
            data[j] = data[j]+data_prev[j]
    ax[0].bar(prep_lb, sort_dict.values(), 0.6, bottom=data, label=i)
ax[0].legend()
ax[0].set_title('Marks per prep')

# список номеров групп
s = len(groups)
group_lb = []
for i in range(0, s):
    group_lb.append(751 + i)

# сортировка словаря для marks per group
sort_dict_2 = {}

for t in group_lb:
    sort_dict_2[str(t)] = data2[1][str(t)]

# вторая диаграмма строится аналогично первой
ax[1].bar(group_lb, sort_dict_2.values(), 0.6, label='1') 
data = [d for d in sort_dict_2.values()]
for i in range(2, 11):
    sort_dict_2 = {}
    for t in group_lb:
        sort_dict_2[str(t)] = data2[i][str(t)]

    sort_dict_prev = {}
    for t in group_lb:
        sort_dict_prev[str(t)] = data2[i-1][str(t)]
    
    data_prev = [d for d in sort_dict_prev.values()]
    for j in range(0, len(data_prev)):
            data[j] = data[j]+data_prev[j]
    ax[1].bar(group_lb, sort_dict_2.values(), 0.6, bottom=data, label=i)
ax[1].legend()
ax[1].set_title('Marks per group')

plt.show()