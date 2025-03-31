from prettytable import PrettyTable

table = PrettyTable(["Pokemon Name","Type"])
table.add_row(["Charmander","Fire"])
table.add_row(["Squirtle","Water"])
table.add_row(["Bulbasaur","Grass"])
table.align="l"
print(table)