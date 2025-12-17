def num_to_list(n: int) -> list:
    numero = n
    l = []
    while (numero >= 10):
        l.append(numero % 10)
        numero = int(numero / 10)
    l.append(numero)
    l.reverse()
    return l

def repeated_sequence(l: list) -> bool:
    mitad = int(len(l)/2)
    return l[:mitad] == l[mitad:]

def read_txt(txt_path: str) -> list:
    with open(txt_path) as txt:
        txt_data = txt.read()
    lista_aux = txt_data.split(",")
    lista = []
    for elem in lista_aux:
        intervalo = [int(n) for n in elem.split("-")]
        lista.append(intervalo)
    return lista

def decorador(func):
    def wrapper():
        print("The sum of invalid IDs is: ")
        print(func())
    return wrapper

@decorador
def adv2():
    lista = []
    for list in read_txt("adv2.txt"):
        for num in range (list[0], list[1]+1):
            if repeated_sequence(num_to_list(num)):
                lista.append(num)
    return sum(lista)

adv2()