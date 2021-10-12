import matplotlib.pyplot as plt


print("Введите путь до файлов с данными: ") 
path = str(input())

files = ["001.dat", "002.dat", "003.dat", "004.dat", "005.dat"]

for fl in files:
    path_f = path  + fl

    c_x = [] # координаты точек по х
    c_y = [] # координаты точек по у
    data = [] # все данные

    with open(path_f, 'r') as f:
        data = f.read()
        n = int(data.split()[0]) # количество точек 
        data = data.splitlines() # считываем построчно координаты
        for i in range(0, n):
            c_x.append(float(data[i+1].split(" ")[0])) # зполняем массивы координат
            c_y.append(float(data[i+1].split(" ")[1]))

    # строим графики (отдельно для каждого файла)
    plt.scatter(c_x, c_y, 0.9)

    plt.title(fl)
    plt.axis('scaled')
    plt.show()


   




