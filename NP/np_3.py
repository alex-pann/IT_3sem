import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from numpngw import AnimatedPNGWriter

print("Введите путь до файла с начальными данными: ") 
path = str(input())

with open (path, 'r') as f:
    start_data = np.loadtxt(f)
 
n = start_data.size
x = np.arange(n) # массив для оси х графика
t = np.arange(255) # массив отсчетов времени
seq = [] # последовательность состояний функции

fig, ax = plt.subplots()
line, = ax.plot(x, start_data) # начальное состояние функции

# обновление графика функции на i-ом отсчете времени
def update_line(i):
    line.set_ydata(seq[i])
    return line,

# рассчет состояний функции
A = np.eye(n) - np.diag(np.ones(n-1), -1)
A[0, n-1] = -1
for p in t:
    data = np.zeros(n)
    data =  start_data.transpose() - np.dot(0.5 * A, start_data.transpose())
    seq.append(data)
    start_data = data

# создание и сохраниение анимации
ani = animation.FuncAnimation(fig, update_line, np.arange(1, 225), init_func=None, interval=50)
plt.show()
writer = AnimatedPNGWriter(fps=12)
ani.save('process.png', dpi=60, writer=writer)