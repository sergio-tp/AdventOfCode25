import numpy as np

prueba = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def input_to_matrix(input: str) -> np.ndarray:
    return np.matrix([[char for char in fila] for fila in input.split('\n')])

m = input_to_matrix(prueba)



def count_at(m: np.ndarray) -> np.ndarray:
    count = np.zeros_like(m, dtype=int)

    n_f, n_c = count.shape

    for i in range(n_f):
        for j in range (n_c):
            if m[i,j] == "@":
                vista = m[max(i-1,0):min(i+2,n_f),max(j-1,0):min(j+2,n_c)]
                sub_num = np.where(vista == "@",1,0)
                count[i,j] = np.sum(sub_num)
    result = np.where((count < 5) & (count != 0), 1, 0)
    return np.sum(result)

def read_txt(txt_path: str) -> list:
    with open(txt_path) as txt:
        txt_data = txt.read()
    lista = txt_data.splitlines()
    return np.matrix([[char for char in fila] for fila in lista])

def decorador(func):
    def wrapper():
        print("The total of rolls: ")
        print(func())
    return wrapper

@decorador
def adv4():
    l = read_txt("adv4.txt")
    return count_at(l)

adv4()