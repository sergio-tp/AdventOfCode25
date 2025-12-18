def repeated_sequence(n: int) -> bool:
    if (len(str(n)) % 2 != 0):
        return False
    else:
        mitad = int(len(str(n))/2)
        return int(n/(10**mitad)) == n % (10**mitad)

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
            if repeated_sequence(num):
                lista.append(num)
    return sum(lista)

adv2()