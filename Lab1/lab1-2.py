import numpy as np

YEAR = 2021
age = [YEAR - 2010, YEAR - 2008, YEAR - 2011, YEAR - 2012, YEAR - 2011]
sex = ["male", "female", "male", "female", "male"]
weight = [40, 50, 45, 60, 55]
height = [130, 120, 150, 170, 180]

kids = np.array([[YEAR - 2010, YEAR - 2008, YEAR - 2011, YEAR - 2012, YEAR - 2011],
                 ["male", "female", "male", "female", "male"],
                 [40, 50, 45, 60, 55],
                 [130, 120, 150, 170, 180]])

# просто выведем наш массив с данными детей
for i in range(len(kids)):
    print(str(kids[i]))
# подсчет мальчиков и девочек
countMale = sex.count("male")
print("количество мальчиков " + str(countMale))
countFemale = sex.count("female")
print("количество девочек " + str(countFemale))
# посчет макс и мин возраста
maxAge = age[0]
minAge = age[0]
for i in range(len(age)):
    # print(age[i])
    if age[i] > maxAge:
        maxAge = age[i]
print("максимальный возраст: " + str(maxAge))
for i in range(len(age)):
    if age[i] < minAge:
        minAge = age[i]
print("минимальный возраст: " + str(minAge))
# подсчет среднего возраста
ageAverage = 0
for i in range(len(age)):
    ageAverage += age[i]
ageAverage = ageAverage / len(age)
print(f"средний возраст детей {ageAverage} лет")
#  подсчет роста, веса
maxWeight = max(weight)
print(f"максимальный вес {maxWeight}")
minWeight = min(weight)
print(f"минимальный вес {minWeight}")

maxHeight = max(height)
print(f"максимальный рост {maxHeight}")
minHeight = min(height)
print(f"минимальный рост {minHeight}")
# сопоставим данные по каждому ребенку, т.к. не нашел как можно сделать сопоставление для:
# ... что самый высокий мальчик весит больше всех в классе, а самая маленькая девочка является самой юной среди девочек
print(kids.transpose())
