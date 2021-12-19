import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


# 2. Функция сортировки вставкой insert:


def InsertSort(A):
    for i in range(1, len(A)):
        t = A[i]
        j = i
        while j >= 0 and A[j - 1] > t:
            A[j] = A[j - 1]
            j -= 1
            A[j] = t


# 3. Функция шейкерной (коктейльной) сортировки shaker - модификации пузырьковой:

def Shakesort(A):  # шейкерная
    for i in range(len(A) // 2):  # работает только получение целой части от деления //
        for j in range(i, len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a
                for j in range(len(A) - 2 - i, i + 1):
                    if A[j] < A[j - 1]:
                        a = A[j]
                        A[j] = A[j - 1]
                        A[j - 1] = a


# 4. Функция сортировки выбором select:
# как-то быстро и график не рисует, нагуглил - работает, надо был не i, a i+1  for j in range(i + 1, len(A)):

# def SelectSort(A):
#     for j in range(len(A) - 1):
#         m = i
#     for j in range(i, len(A)):
#         if A[j] < A[m]:
#             m = j
#             A[m], A[i] = A[i], A[m]

def SelectSort(A):
    for i in range(0, len(A) - 1):
        m = i
        for j in range(i + 1, len(A)):
            if A[j] < A[m]:
                m = j
        A[i], A[m] = A[m], A[i]


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время Шейкерной",
                                 "Время Выбором", "Время вставкой"])
x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    # print(A)

    B = A.copy()
    C = A.copy()
    D = A.copy()
    E = A.copy()
    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)

    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B) - 1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    Shakesort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Шейкерная   " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")

    t7 = datetime.datetime.now()
    SelectSort(D)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Выбором   " + str(N) + "   заняла   " + str((t8 - t7).total_seconds()) + "c")

    t9 = datetime.datetime.now()
    InsertSort(E)
    t10 = datetime.datetime.now()
    y5.append((t10 - t9).total_seconds())
    print("Вставкой   " + str(N) + "   заняла   " + str((t10 - t9).total_seconds()) + "c")

    # какой-то косяк, не строится таблица, надо разбираться.., Разобрался (надо было в table поля добавить)..
    # Теперь графики не строятся (вроде отвалился matplotlib, но в pycharm ошибок нет) \\ Все строится.
    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()),
                   str((t6 - t5).total_seconds()), str((t8 - t7).total_seconds()),
                   str((t10 - t9).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.plot(x, y4, "C3")
plt.plot(x, y5, "C4")
plt.show()
