# Частично подсмотрено, не хочу копипастить 1:1 с рекурсией печаль.(, не заходит в цикл..( 2 последних варианта
# собраны из кусков с WEB.


a = int(input("Длина:  "))
b = int(input("Ширина: "))

area = a * b

def slice_to_qudrats(area):
    if area == 0:
        raise StopIteration
    while(area):
        for i in range(area, 0, -1):
            if i * i <= area:
                area -= i * i
                yield i
                break
        slice_to_qudrats(area)

result = list(slice_to_qudrats(area))
print(f" стороны квадратов {result} ")
print(f" Количество квадратов {len(result)} ")




#+ подсмотрено у Яны

def rectangle(a, b, n=0):
    if a == b:
        return n + 1
    elif a < b:
        return rectangle(a, b - a, n + 1)
    return rectangle(a - b, b, n + 1)


a = int(input("Сторона а=\n"))
b = int(input("Сторона b=\n"))

print(f"Прямоугольнику с длинами {a} и {b} можно нарезать {rectangle(a, b)} квадратов")



