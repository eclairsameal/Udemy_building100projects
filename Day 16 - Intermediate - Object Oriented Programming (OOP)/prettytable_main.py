from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Abra", "Gastly", "Sandshrew"])
table.add_column("Type", ["Psychic", "Ghost · Poison", "Ground"])
#print(table.align)
table.align = "l"
print(table)

