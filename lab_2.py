import matplotlib.pyplot as plt

print("Введите путь до файлов с данными: ") 
path = str(input())

with open(path, 'r') as f:
    data = f.read()
    n = len(data.splitlines()) # количество строк
    data = data.splitlines()

fig, axs = plt.subplots(nrows=2, ncols=3)

for i in range(0, n, 2):
    # считываем из файла массивы коррдинат
    data_x = []
    for w in data[i].split(" "):
        data_x.append(float(w))

    data_y = []
    for m in data[i+1].split(" "):
        data_y.append(float(m))

    k = int(i/2 + 1) #перевод i в номер графика [1, 6]
    
    # построение графиков
    if ( k <= 3):
        axs[0][k-1].plot(data_x, data_y)
        axs[0][k-1].minorticks_on()
        axs[0][k-1].grid(which = 'major', color = 'k')
        axs[0][k-1].grid(which = 'minor', color = 'gray')
        axs[0][k-1].set(title = k)
        axs[0][k-1].set_ylim([-15, 15])
    else:
        axs[1][k-4].plot(data_x, data_y)
        axs[1][k-4].minorticks_on()
        axs[1][k-4].grid(which = 'major', color = 'k')
        axs[1][k-4].grid(which = 'minor', color = 'gray')
        axs[1][k-4].set(title = k)
        axs[1][k-4].set_ylim([-15, 15])

plt.show()