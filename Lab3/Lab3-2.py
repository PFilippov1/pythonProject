# Частично подсмотрено, не хочу копипастить 1:1 с рекурсией печаль.(, не заходит в цикл..( 2 последних варианта
# собраны из кусков с WEB.

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



# a = int(input("Длина:  "))
# b = int(input("Ширина: "))
#
# area = a * b
#
# def slice_to_qudrats(area):
#     if area == 0:
#         raise StopIteration
#     while(area):
#         for i in range(area, 0, -1):
#             if i * i <= area:
#                 area -= i * i
#                 yield i
#                 break
#         slice_to_qudrats(area)
#
# result = list(slice_to_qudrats(area))
# print(f" стороны квадратов {result} ")
# print(f" Количество квадратов {len(result)} ")


#
# length = int(input("Длина:  "))
# width = int(input("Ширина: "))
#
# result = []
#
# while (length > 0):
#     if length < width:
#         length, width = width, length
#     result.append(width)
#     length -= width
#

# a=len(result)
# print(f" стороны квадратов {result} ")
# print(f" Количество квадратов {len(result)} ")




