from sys import stdin
#Primer punto (Calcule la suma de todos los elementos de X)
def sumaVector(a):
    if (len(a)==1):
        return a[0]
    else:
        return a[0] + suma(a[1:])


#Segundo punto (Calcule el minimo del vector)
def minimoVector(a):
    if (len(a)==1):
        return a[0]
    else:
        if (a[0]< minimoVector(a[1:])):
            return a[0]
        else:
            return minimoVector(a[1:])

    
def main():
    a=[int(x)for x in stdin.readline().split()]
    print(minimoVector(a))
    
main()
