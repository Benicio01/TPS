def crear_grilla(desc):
    grilla = desc
    for i in range(len(desc)): 
       print(grilla[i])
    return grilla

def dimensiones(grilla):
    contadorColumnas = len(grilla[0]) 
    contadorFilas = len(grilla)
    return(contadorColumnas, contadorFilas)
    
def hay_pared(grilla, c, f):    
    if(grilla[f][c] == "#"):
        return True
    return False
    
def hay_objetivo(grilla, c, f):   
    if(grilla[f][c] == "." or grilla[f][c] == "*" or grilla[f][c] == "+"):
        return True
    return False 
    
def hay_caja(grilla, c, f): 
    if(grilla[f][c] == "$" or grilla[f][c] == "*"):
        return True
    return False
    
def hay_jugador(grilla, c, f): 
    if(grilla[f][c] == "@" or grilla[f][c] == "+"):
        return True
    return False

def contar_objetivos(grilla):
    cant_objetivos = 0
    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            if hay_objetivo(grilla, j, i) == True:
                cant_objetivos += 1
    return cant_objetivos
            

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    contador = 0
    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            if(hay_caja(grilla, j, i) and hay_objetivo(grilla, j, i)):
                contador += 1
    if contador == contar_objetivos(grilla):
        return True
    return False

def clonar(grilla):
    nuevaGrilla = []
    for i in range(len(grilla)): 
       nuevaGrilla.append(list(grilla[i]))
    return nuevaGrilla

def mover(grilla, direccion):
    nuevaGrilla = clonar(grilla)
    retorno = 0
    if(direccion == (-1, 0) or direccion == (1, 0) or direccion == (0, -1) or direccion == (0, 1)):
        if(direccion == (-1, 0)):
                for i in range(len(grilla)):
                    for j in range(len(grilla[i])):
                        if(hay_jugador(grilla, j, i) == True and hay_pared(grilla, j-1, i) == False):
                            if (hay_caja(grilla, j-1, i) == True) and (hay_caja(grilla, j-2, i) == True):#validacion doble caja
                                return grilla
                            
                            elif (hay_caja(grilla, j-1, i) == True) and hay_pared(grilla, j-2, i) == True:#validacion caja + pared
                                return grilla
                            
                            elif hay_caja(grilla, j-1, i) == True and hay_objetivo(grilla, j-2, i) == True: #caja + objetivo
                                caja_aux = "*"
                                nuevaGrilla[i][j-2] = caja_aux #Movimiento de la caja
                                nuevaGrilla[i][j-1] = " "

                            elif hay_jugador(grilla, j, i) == True and hay_objetivo(grilla, j-1, i) == True and hay_caja(grilla, j-1, i) == True and hay_objetivo(grilla, j-2, i):
                                nuevaGrilla[i][j] = " "
                                nuevaGrilla[i][j-1] = "+"
                                nuevaGrilla[i][j-2] = "*"

                            elif hay_objetivo(grilla, j, i) == True and hay_jugador(grilla, j, i) == True:#salir del objetivo
                                nuevaGrilla[i][j-1] = "@"
                                nuevaGrilla[i][j] = "."

                            elif hay_objetivo(grilla, j-1, i) == True:#entrar al objetivo
                                nuevaGrilla[i][j-1] = "+"
                                nuevaGrilla[i][j] = " "

                            elif hay_objetivo(grilla, j-1, i) == True and hay_caja(grilla, j-1, i) == True: #caja + objetivo al lado
                                nuevaGrilla[i][j-2] = "$" #Movimiento de la caja
                                nuevaGrilla[i][j] = " "
                                nuevaGrilla[i][j-1] = "+" #Movimiento del jugador
                                retorno = 1 
                                break

                            elif(hay_caja(grilla, j-1, i) == True) and (hay_pared(grilla, j-2, i) == False):#empujar caja
                                caja_aux = nuevaGrilla[i][j-2]
                                nuevaGrilla[i][j-2] = grilla[i][j-1] #Movimiento de la caja
                                nuevaGrilla[i][j-1] = caja_aux

                                grilla_aux = nuevaGrilla[i][j-1]
                                nuevaGrilla[i][j-1] = nuevaGrilla[i][j] #Movimiento del jugador
                                nuevaGrilla[i][j] = grilla_aux
                                retorno = 1 
                                break 

                            else:
                                grilla_aux = nuevaGrilla[i][j-1]
                                nuevaGrilla[i][j-1] = nuevaGrilla[i][j] #Movimiento del jugador
                                nuevaGrilla[i][j] = grilla_aux
                                retorno = 1 
                                break
        else:
            if(direccion == (1, 0)):
                for i in range(len(grilla)):
                    for j in range(len(grilla[i])):
                        if(hay_jugador(grilla, j, i) == True and hay_pared(grilla, j+1, i) == False):
                            if (hay_caja(grilla, j+1, i) == True) and (hay_caja(grilla, j+2, i) == True):
                                return grilla

                            elif hay_jugador(grilla, j, i) == True and hay_objetivo(grilla, j+1, i) == True and hay_caja(grilla, j+1, i) == True and hay_objetivo(grilla, j+2, i):
                                nuevaGrilla[i][j] = " "
                                nuevaGrilla[i][j+1] = "+"
                                nuevaGrilla[i][j+2] = "*"

                            elif (hay_caja(grilla, j+1, i) == True) and hay_pared(grilla, j+2, i) == True:#validacion caja + pared
                                return grilla 

                            elif hay_caja(grilla, j+1, i) == True and hay_objetivo(grilla, j+2, i) == True: #caja + objetivo
                                caja_aux = "*"
                                nuevaGrilla[i][j+2] = caja_aux #Movimiento de la caja
                                nuevaGrilla[i][j+1] = " "

                                grilla_aux = nuevaGrilla[i][j+1]
                                nuevaGrilla[i][j+1] = nuevaGrilla[i][j] #Movimiento del jugador
                                nuevaGrilla[i][j] = grilla_aux
                                retorno = 1 
                                break

                            elif hay_objetivo(grilla, j+1, i) == True and hay_caja(grilla, j+1, i) == True: #caja + objetivo al lado
                                nuevaGrilla[i][j+2] = "$" #Movimiento de la caja
                                nuevaGrilla[i][j] = " "
                                nuevaGrilla[i][j+1] = "+" #Movimiento del jugador
                                retorno = 1 
                                break

                            elif(hay_caja(grilla, j+1, i) == True) and (hay_pared(grilla, j+2, i) == False):
                                caja_aux = nuevaGrilla[i][j+2]
                                nuevaGrilla[i][j+2] = grilla[i][j+1] #Movimiento de la caja
                                nuevaGrilla[i][j+1] = caja_aux

                                grilla_aux = nuevaGrilla[i][j+1]
                                nuevaGrilla[i][j+1] = nuevaGrilla[i][j] #Movimiento del jugador
                                nuevaGrilla[i][j] = grilla_aux
                                retorno = 1 
                                break     

                            else:
                                grilla_aux = nuevaGrilla[i][j+1]
                                nuevaGrilla[i][j+1] = nuevaGrilla[i][j] #Movimiento del jugador
                                nuevaGrilla[i][j] = grilla_aux
                                retorno = 1 
                                break
            else:
                if(direccion == (0, -1)):
                    for i in range(len(grilla)):
                        for j in range(len(grilla[i])):
                            if(hay_jugador(grilla, j, i) == True and hay_pared(grilla, j, i-1) == False):
                                if (hay_caja(grilla, j, i-1) == True) and (hay_caja(grilla, j, i-2) == True):
                                    return grilla

                                elif (hay_pared(grilla, j, i-1) == True):
                                    return grilla 

                                elif(hay_caja(grilla, j, i-1) == True) and (hay_pared(grilla, j, i-2) == False):
                                    caja_aux = nuevaGrilla[i-2][j]
                                    nuevaGrilla[i-2][j] = grilla[i][j+1] #Movimiento de la caja
                                    nuevaGrilla[i-1][j] = caja_aux

                                    grilla_aux = nuevaGrilla[i-1][j]
                                    nuevaGrilla[i-1][j] = nuevaGrilla[i][j] #Movimiento del jugador
                                    nuevaGrilla[i][j] = grilla_aux
                                    retorno = 1 
                                    break     

                                else:
                                    grilla_aux = nuevaGrilla[i-1][j]
                                    nuevaGrilla[i-1][j] = nuevaGrilla[i][j] #Movimiento del jugador
                                    nuevaGrilla[i][j] = grilla_aux
                                    retorno = 1 
                                    break  
                else:
                    for i in range(len(grilla)):
                        for j in range(len(grilla[i])):
                            if(hay_jugador(grilla, j, i) == True and hay_pared(grilla, j, i+1) == False):
                                if (hay_caja(grilla, j, i+1) == True) and (hay_caja(grilla, j, i+2) == True):
                                    return grilla

                                elif (hay_pared(grilla, j, i+1) == True):
                                    return grilla 

                                elif(hay_caja(grilla, j, i+1) == True) and (hay_pared(grilla, j, i+2) == False):
                                    caja_aux = nuevaGrilla[i+2][j]
                                    nuevaGrilla[i+2][j] = grilla[i+1][j] #Movimiento de la caja
                                    nuevaGrilla[i+1][j] = caja_aux

                                    grilla_aux = nuevaGrilla[i+1][j]
                                    nuevaGrilla[i+1][j] = nuevaGrilla[i][j] #Movimiento del jugador
                                    nuevaGrilla[i][j] = grilla_aux
                                    retorno = 1 
                                    break     

                                else:
                                    grilla_aux = nuevaGrilla[i+1][j]
                                    nuevaGrilla[i+1][j] = nuevaGrilla[i][j] #Movimiento del jugador
                                    nuevaGrilla[i][j] = grilla_aux
                                    retorno = 1 
                                    break  
  
    for i in range(len(nuevaGrilla)):
        nuevaGrilla = [''.join(i) for i in nuevaGrilla]
        print(nuevaGrilla[i])
    if(retorno == 1):    
        return nuevaGrilla
    else:
        return grilla
desc1 = [
        '########',
        '#    .@#',
        '#      #',
        '########',
    ]
desc2 = [
        '########',
        '#    + #',
        '#      #',
        '########',
    ]
mover(crear_grilla(desc1),(-1, 0))
print(hay_jugador(desc2, 5, 1))