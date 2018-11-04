try:
    contador=0
    while True:
        print('Escribe la palabra')
        word=input()
        contador+=1
except KeyboardInterrupt:
    print('Total de Palabras:',contador)
