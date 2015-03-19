# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:47:59 2015

@author: Alejandro
"""
from random import randint

joPlacar = 0
coPlacar = 0



def computador(jogada):
    if jogada==1:
        return("papel")
    elif jogada==2:
        return("pedra")
    elif jogada==3:
        return("tesoura")
    elif jogada==4:
        return("spock")
    elif jogada==5:
        return("lagarto")


g="voce ganhou"
p="computador ganhou"
x="proxima jogada"
while joPlacar!=3 and coPlacar!=3:
    jog=input("faça sua jogada: ")
    comp=(computador(randint(1,5)))
    print("computador: ",comp)
    if jog==comp:
        print("Empate")
    elif jog == "papel" and comp == "pedra":
        print(g)
        joPlacar = joPlacar +1
        coPlacar = 0
        
    elif jog=="pedra" and comp=="papel":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
        
    elif jog=="papel" and comp=="tesoura":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
        
    elif jog=="esoura" and comp=="papel":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1    
    
    elif jog=="papel" and comp=="lagarto":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
    
    elif jog=="lagarto" and comp=="papel":
        print(g)
        joPlacar = joPlacar +1
        coPlacar = 0
    
    elif jog=="papel" and comp=="spock":
        print(g)
        joPlacar=joPlacar+1
        coPlacar=0        
        
    elif jog=="spock" and comp=="papel":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
        
    elif jog=="pedra" and comp=="tesoura":
        print(g)
        joPlacar = joPlacar +1
        coPlacar = 0
        
    elif jog=="tesoura" and comp=="pedra":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
        
    elif jog=="pedra" and comp=="lagarto":
        print(g)
        joPlacar = joPlacar +1
        coPlacar = 0
        
    elif jog=="lagarto" and comp=="pedra":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
        
    elif jog=="pedra" and comp=="spock":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
        
    elif jog=="spock" and comp=="pedra":
        print(g)
        joPlacar = joPlacar +1
        coPlacar = 0
        
    elif jog=="tesoura" and comp=="lagarto":
        print(g)
        joPlacar = joPlacar +1
        coPlacar = 0
        
    elif jog=="lagarto" and comp=="tesoura":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
        
    elif jog=="tesoura" and comp=="spock":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
        
    elif jog=="spock" and comp=="tesoura": 
        print(g)
        joPlacar = joPlacar +1
        coPlacar = 0
    elif jog=="lagarto" and comp=="spock":
        print(g)
        joPlacar = joPlacar +1
        coPlacar = 0
    elif jog=="spock" and comp=="lagarto":
        print(p)
        joPlacar=0
        coPlacar= coPlacar+1
if joPlacar==3:
    print("parabens!!!")
elif coPlacar==3:
    print("voce perdeu FEIO!!")