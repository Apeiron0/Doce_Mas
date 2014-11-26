# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import*
pygame.init()
import doce_mas


altura=800
ancho=600

def main():
    #inicializar componentes
    pygame.init()
    #creacion de ventana
    screen=pygame.display.set_mode((altura,ancho))
    pygame.display.set_caption("12 mas")
    #creacion de jugadores
    j1=[0,0,0,0,0,0,0,0,0,0,0,0]
    j2=[0,0,0,0,0,0,0,0,0,0,0,0]
    t2=doce_mas.verificar_0
    r=doce_mas.insertar_numero
    valor=0
    tj1="turno jugador #1"
    tj2="turno jugador #2"
    gana_j1="El ganador es el jugador #1"
    gana_j2="El ganador es el jugador #2"
    ##img de teclas
    teclas=pygame.image.load("teclas/teclas.png").convert()
    #cargar fondo
    fondo=pygame.image.load("fondo.png").convert()
    #cargar dado
    d1=pygame.image.load("dado/1.png").convert()
    d2=pygame.image.load("dado/6.png").convert()
    #label jugadores
    lj2=pygame.image.load("jugador/j1.png").convert()
    lj1=pygame.image.load("jugador/j2.png").convert()
    t=lj1
    #posicion de imagenes
    screen.blit(fondo,(0,0))
    #definicion del turno
    turno=1
    #bucle principal/infinito
    while True:
        screen.blit(d1,(350,150))
        screen.blit(d2,(350,250))
        screen.blit(teclas,(500,200))
        #keys=pygame.key.get_pressed()
        for evento in pygame.event.get():
            j1.sort
            j2.sort
            if evento.type==QUIT:
                sys.exit(0)
            elif evento.type==KEYUP:
                if evento.key==K_SPACE:
                    #screen.blit(t,(100,250))
                    dado1=doce_mas.lanzar_dado()
                    dado2=doce_mas.lanzar_dado()
                    #print(dado1,dado2)
                    if dado1==1:
                        d1=pygame.image.load("dado/1.png").convert()
                    if dado1==2:
                        d1=pygame.image.load("dado/2.png").convert()
                    if dado1==3:
                        d1=pygame.image.load("dado/3.png").convert()
                    if dado1==4:
                        d1=pygame.image.load("dado/4.png").convert()
                    if dado1==5:
                        d1=pygame.image.load("dado/5.png").convert()
                    if dado1==6:
                        d1=pygame.image.load("dado/6.png").convert()
                        d1=pygame.image.load("dado/6.png").convert()
                    if dado2==1:
                        d2=pygame.image.load("dado/1.png").convert()
                    if dado2==2:
                        d2=pygame.image.load("dado/2.png").convert()
                    if dado2==3:
                        d2=pygame.image.load("dado/3.png").convert()
                    if dado2==4:
                        d2=pygame.image.load("dado/4.png").convert()
                    if dado2==5:
                        d2=pygame.image.load("dado/5.png").convert()
                    if dado2==6:
                        d2=pygame.image.load("dado/6.png").convert()
                    turno=turno+1
                if evento.key==K_1:
                    valor=dado1
                    #turno=turno+1
                    if turno%2==0:
                        if (t2(*j1))==True:
                            t=lj1
                            j1=r(valor,*j1)
                            print "turno jugador1"
                            print j1
                            #print j2
                            #print "turno",turno
                        else:
                            # "ganador=jugador1"
                            l30=pygame.font.SysFont("Arial",30)
                            iTP=l30.render(gana_j1,True,(50,50,50),(0,0,0))
                            rTP=iTP.get_rect()
                            rTP.centerx=150
                            rTP.centery=300
                            screen.blit(iTP,rTP)
                    else:
                        if(t2(*j2))==True:
                            t=lj2
                            j2=r(valor,*j2)
                            print "turno jugador2"
                            print j2
                        else:
                            #print "ganador=jugador2"
                            l30=pygame.font.SysFont("Arial",30)
                            iTP=l30.render(gana_j2,True,(50,50,50),(0,0,0))
                            rTP=iTP.get_rect()
                            rTP.centerx=150
                            rTP.centery=300
                            screen.blit(iTP,rTP)
                if evento.key==K_2:
                    valor=dado2
                    #turno=turno+1
                    if turno%2==0:
                        if (t2(*j1))==True:
                            t=lj1
                            j1=r(valor,*j1)
                            print "turno jugador1"
                            print j1
                            #print j2
                            #print "turno",turno
                        else:
                            #print "ganador=jugador1"
                            l30=pygame.font.SysFont("Arial",30)
                            iTP=l30.render(gana_j1,True,(50,50,50),(0,0,0))
                            rTP=iTP.get_rect()
                            rTP.centerx=150
                            rTP.centery=300
                            screen.blit(iTP,rTP)
                    else:
                        if(t2(*j2))==True:
                            t=lj2
                            j2=r(valor,*j2)
                            print "turno jugador2"
                            print j2
                        else:
                            #print "ganador=jugador2"
                            l30=pygame.font.SysFont("Arial",30)
                            iTP=l30.render(gana_j2,True,(50,50,50),(0,0,0))
                            rTP=iTP.get_rect()
                            rTP.centerx=150
                            rTP.centery=300
                            screen.blit(iTP,rTP)
                if evento.key==K_3:
                    valor=dado1+dado2
                    #turno=turno+1
                    if turno%2==0:
                        if (t2(*j1))==True:
                            t=lj1
                            j1=r(valor,*j1)
                            print "turno jugador1"
                            print j1
                            #print j2
                            #print "turno",turno
                        else:
                            #print "ganador=jugador1"
                            l30=pygame.font.SysFont("Arial",30)
                            iTP=l30.render(gana_j1,True,(50,50,50),(0,0,0))
                            rTP=iTP.get_rect()
                            rTP.centerx=150
                            rTP.centery=300
                            screen.blit(iTP,rTP)
                    else:
                        if(t2(*j2))==True:
                            t=lj2
                            j2=r(valor,*j2)
                            print "turno jugador2"
                            print j2
                        else:
                            #print "ganador=jugador2"
                            l30=pygame.font.SysFont("Arial",30)
                            iTP=l30.render(gana_j2,True,(50,50,50),(0,0,0))
                            rTP=iTP.get_rect()
                            rTP.centerx=150
                            rTP.centery=300
                            screen.blit(iTP,rTP)
                if turno%2==0:
                    #t=lj2
                    letra30=pygame.font.SysFont("Arial",20)
                    imagenTextoPresent=letra30.render(tj1,True,(50,50,50),(0,0,0))
                    rectanguloTextoPresent=imagenTextoPresent.get_rect()
                    rectanguloTextoPresent.centerx=250
                    rectanguloTextoPresent.centery=250
                else:
                    letra30=pygame.font.SysFont("Arial",20)
                    imagenTextoPresent=letra30.render(tj2,True,(50,50,50),(0,0,0))
                    rectanguloTextoPresent=imagenTextoPresent.get_rect()
                    rectanguloTextoPresent.centerx=250
                    rectanguloTextoPresent.centery=250
                    #t=lj1
                screen.blit(imagenTextoPresent,rectanguloTextoPresent)
                #screen.blit(t,(100,250))
                #print turno
        p1x=50
        p2x=50
        for er in j1:
                qw=str(er)
                letra=pygame.font.SysFont("Arial",30)
                img_j1=letra.render(qw,True,(50,50,50),(0,0,0))
                r_j1=img_j1.get_rect()
                r_j1.centerx=p1x
                p1x=p1x+50
                r_j1.centery=50
                screen.blit(img_j1,r_j1)
        for er in j2:
                qw=str(er)
                letra=pygame.font.SysFont("Arial",30)
                img_j1=letra.render(qw,True,(50,50,50),(0,0,0))
                r_j1=img_j1.get_rect()
                r_j1.centerx=p2x
                p2x=p2x+50
                r_j1.centery=500
                screen.blit(img_j1,r_j1)
        pygame.display.flip()
    #return 0

if __name__=="__main__":
    main()