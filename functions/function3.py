#Funciones con parametros
def print_param(daddy):
    print(daddy)
    print(daddy)

# No es necesario que el nobre del objeto que vamos a pasar 
# con argumento sea el mismo que el nombre del parámetro
print_param(77)

singer = "Adele"
print_param(singer)

def volumen(radio):
    result = 4/3 * 3.1416 * radio **3
    print(result)

big = 7
small = 2
volumen(big)
volumen(small)

def multiply_by_2(number):
    number = number * 2
    print(number)

multiply_by_2(big)
print(big)

# Función de dos parámetros
def concat_strings(str1,str2):
    longstr = str1 + " " + str2
    print(longstr)

text1 = "pasito a pasito"
text2 = "suave suavecito"

concat_strings(text1,text2)
