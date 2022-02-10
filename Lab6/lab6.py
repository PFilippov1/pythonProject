# 1. Скопировать в файл F2 только четные строки из F1.
# Подсчитать размер файлов F1 и F2 (в байтах).


import os

file1 = "f1.txt"
file2 = "f2.txt"


try:


    file1 = open("f1.txt", "r")
    file2 = open("f2.txt", "w")
    # Читаем все строки
    Lines_of_file = file1.readlines()

    # запись во второй файл четных строк,  начиная со второй с шагом 2 [start: stop: step]
    file2.writelines(Lines_of_file[1::2])

    # подсчет размера в байтах
    print(os.path.getsize("f1.txt"))
    print(os.path.getsize("f2.txt"))

    file1.close()
    file2.close()

except FileNotFoundError:
    print("Can not find source file")
except IOError:
    print("Error reading or writing  file")
