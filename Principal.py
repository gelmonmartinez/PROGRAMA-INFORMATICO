import re
#Integrantes:
# Beatriz Adriana
# Ruben Ulises
# Javier Carranza
# Gelmon Martinez 
print("-----------------------------------------------------------------------------------------")
print("Elija una opcion")
print("-----------------------------------------------------------------------------------------")
print (    "1. EJEMPLO1." +"\n"+ 
           "2. EJEMPLO2." + "\n" +
           "3. EJEMPLO3." + "\n" + 
           "4. EJEMPLO4."  + "\n"+
           "5. EJEMPLO5." + "\n" + 
           "6. salir")
print("-----------------------------------------------------------------------------------------")
x=int(input("Opcion: "))

if x > 0 and x < 6:
    #Ejercicio sin regex con listas.
    #Regex = Secuencia de caracteres que conforma un patrón de búsqueda.
    print()
    f = open ("EJEMPLO"+ str(x) +".txt").read() #Abre el ejmplo del ejercicio.
    print(f) #Imprime el ejercicio
    print()

    #variables
    operadores = [")", "/","*","+", "-"]
    temporal = ""
    operaciones = []
    count = -1
    index = 0

    auxExpresion = ""
    expresion = []
    ordenOriginal = []
    #fin variables

    #Almacenamos en un array de expresion, cada valor del string leido del archivo. El delimitador es el espacio
    for i in f:
        if i != " ":
            expresion.append(i)
        if i in operadores and i != "(" and i != ")":
            ordenOriginal.append(i) #se almacena el orden original de los operadores para conocer el orden de operación cuando se resuelven los parentesis
            
    #Se recorre los operadores para construir las operaciones por jerarquia        
    for operador in operadores:
        count = -1
        #se recorre la expreción almacenada en el array
        for item in expresion:
            count +=1
                
            #Si el item es un parentesis que cierra, se buscan el parentesis que abre para localizar la operacion
            if(item == ")"):
                #si se localiza el parentesis que cierra se concatena toda la operacion.  ejemplo t = (a + b)
                if(expresion[count-4] == "("):
                    auxExpresion =  "_t" +str(index)+" = " + " " + expresion[count-4] +" "+ expresion[count-3] + " " + expresion[count-2]  + " " +  expresion[count-1] + " " + item

                    del expresion[count]
                    del expresion[count-1]
                    del expresion[count-2]
                    del expresion[count-3]
                    del expresion[count-4]
                else:
                    #Si no se localiza el parentesis, puede deberse a que exisita una operación dentro de los parentesis. Por lo cual sea concatena la operacion temporal(anterior)
                    #ejemplo tn = (t + b)
                    auxExpresion =  "_t" +str(index)+" = " + " " + expresion[count-3] + " " + operaciones[len(operaciones)-1] +" " + expresion[count-2]  + " " +  expresion[count-1] + " " + item
                    
                    del expresion[count]
                    del expresion[count-1]
                    del expresion[count-2]
                    del expresion[count-3]

                #se imprime todo el resuldato de la valdiacion del if
                print(auxExpresion)
                #se guarda la operacion realizada para utilizar despues
                temporal = "_t" +str(index)
                #se guarda esta operación para determinar X
                operaciones.append(temporal)
                #se incrementa el index de t, ejemplo t1, t2, etc
                index += 1

            elif item == operador: #Si el item de la expresion es igual al item de los operadores. ejemplo + = +
                if(len(expresion) == 1): #si solo existe un valor y es un operador se buscan las ultimas 2 operaciones(t1 y t2) para concatenarlas en una nueva operacion
                    
                    if(ordenOriginal[ordenOriginal.index(item) -1] in auxExpresion): #validación para identificar que operacion va primero. Orden de la expreción original. ejemplo, a * b / (c-d) donde t1 = (c - d) y t2 = a * b,  tiene que ser t2 - t1
                        auxExpresion = "_t" +str(index)+" = " + operaciones[len(operaciones)-1] +" "+ item +" " + operaciones[len(operaciones)-2]
                    else: #caso contrario ejemplo, (a * b) + (c-d) donde t1 = (a * b) y t2 = (c-d), tiene que ser t1 - t2
                        auxExpresion = "_t" +str(index)+" = " + operaciones[len(operaciones)-2] +" "+ item +" " + operaciones[len(operaciones)-1]

                elif expresion.index(item) == 0 : #si el operador esta en la primera posición significa que antes huno una operación. Por lo cual se busca para concatenar (_t + operador + siguiente valor)
                    auxExpresion = "_t" +str(index)+" = " + temporal +" "+ item +" " + expresion[count + 1] 
                    
                    del expresion[count+1]
                    del expresion[count]
                    
                #Si el conteo mas una posición no sobre pasa el tamaño del array, se arma la operación del operador actual. Se ocupa para buscar el siguiente valor. Ejemplo a + b. Ahora count apunta a +, para concer + hay que sumarle a count 1
                #valor anterior + operador+ valor siguiente
                elif count+1 <= len(expresion) -1 : 
                    auxExpresion = "_t" +str(index)+" = " + expresion[count-1]  + " " +  item + " " + expresion[count+1]

                    op1 = expresion[count-1]
                    op2 = expresion[count+1]

                    expresion.remove(item)
                    expresion.remove (op2)
                    expresion.remove(op1)

                #Si el conteo + 1 sobre pasa el tamaño del array de expresion, se arma la operación con el operador actual:  ejemplo: a + t0
                #valor anterior + operador + Operación Anterior
                else: 
                    auxExpresion = "_t" +str(index)+" = " + expresion[count-1] + " " + item + " " + temporal

                #Se imprime todo el resuldato de la valdiacion del else if
                print(auxExpresion)
                temporal = "_t" +str(index)
                operaciones.append(temporal) 
                index += 1
                
    print("  " + "X =" + temporal)
elif x == 6:
    salir = True
else:
    print ("VUELVA A INTENTAR" + "\n" + "Elija una obcion entre 1 al 6")
