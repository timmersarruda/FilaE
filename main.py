# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:59:34 2022

@author: PC
"""

import FilaE

fila = FilaE.FilaE()


if not (fila.estaCheia()):
    fila.inserir('a')
if (fila.estaCheia()) != True:
    fila.inserir('b')
if (fila.estaCheia()) != True:
    fila.inserir('c')
if (fila.estaCheia()) != True:
    fila.inserir('d')
if (fila.estaCheia()) != True:
    fila.inserir('e')

print("Apos a insercao dos elementos a b c d e na fila")
fila.imprimir()

if not fila.estaVazia():
    fila.remover()

print("Apos a remocao de um elemento da fila - b c d e")
fila.imprimir()

fila.inserir('f')
print("Apos a insercao do elemento f na fila")
fila.imprimir()

if not fila.estaVazia():
    fila.remover()

print("Apos a remocao de um elemento da fila - c d e f")
fila.imprimir()

print("Primeiro da fila é o c:", fila.getPrim())
