# Частично подсмотрено, не хочу копипастить 1:1 с рекурсией печаль.(, не заходит в цикл..(


length = int(input("Длина:  "))
width = int(input("Ширина: "))

result = []
s = length * width

break_out_flag = False
def slice_to_qudrats(s):
    if s == 0:
      raise StopIteration
    else:
        while s > 0:
            for i in range(s, 0, -1):
                if length < width:
                    length, width = width, length
    result.append(width)
    length -= width
    slice_to_qudrats(s)

print(f" стороны квадратов {result} ")
print(f" Количество квадратов {len(result)} ")
