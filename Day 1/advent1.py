def parse_code(codigo: str) -> int:
    """
    Convierte el código en un número negativo o positivo en función de R(+) O L(-)
    """
    signo = codigo[0]
    numero = int(codigo[1:])
    if (signo == "L"):
        return -numero
    else:
        return numero
    
lista = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

def count_cero(l: list) -> int:
    numero = 50
    contador = 0
    for num in l:
        numero += parse_code(num)
        if numero % 100 == 0:
            contador += 1
            numero = 0
        if numero > 100:
            numero = numero % 100
        if numero < 0:
            numero = numero % 100 + 100
    return contador

def read_txt(txt_path: str) -> list:
    with open(txt_path) as txt:
        txt_data = txt.read()
    lista = txt_data.splitlines()
    return lista

def decorador(func):
    def wrapper():
        print("The password is: ")
        print(func())
    return wrapper

@decorador
def adv1():
    return count_cero(read_txt("adv1.txt"))

adv1()