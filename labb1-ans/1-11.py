# Den omvända termometern (F -> C)
# Läs in temperatur i Fahrenheit och konvertera till Celsius

temp_F = float(input("Ange temperaturen i grader F: "))

# Omvandla enligt formeln: C = (F - 32) * 5/9
temp_C = (temp_F - 32) * (5 / 9)

print(f"Temperaturen i grader C: {temp_C}")
