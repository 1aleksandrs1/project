from pyowm import OWM

owm = OWM('7756e85622c34c360fb1eeac63b8a863')
mgr = owm.weather_manager()

place = input("В каком городе/стране?: ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print( "В городе " + place + " сейчас " + w.detailed_status)
print( "Температура сейчас в районе " + str(temp))

if temp < 10:
	print( "Сейчас очень холодно, хорошо одевайся! ")
elif temp < 20:
	print( "Сейчас холодно, оденься потеплее, но не в шортах) ")
else: 
	print( "На улице тепло, одевайся как хочешь. ")