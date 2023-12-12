x = input("zadejte promeněnou x: ")
y = input("zadejte promeněnou y: ")
x = int(x)
y = int(y)
print(" pro sčitaní zadejte +")
print(" pro odečitaní zadejte -")
print(" pro násobení zadejte *")
print(" pro dělení zadejte /")
print(" pro mocnění zadejte **, x = mocněnec a y = mocnitel")
print(" pro odmocnění zadejte /*, x = odmocněnec a y = odmocnitel")
znamenko = input("zadejte vaši volbu operatoru")
print(f"Výsledek: ")
if znamenko == "+":
    print(x+y)
elif znamenko == "-":
    print (x-y)
elif znamenko == "*":
    print(x*y)
elif znamenko == "/":
    if y == 0:
        print("Nulou nelze dělit!")
    else:
        print(x/y)
elif znamenko == "**":
    print(x**y)
elif znamenko == "/*":
    if y < 0:
     print(x**(1/y))

else:
    print("Neplatná volba")