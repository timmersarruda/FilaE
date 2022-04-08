# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:58:12 2022

@author: Timmers Arruda 
"""

class FilaE():
    def __init__(self):
        self.vetor = [None, None, None, None, None]
        self.quant = 0

    def getQuant(self):
        return self.quant

    def getPrim(self):
        return self.vetor[0]

    def estaCheia(self):
        return self.quant == 5

    def estaVazia(self):
        return self.quant == 0

    def inserir(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def remover(self):
        for i in range(0, self.quant-1):
            self.vetor[i] = self.vetor[i + 1]
        self.quant -= 1

    def imprimir(self):
        for i in range(self.quant):
            print(self.vetor[i], end = ' ')
        print()
