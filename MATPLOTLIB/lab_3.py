import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

print("Введите путь до файлов с данными: ") 
path = str(input())
path_data = path + 'students.csv' 

preps = set()
groups = set()

with open(path_data, 'r') as f:

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


with open(path_data, 'r') as f:
    # в каждой строке файла считываем преподавателя, группу, оценку
    for l in f.readlines():
        line = l.split(';')
        pr = line[0]
        gr = line[1]
        mark = int(line[2])

        data1[mark][pr] += 1
        data2[mark][gr] += 1

f.close()

fig, ax = plt.subplots(2, 1, figsize=(12, 8))

s = len(preps)
prep_lb = []
for i in range(0, s):
    prep_lb.append("prep" + str(i+1))

ax[0].bar(prep_lb, sorted(data1[1].values(), key = lambda key: data1[1].keys()), 0.6, label='1')
data = [d for d in sorted(data1[1].values(), key = lambda key: data1[1].keys())]
for i in range(2, 11):
    data_prev = [d for d in sorted(data1[i-1].values(), key = lambda key: data1[i-1].keys())]
    for j in range(0, len(data_prev)):
        if i != 2:
            data[j] = data[j]+data_prev[j]
    ax[0].bar(prep_lb, sorted(data1[i].values(), key = lambda key: data1[i].keys()), 0.6, bottom=data, label=i)
ax[0].yaxis.set_major_locator(ticker.MultipleLocator(3))
ax[0].legend(loc='right')
ax[0].set_title('Marks per prep')

s = len(groups)
group_lb = []
for i in range(0, s):
    group_lb.append(751 + i)

ax[1].bar(group_lb, data2[1].values(), 0.6, label='1')
data = [d for d in data2[1].values()]
for i in range(2, 11):
    data_prev = [d for d in data2[i-1].values()]
    for j in range(0, len(data_prev)):
        if i != 2:
            data[j] = data[j]+data_prev[j]
    ax[1].bar(group_lb, data2[i].values(), 0.6, bottom=data, label=i)
ax[1].yaxis.set_major_locator(ticker.MultipleLocator(3))
ax[1].legend(loc='right')
ax[1].set_title('Marks per group')

plt.savefig(path + "graphs.png")
plt.show()
