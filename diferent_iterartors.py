"""

Loops to explain iterators, recuerda subir los ejercicio de python a ]GITHUB[

"""

def main():
    days = ['sunday','monday','tuersday','wednsday','thursday','friday','saturday','another']
    daysF = ['Dim','Lun','Mar','Mer','Jeu','Ven','Sam','another']

    #TODO: use iter to create an iterator over collection
    i=iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print('--------------------')

    #TODO: use iterate usin a function and a sentinel
    with open("TxtPython.txt","r") as fp:
        for line in iter(fp.readline,''): # // As a sentinel & fp as a file pointer of the TxtPython File
            print(line)
    print('--------------------')

    #TODO: use regular interation over days
    for m in days:
        print(m)
    print('--------------------')

    for m in range(len(days)):
        print(m+1,days[m])
    print('--------------------')

    #TODO: using enumarate reduces code and provide a counter
    for i,m in enumerate(days,start=1):
        print(i,m)
    print('--------------------')

    #TODO: use zip to combine sequences at the same time days and daysF
    for m in enumerate(zip(days,daysF),start=1):
        print(m)
    print('--------------------')

    for i,m in enumerate(zip(days,daysF),start=1):
        print(i, m[0], '=', m[1], 'in French ')


if __name__=="__main__":
    main()
