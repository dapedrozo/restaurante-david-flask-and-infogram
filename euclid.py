def gcd():
    a,b=int(input("Escriba el valor de a: ")),int(input("Escriba el valor de b: "))
    while b != 0:
        a,b=b,a%b
    print(max(-a,a))
gcd()