# Fråga efter summan
total = int(input("Ange summan pengar i hela kr: "))

# Vi kollar resten med 1000
remainder = total % 1000
num_1000 = (total - remainder) / 1000
# Vi drar bort antalet tusenlappar från totalen
total -= num_1000 * 1000

remainder = total % 500
num_500 = (total - remainder) / 500
total -= num_500 * 500

remainder = total % 200
num_200 = (total - remainder) / 200
total -= num_200 * 200

remainder = total % 100
num_100 = (total - remainder) / 100
total -= num_100 * 100

remainder = total % 50
num_50 = (total - remainder) / 50
total -= num_50 * 50

remainder = total % 20
num_20 = (total - remainder) / 20
total -= num_20 * 20

remainder = total % 10
num_10 = (total - remainder) / 10
total -= num_10 * 10

remainder = total % 5
num_5 = (total - remainder) / 5
total -= num_5 * 5

remainder = total % 2
num_2 = (total - remainder) / 2
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
