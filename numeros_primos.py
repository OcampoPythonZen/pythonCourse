primos=[]
for x in range(1,101):
    cont=0
    for y in range(1,x+1):
        if x%y==0:
            cont+=1
    if cont<=2:
        primos.append(x)
print(primos)
print('------------Doble ciclo para la combinacion-----------')
for i in range(1,10):
    for j in range(1,i+1):
        print(i,j)
        




