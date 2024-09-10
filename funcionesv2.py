print("mas sobre funciones")
#aqui se escriben las funciones
def suma_ab(a,b):
    s = a + b
    return s
def resta_cd(c,d):
    r = c - d
    return r
def multi_fg(f,g):
    m = f * g
    return m
def divi_hi(h,i):
    d = h / i
    return d
#llamadas a funciones
#suma 
print("--calculamos suma--")
n1=int(input("ingresa el primer numero "))
n2=int(input("ingresa el segundo numero "))
suma = suma_ab(n1,n2)
print(f"la suma de {n1} + {n2} es {suma}")
#resta
print("--calculamos resta--")
n01=int(input("ingresa el primer numero "))
n02=int(input("ingresa el segundo numero "))
resta = resta_cd(n01,n02)
print(f"la resta de {n01} - {n02} es {resta}")
#multiplicacion
print("--calculamos multiplicacion--")
num1=int(input("ingresa el primer numero "))
num2=int(input("ingresa el segundo numero "))
multiplicacion = multi_fg(num1,num2)
print(f"la multiplicacion de {num1} x {num2} es {multiplicacion}")
#division
print("--calculamos divison--")
nume1=int(input("ingresa el primer numero "))
nume2=int(input("ingresa el segundo numero "))
division = divi_hi(nume1,nume2)
print(f"la division de {nume1} / {nume2} es {division}")

