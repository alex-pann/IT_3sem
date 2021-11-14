import numpy as np
import matplotlib.pyplot as plt

print("Введите путь до файлов с данными: ") 
path = str(input())

for i in range (1, 4):
    name = "signal0" + str(i) + ".dat"
    file_path = path + name

    with open (file_path, 'r') as f:
        data = np.loadtxt(f)
        y_min = data.min()
        y_max = data.max()
        n = data.size
        l = np.linspace(0, n-1, n)

        fig, ax = plt.subplots(1, 2, figsize=(6, 4))
        ax[0].plot(l, data)
        ax[0].set_title("Исходный сигнал")
        ax[0].grid()
        ax[0].set(xlim=(0, 100), ylim=(y_min, y_max))

        data_filt = np.array(data)

        for k in range(0, n):
            if k < 10:
                data_prev = data[0:k+1]
                data_filt[k] = data_prev.mean()
            else:
                data_prev = data[k-9:k+1]
                data_filt[k] = data_prev.mean()


        ax[1].plot(l, data_filt)
        ax[1].set_title("Сигнал после фильтрации")
        ax[1].grid()
        ax[1].set(xlim=(0, 100), ylim=(y_min, y_max))

        plot_name = "plot_" + str(i) + ".jpg"
        plt.savefig(path + plot_name)
        print("Image " + plot_name + " created")

        plt.show()