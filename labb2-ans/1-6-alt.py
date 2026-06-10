number = int(input("Ange ett tal: "))

table_elements = [number * i for i in range(1, 11)]

table_elements = [str(number) for number in table_elements]

max_letters = max([len(string) for string in table_elements])

for i, num in enumerate(table_elements):
    if i == 5:
        # Trycker en vanlig radbrytning efter de 5e talet.
        print()

    # end="" är ett nyckelordsargument som gör att den sedvanliga
    # radbrytningen inte förekommer.
    # :<10 gör att varje tal är minst 10 karaktärer bred + mellanslag.
    print(f"{num:<10} ", end="")
