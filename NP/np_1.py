import numpy as np
from PIL import Image

print("Введите путь до файлов с данными: ") 
path = str(input())

for i in range (1, 4):
    name = "lunar0" + str(i) + "_raw.jpg"
    file_path = path + name
    # считаем картинку в numpy array
    img = Image.open(file_path)
    data = np.array(img)

    a = data.min()
    b = data.max()

    k = 255/(b - a)

    new_data = np.array( data * k - 255* a/(b-a), dtype=np.uint8)

    # запись картинки после обработки
    new_name = "new_" + name
    new_file_path = path + new_name
    res_img = Image.fromarray(new_data)
    res_img.save(new_file_path)
    print("Image " + new_name + " created")