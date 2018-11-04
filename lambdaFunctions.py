"""
Lambda structure:

lambda (parameters) : (expression)

"""

# Im gonna put the functions and reduce the function to lambda expression after it

def CelsiusToFharenheit(temp):
    return (temp * 9/5) + 32

def FharenheitToCelsius(temp):
    return (temp - 32) * 5/9

def main():
    ctemps = [0,12,34,100]
    ftemps = [32,65,100,212]

    #TODO: Use regular function to converts temps
    print(list(map(FharenheitToCelsius,ftemps)))
    print(list(map(CelsiusToFharenheit,ctemps)))

    print('-------------------------------------')
    #TODO: Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t - 32) * 5/9,ftemps)))
    print(list(map(lambda temp: (temp * 9/5) + 32,ctemps)))

    #CelsiusToFharenheit sustituimos palabra reservada lambda seguida de variable o nombre t : despues de los puntos la expresion
    # al final se le pasan los parametros que se van a realizar con la funcion incognita

if __name__=='__main__':
    main()
