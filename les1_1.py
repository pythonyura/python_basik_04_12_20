"""Задание 1
    Поработайте с переменными, создайте несколько,
    выведите на экран, запросите у пользователя
    несколько чисел и строк и сохраните
    в переменные, выведите на экран.
"""
Number = 10
text = "Hello world"
fraction = 3.2
print(f"Заданное число: {Number}\nПриветственный тектс: {text} \nИ для примера дробное значение: {fraction}")

User_name = input("\nВведите свое имя ")
User_age = int(input("Введите свой возраст "))
User_number = int(input("Введите любимое число "))
print(f"Здравствуйте {User_name} \nВам: {User_age} года \nВаше любимое число: {User_number}")

"""Задание 2
    Пользователь вводит время в секундах. 
    Переведите время в часы, минуты и секунды 
    и выведите в формате чч:мм:сс. 
    Используйте форматирование строк.
"""
User_time = int(input("Введите время в секундах "))
hours = User_time // 3600
minuts = (User_time - hours *3600) //60
seconds = User_time - (hours * 3600 + minuts * 60)
print(f"Время в привычном формате {hours}час(ов):{minuts}минут:{seconds}секунд")

"""Задание 3
   Узнайте у пользователя число n.
    Найдите сумму чисел n + nn + nnn.
    Например, пользователь ввёл число 3.
    Считаем 3 + 33 + 333 = 369
"""
number = int(input("Введите число: "))
total = (number + int(str(number) + str(number)) + int(str(number) + str(number) + str(number)))
print(f"Получившееся число: {total}")

"""Задание 4
    Пользователь вводит целое положительное число.
    Найдите самую большую цифру в числе.
    Для решения используйте цикл while и арифметические операции.
"""
number = abs(int(input("Введите целое положительное число "))) # число пользователя возвращаем в абсолютное значение
max_number = number % 10    #% возвращает остаток
while number >= 1:
    number = number // 10
    if number % 10 > max_number:
        max_number = number % 10
    if number > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

"""Задание 5
    Запросите у пользователя значения выручки и издержек фирмы.
    Определите, с каким финансовым результатом работает фирма
    (прибыль — выручка больше издержек, или
    убыток — издержки больше выручки).
    Выведите соответствующее сообщение.
    Если фирма отработала с прибылью,
    вычислите рентабельность выручки (соотношение прибыли к выручке).
    Далее запросите численность сотрудников фирмы
    и определите прибыль фирмы в расчете на одного сотрудника.
"""
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

"""Задание 6
    Спортсмен занимается ежедневными пробежками. 
    В первый день его результат составил a километров. 
    Каждый день спортсмен увеличивал результат на 10 % 
    относительно предыдущего. 
    Требуется определить номер дня, на который общий 
    результат спортсмена составить не менее b километров. 
    Программа должна принимать значения параметров a и b и  
    выводить одно натуральное число — номер дня.
"""
result = int(input("Введите результаты пробежки первого дня в км "))
desired_value= int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = result
while result_km < desired_value:
        result = result + 0.1 * result
        result_days += 1
        result_km = result_km + result
print(f"Вы достигнете требуемых показателей на: {result_days}")