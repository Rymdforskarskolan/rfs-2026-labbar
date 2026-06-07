# Koordinater kan vara decimaler
x = float(input("Ange x-koordinat: "))
y = float(input("Ange y-koordinat: "))

if x == 0 and y == 0:
    print("Punkten ligger i origo.")
elif x == 0:
    print("Punkten ligger på y-axeln.")
elif y == 0:
    print("Punkten ligger på x-axeln.")
elif x > 0 and y > 0:
    print("Första kvadranten (x>0, y>0)")
elif x < 0 and y > 0:
    print("Andra kvadranten (x<0, y>0)")
elif x < 0 and y < 0:
    print("Tredje kvadranten (x<0, y<0)")
else:
    print("Fjärde kvadranten (x>0, y<0)")
