from itertools import dropwhile

def largest_number(n: int) -> int:
    cadena = num_to_list(n)
    cadena = cadena[:-1]
    return (max(cadena))

def num_to_list(n: int) -> list:
    lista = []
    numero = n
    while (numero >= 10):
        lista.append(numero % 10)
        numero = numero // 10
    lista.append(numero)
    lista.reverse()
    return lista


def largest_joltage(n:int):
    cadena = num_to_list(n)
    lista = []
    numero_max = largest_number(n)
    if cadena[0] == numero_max:
        cadena = cadena[1:]
    else:
        cadena = list(dropwhile(lambda x: x != numero_max, cadena))
        cadena = cadena[1:]
    for num in cadena:
        lista.append(int(num) + largest_number(n)*10)
    return max(lista)

def read_txt(txt_path: str) -> list:
    with open(txt_path) as txt:
        txt_data = txt.read()
    lista = txt_data.splitlines()
    return [int(n) for n in lista]

def decorador(func):
    def wrapper():
        print("The total output joltage: ")
        print(func())
    return wrapper

@decorador
def adv3():
    lista = []
    for num in read_txt("adv3.txt"):
        lista.append(largest_joltage(num))
    return sum(lista)

listaej = [987654321111111, 811111111111119, 234234234234278, 818181911112111]

adv3()
print(num_to_list(1987654321111111))
print(largest_number(1987654321111111))
print(largest_joltage(1987654321111111))
print(largest_number(12345))