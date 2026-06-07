# Fråga efter tempen i C
# Notera att det nu inte måste vara heltal, så vi använder flyttal
temp_C = float(input("Ange temperaturen i grader C: "))

# Genomför beräkningen
temp_F = (temp_C * (9 / 5)) + 32

print(f"Temperaturen i grader F: {temp_F}")
