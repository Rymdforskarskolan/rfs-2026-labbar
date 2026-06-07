minutes = int(input("Ange hur många minuter du har: "))

if minutes < 20:
    plan = "Kort pass"
elif minutes <= 45:
    plan = "Normalt pass"
else:
    plan = "Långt pass"

print(plan)
