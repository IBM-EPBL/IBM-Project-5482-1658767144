import random
import time
import playsound

MAXIMUM_TEMPERATURE = 42
MAXIMUM_HUMIDITY = 60

while True:
    Temperature = random.randint(0, 100)
    Humidity = random.randint(0, 100)
    print("Temperature : "+str(Temperature)+"°C"+"    "+"Humidity : "+str(Humidity)+"%")
    if Temperature > MAXIMUM_TEMPERATURE and Humidity > MAXIMUM_HUMIDITY:
        print("Alert! Alert! Both Temperature and Humidity value crosses the required value")
        playsound.playsound("Temperature and Humidity.mp3")
    elif Temperature > MAXIMUM_TEMPERATURE:
        print("Alert! Alert! Temperature value crosses the required value")
        playsound.playsound("Temperature.mp3")
    elif Humidity > MAXIMUM_HUMIDITY:
        print("Alert! Alert! Humidity value crosses the required value")
        playsound.playsound("Humidity.mp3")
    print("\n")
    time.sleep(1)

