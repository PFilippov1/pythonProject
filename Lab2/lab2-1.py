# Вариант 2
# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.

a = []
for i in range(int(input("введите размер списка:"))):
    a.append(int(input(f"введите элемет")))
print(f" наш список {a}")
minimal = (a[0])
for i in range(len(a)):
    if a[i] < minimal:
        minimal = a[i]
print(f"наибольший нечетый элемент (если вводили нечетные числа) {minimal}")

modMin = abs(a[0])
for i in range(len(a)):
    if abs(a[i]) < modMin:
        modMin = abs(a[i])
print(f"минимальный элемент по модулю {modMin}")
