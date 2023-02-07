import random 

adorno = ""
titulo = "Adivina el numero"
print(adorno.center(50,"*"))
print(titulo.center(50).upper())
print(adorno.center(50, "*"))


def juego():    
    x = int(input("Ingrese un numero del 1 al 10: "))
    ram = random.randrange(1,10)

    if ram == x:
        print(f"Usted le atino al numero: {ram}")
    else:
        print(f"Lo siento no le atino el numero era: {ram}")


while True:
    juego()
    opcion = input("\nDesea Repetir Y/N: ")
    if opcion.upper() == 'Y':
        continue
    else:
        break
print("Gracias por jugar \nADIOS..")
