n=5
table=[n*i for i in range (1,11)]
print(table)
with open("tables.txt", "w") as f:
    f.write(f" table of {n} {str(table)} + \n")