k = int(input("Введите число\n"))
num = k
x = [int(a) for a in str(num)]
print(x)

frase1 = "мы нашли " + str(k) + " грибов"
frase2 = "мы нашли " + str(k) + " гриба"
frase3 = "мы нашли " + str(k) + " гриб"

if (x[0] >= 2 and x[-1] == 1) or (k == 1):
    print(frase3)
elif x[0] <= 4 and x[-1] <= 4:
    print(frase2)
elif (x[0] == 0 and x[-1] == 0) or (x[0] > 0 and x[-1] == 0) or (x[0] > 0 and x[-1] > 0 < 5):
    print(frase1)

# elif x[0] > 0 and x[-1] == 0:
#     print(frase1)
else:
    print(frase1)
    # print("Я уже весь в грыбах, грибов, грибей...")
