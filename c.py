import math

def incremental(f, x0, delta, ite):
        fx0 = f(x0)
            if(fx0 == 0):
                        print(str(x0)+" es raiz")
            else:
                        x1 = x0 + delta
                                cont = 1
                                        fx1 = f(x1)
                                                while((fx0*fx1 > 0) and (cont < ite)):
                                                                x0 = x1
                                                                            fx0 = fx1
                                                                                        x1 = x0 + delta
                                                                                                    fx1 = f(x1)
                                                                                                                print("x0="+str(x0)+" fx0="+str(fx0)+ " x1="+str(x1)+" fx1 = "+str(fx1))
                                                                                                                            cont += 1
                                                                                                                                    if(fx1 == 0):
                                                                                                                                                    print(str(x1)+" es raiz")
                                                                                                                                    elif(fx0*fx1 < 0):
                                                                                                                                                    print("hay una raiz entre "+str(x0)+" y "+str(x1))
                                                                                                                                    else:
                                                                                                                                                    print("fracaso en "+str(ite)+" iteraciones")


                                                                                                                                                    def main():
                                                                                                                                                            x0 = input("x0\n")
                                                                                                                                                                delta = input("delta\n")
                                                                                                                                                                    ite = input("iteraciones\n")
                                                                                                                                                                        f = lambda x: math.exp(-x**2+5) + math.log(x**2 + 3) - 4*x + 45
                                                                                                                                                                            #3#f = lambda x: math.log(x**2 +1 ) - 6*x * math.cos(3*x - 3) + 4*x - 8
                                                                                                                                                                                #math.exp(3*x-12) + x*math.cos(3*x) - x**2 + 4  #function here
                                                                                                                                                                                    incremental(f, float(x0), float(delta), int(ite))

                                                                                                                                                                                    main()
