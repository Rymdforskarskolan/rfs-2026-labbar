# Två grupper som mängder
group_a = {"Alice", "Bob", "Charlie"}
group_b = {"Daniel", "Charlie", "Eva"}

# Ta in namnet, lämnas som str
name = input("Ange elevens namn: ")

# Här lagrar vi alltså resultatet av de booleska uttrycket
# in_a resp. in_b är True el. False beroende på deras kriterium
in_a = name in group_a
in_b = name in group_b

# Här använder endast det booleska värdet
# Du skall alltså INTE kolla in_a == True till exempel.
if in_a and in_b:
    print("Eleven finns i båda grupperna.")
elif in_a:
    print("Eleven finns endast i grupp A.")
elif in_b:
    print("Eleven finns endast i grupp B.")
else:
    print("Eleven finns i ingen av grupperna.")
