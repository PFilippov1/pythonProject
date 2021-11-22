# Удалить все элементы с заданным значением, если они имеются в списке.
from random import randrange
print('введите размер списка:')
n = int(input())
A = [randrange(0, 99) for i in range(n)]
print(A)

print("введите число, которое нужно удалить во всех вхождениях:")
delete = int(input())
A = [i for i in A if i != delete]
print("список после удаления:")
print(A)
