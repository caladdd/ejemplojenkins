import math

def biseccion(f, xi, xf, tol, ite):
    fxi = f(xi)
    fxf = f(xf)
    if(fxi ==0):
        print(str(xi)+" es raiz")
    elif(fxf==0):
        print(str(xf)+" es raiz")
    elif(fxi*fxf < 0):
        xm = (xi+xf)/2
        fxm = f(xm)
        cont = 1
        error = tol+1
        while((error > tol) and (fxm != 0) and (cont < ite)):
            if(fxi*fxm < 0):
                xf = xm
                fxf = fxm
            else:
                xi = xm
                fxi = fxm
            xaux = xm
            xm = (xi+xf)/2
            fxm = f(xm)
            error = abs(xm - xaux)
            print("xi "+str(xi)+" xf "+str(xf)+" xm "+str(xm)+" fxm "+str(fxm)+" err "+str(error))
            cont += 1
        if(fxm == 0):
            print(str(xm)+" es raiz")
        elif(error < tol):
            print(str(xm)+" es un valor aproximado a una raiz con un error de "+str(tol))
        else:
            print("fracaso en "+str(ite)+" iteraciones")
    else:
        print("intervalo inadecuado")
            
    
def main():
    xi = input("xi\n")
    xf = input("xf\n")
    tol = input("tolerancia\n")
    ite = input("iteraciones\n")
    f = lambda x: math.exp(-3*x) - 6 * x**2  #function here
    #f = lambda x: math.exp(3*x-12) + x*math.cos(3*x) - x**2 + 4  #function here
    biseccion(f, float(xi), float(xf), float(tol), int(ite))

main()
