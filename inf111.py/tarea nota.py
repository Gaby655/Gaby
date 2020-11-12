user = "Gaby"
password = "1234567"
def division():
    a = int(input(" "))
    b = int(input(" "))
    c = 0
    while a>=b:
        a = a - b
        c = c + 1
    print("cociente", c)
    print("resto", a )
def divisores():



def numeros_capicua():


def cambio_de_base():


while(True):
    newUser = input()
    newPassword = input()
    if (newUser == user and newPassword == password):
        print("correcto, elija una opcion: ")
        print("para division precionar 1")
        print("para divisores precionar 2")
        print("para numeros capicua precionar 3")
        print("para cambio de base precionar 4")
        while(True):
            option = int(input())
            if (option == 1):
                division()
            if (option == 2):
                divisores()
            if (option == 3):
                numeros_capicua()
            if (option == 4):
                cambio_de_base()
        break
    else:
        print("inorrecto: ")