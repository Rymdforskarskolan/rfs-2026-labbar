# Fråga efter summan
total = int(input("Ange summan pengar i hela kr: "))

# Vi delar på tusen och stryker decimalerna
num_1000 = total // 1000
# Vi tar sedan bort så många tusenlappar som vi fick
total -= num_1000 * 1000

# Samma sak för resten av valörerna
num_500 = total // 500
total -= num_500 * 500

num_200 = total // 200
total -= num_200 * 200

num_100 = total // 100
total -= num_100 * 100

num_50 = total // 50
total -= num_50 * 50

num_20 = total // 20
total -= num_20 * 20

num_10 = total // 10
total -= num_10 * 10

num_5 = total // 5
total -= num_5 * 5

num_2 = total // 2
total -= num_2 * 2

# Eftersom alla valörer är sparade som variabler är det bara att trycka ut dem.
print("Valörer som krävs:")
print(f"1000kr: {num_1000}")
print(f"500kr: {num_500}")
print(f"200kr: {num_200}")
print(f"100kr: {num_100}")
print(f"50kr: {num_50}")
print(f"20kr: {num_20}")
print(f"10kr: {num_10}")
print(f"5kr: {num_5}")
print(f"2kr: {num_2}")
# Totalen vid slutet är alltid 1 eller 0,
# Vi kan printa den för att spara en beräkning
print(f"1kr: {total}")
