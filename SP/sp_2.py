import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

print("Введите путь до файла: ") 
path = str(input())

with open(path, 'r') as f:
    data = f.read()
    n = int(data.split()[0])
    data = data.splitlines()

    A = np.zeros((n, n))
    for i in range(1, n+1):
        A[i-1] =  data[i].split()

    b = np.array(data[n+1].split(), float)

    x = linalg.solve(A, b)
    l = np.linspace(1, len(x), len(x))

    f, ax = plt.subplots(figsize=(12, 6))
    plt.bar(l, x)
    plt.grid(which = 'major', color = 'gray')
    plt.savefig("sp_2_result.png")
    plt.show()
