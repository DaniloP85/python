N = int(input())
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
if N < 1 or N > 26:
    print('numero informado invalido')
    exit
else:
    while i < N:
        letra = alfabeto[i]
        j = 0
        acumuladorDeLetras = ""
        t = i+1 # Quando i for 0, precisa pelo menos imprimir uma vez
        while j < t:
            acumuladorDeLetras = acumuladorDeLetras+letra
            j+=1

        print(acumuladorDeLetras)
        i+=1