# Создайте класс и поля соответствующему вашему варианту (поля статические и динамические).
# Создайте три метода (класса, объекта и статический). Выберете поле или метод для реализации
# инкапсуляции. Пропишите запись и считывание (get, set) инкапсулированных полей.
# Kласс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер

class Car:
    id = 0

    # конструктор
    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.__regNumber = 0      # вроде self.__regNumber = 0 можно и не указывать, т.к. будет сеттер
        Car.id += 1

    def getBrand(self):
        return brand

    def getModel(self):
        return model

    def getYear(year):
        return year

    def getColor(self):
        return color

    def getPrice(self):
        return price

    # решил назначить поле регистрационного номера приватным
    def getRegNumber(self):
        return self.__regNumber

    #  для приватного поля используем сеттер
    def setRegNumber(self, regNumber):
        self.__regNumber = regNumber

    # метод класса который будет каждый раз выводить ID+1 при создании объекта
    @classmethod
    def print_cars_id(cls):
        print(f"Car id is: {cls.id}")

    # Создадим статический метод для расчета скидки клиента
    @staticmethod
    def customer_discount(price):
        return price - (price * discount)


print("please set years experience of our service")

discount = int(input())

if (discount >= 0) and (discount < 2):
    discount = 0.05
elif (discount >= 2) and (discount < 5):
    discount = 0.1
elif discount >= 5:
    discount = 0.2
else:
    print("please enter correct value")

car1 = Car("toyota", "auris", 2017, "red", 12000)
Car.print_cars_id()
# добавляем рег. номер через сеттер
car1.setRegNumber("22-ff-44")
print(f" {car1.brand}, {car1.model}, {car1.year}, {car1.year}, {car1.price}, {car1.getRegNumber()}")
# посчитаем скидку
print(Car.customer_discount(car1.price))

car2 = Car("mazda", "cx-5", 2020, "blue", 22000)
Car.print_cars_id()
# добавляем рег. номер через сеттер
car2.setRegNumber("33-mm-55")
print(f" {car2.brand}, {car2.model}, {car2.year}, {car2.year}, {car2.price}, {car2.getRegNumber()}")
print(Car.customer_discount(car2.price))
