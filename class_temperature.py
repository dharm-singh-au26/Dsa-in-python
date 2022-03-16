"""
Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
"""

class Temprature():
    def  convertFahrenhiet(self,celsius):
        return (celsius*(9/5))+32
    def convertCelsius(self,farenhiet):
        return (farenhiet-32)*(5/9)
    
T = Temprature()
print(T.convertCelsius(49),T.convertFahrenhiet(49))