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


# 3. Функция шейкерной (коктейльной) сортировки shaker - модификации пузырьковой:
def Shakesort(A):  # шейкерная
    for i in range(len(A) // 2):
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


# sample = [0, -1, 5, -2, 3]


#
# left = 0
# right = len(sample) - 1
#
# while left <= right:
#     for i in range(left, right, +1):
#         if sample[i] > sample[i + 1]:
#             sample[i], sample[i + 1] = sample[i + 1], sample[i]
#     right -= 1
#
#     for i in range(right, left, -1):
#         if sample[i - 1] > sample[i]:
#             sample[i], sample[i - 1] = sample[i - 1], sample[i]
#     left += 1
#
# print(sample)

def SelectSort(D):


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


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой"])
x = []
y1 = []
y2 = []
y3 = []
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

## какой-то косяк надо разбираться....
    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()),
                   str((t6 - t5).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.show()