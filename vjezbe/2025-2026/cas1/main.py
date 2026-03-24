x = 5
x = 'marko'

def saberi(a: int, b: int) -> int:
    zbir = a + b
    return zbir

print('x =', x)

ime = input("Ime: ")
print("Ime =", ime)

if ime == "Janko":
    print("Necu ra radim sa jankom")
    exit()
elif ime == "Ana":
    print("Jesi li sigiran da zelis da nastavis?")
    ans = input("DA/NE: ")
    if ans == "DA":
        print("Ok, nastavljamo rad programa")
    else:
        print("Dobra odluka")
        exit()
else:
    print("Ok, nastavljamo rad programa")

niz=[1, 2, "Janko"]

for el in niz:
    print(el)

for i in range(5): #range(5) => 0, 1, 2, 3 ,4
    print(i)

print("$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5, 10, 2): #for(i=5;i<10;i+=2)
    print(i)

i = 5
suma = 0
while i < 10:
    # print(i, end=" ")
    suma = saberi(suma, i)
    i += 2

print(f"Zbir neparnih brojeva od 5 do 10 je : {suma}")

populacija = {
    "Berane": 20000,
    "Podgorica": 150000,
    "Danilovgrad": 15000,
    "Niksic": 60000
}

graf = {
    "Berane": ["Andrijevica", "Bijelo Polje"]
}

graf["Bijelo Polje"] = ["Berane"]
graf["Bijelo Polje"].append("Mojkovac")

graf["Mojkovac"] = []
graf["Mojkovac"].append("Bijelo Polje")
graf["Mojkovac"].append("Kolasin")

graf["Kolasin"] = []
graf["Kolasin"] += ["Berane", "Podgorica", "Mojkovac"]

print(graf)

print(f"Berane ima {populacija['Berane']} stanovnika")

for grad, br in populacija.items():
    print(f"{grad} ima {br} stanovnika")
