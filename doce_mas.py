# -*- coding: utf-8 -*-
## sirve para lanzar dado


#def __init__(self):
#    super(doce_mas, self).__init__()

def lanzar_dado():
    import random
    cara=random.randrange(1,7)
    return cara

#inserta el valor en su lugar
def insertar_numero(valor,*lista):
    if valor>0:
        v=valor
        l=[]
        #print(l)
        posicion=v-1
        for x in lista:
            #l.remove(v)
            l.append(x)
        if (v in l)==False:
            l.remove(0)
            l.insert(posicion,v)
        #print l
    else:
        l=[0,0,0,0,0,0,0,0,0,0,0,0]
    return l


##verifica si hay un 0 en la lista
def verificar_0(*lista):
    l=[]
    for x in lista:
        l.append(x)
    if (0 in l)==True:
        #print "hay 0"
        return True
    else:
        #print "no hay 0"
        return False


#def main():
    #w=insertar_numero
    ###q=verificar_0
    ###l=[1,2,3,4,5,6,7,8,9,10,11,12]
    #l=[0,0,0,0,0,0,0,0,0,0,0,0]
    ##print w(2,*l)
    #l=w(2,*l)
    #print l
    ##l=w
    ##print w



#main()

#