"""
Fia Berggren Lindqvist
Operativsystem: Windows 10
"""

print("Welcome, here you can convert Fahrenheit to Celsius")
while True: #Starts a loop as long as the input is a ValueError
    try: #Tests if the input gives a ValueError
        fahrenheit = float(input("Please enter how many degrees Fahrenheit you would like to convert: "))
        break #If no ValueError arise, this cancels the loop
    except ValueError:
        print("Wrong type of input")



#Converts Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9


#This rounds off so the degrees always will be displayed with two decimals
celsius = ("{:.2f}".format(celsius))


print("Hello again, the temperature in Celsius is: ", celsius, "degrees.")

