#Мини проэкт : Простой Калькулятор

from colorama import init
from colorama import Fore, Back, Style


# use Colorama to make Termcolor work on Windows too
init()

print( Fore.BLACK)

print( Back.GREEN)

what = input("Что делаем? (+, -, *, **, %, //): ")

print( Back.YELLOW)

a = float(input("Введите первое число: "))

print( Back.CYAN)

b = float(input("Введите второе число: "))

#x = 0

print( Back.RED)

if what == "+":
	c = a + b
	print("Результат" + str(c))
		
elif what == "-":
	c = a - b
	print("Результат" + str(c))
		
elif what == "*":
	c = a * b
	print("Результат" + str(c))
		
elif what == "**":
	c = a ** b
	print("Результат" + str(c))
		
elif what == "%":
	c = a % b
	print("Результат" + str(c))
	
elif what == "//":
	c = a // b
	print("Результат" + str(c))
		
else:
	print("Выбрана неверная операция")
	#calc += 1
print( Back.GREEN)
print("Спасибо за использование мной)")
input()
