# -*- coding: utf-8 -*-

import argparse
import random

class MatrizColuna(object):
  def __init__(self,qtdColunas): 
    assert qtdColunas > 0

    super(MatrizColuna, self).__init__()    
    self.qtdColunas       = qtdColunas
    self.matriz           = self.random()    
    self.matrizStr        = " ".join(list(map(lambda it:str(it),self.matriz)))
  def random(self):
    return random.choices(range(0,9),k=self.qtdColunas) 
  def printar(self):
    print (self.matrizStr)  

class Matriz(object):
   def __init__(self,qtdColunas,qtdLinhas): 
    assert qtdColunas > 0
    assert qtdLinhas > 0

    super(Matriz, self).__init__()    
    self.qtdColunas       = qtdColunas
    self.qtdLinhas        = qtdLinhas
    self.linhas           = self.gerarLinhas()
    self.matrizStr        = self.gerarStringLinhas()
   def gerarLinhas(self):
    return list(map(lambda it:MatrizColuna(self.qtdColunas),range(0,self.qtdLinhas)))
   def gerarStringLinhas(self):
    return "\n".join(list(map(lambda it:it.matrizStr,self.linhas)))  
   def printar(self):
    print (self.matrizStr)

class ListaDiagonal(object):
  def __init__(self,matriz,bltr=True):
    super(ListaDiagonal, self).__init__()
    self.matriz   = matriz
    self.bltr     = bltr 
    self.lista    = self.gerarListaMatriz()
  def gerarListaMatriz(self):
    grid = list(map(lambda it:it.matriz,self.matriz.linhas))
    dim = len(grid)
    dim2 = len(grid[0])      
    if (dim != dim2):        
      if (dim > dim2):
        self.adicionarZeros(grid,abs(dim - dim2))                            
      else:
        _linhasZero = self.linhasZero(abs(dim - dim2),dim2)
        grid.extend(_linhasZero)      
    return grid  
  def linhaZero(self,colunas):
    return list(map(lambda it:0,range(0,colunas)))    
  def linhasZero(self,linhas,colunas):     
    return list(map(lambda it:self.linhaZero(colunas),range(0,linhas)))
  def adicionarZeros(self,lista,colunas):
    for it in lista:
      it.extend(self.linhaZero(colunas))
 
class Diagonal(object):
   def __init__(self,matriz,bltr=True):
      super(Diagonal, self).__init__()
      self.matriz   = matriz
      self.bltr     = bltr 
      self.diagonal = self.gerarDiagonal()
      self.diagonalStr = self.gerarStringDiagonal() 
   def gerarDiagonal(self):
      grid = ListaDiagonal(self.matriz,self.bltr).lista
      dim = len(grid)
      return_grid = [[] for total in range(2 * len(grid) - 1)]
      for row in range(len(grid)):
        for col in range(len(grid[row])):
          if self.bltr:
            return_grid[row + col].append(grid[col][row])
          else:
            return_grid[col - row + (dim - 1)].append(grid[row][col])
      return return_grid
   def gerarDiagonais(self):
     self.diagonals.append(self.gerarDiagonal(False))            
   def gerarStringDiagonalLinha(self,linha):
      return " ".join(list(map(lambda it:str(it),linha)))    
   def gerarStringDiagonal(self):
      return "\n".join(list(map(lambda it:self.gerarStringDiagonalLinha(it),self.diagonal)))   
   def printar(self):
      print (self.diagonalStr)

class Diagonais(object):
   def __init__(self,matriz):
      super(Diagonais, self).__init__()
      self.matriz   = matriz
      self.diagonais = []
      self.diagonais.append(Diagonal(matriz,True))
      self.diagonais.append(Diagonal(matriz,False))
      self.diagonaisStr = self.gerarStringDiagonal()
   def gerarStringDiagonal(self):
      return "\n".join(list(map(lambda it:it.diagonalStr,self.diagonais)))
   def printar(self):
      print (self.diagonaisStr)       
          
if (__name__ == "__main__"):  
  linhas = int(input("Digite a quantidade de linhas:"))
  colunas = int(input("Digite a quantidade de colunas:")) 
  matriz = Matriz(colunas,linhas)
  print ("\nMatriz Gerada Aleatoriamente:\n")
  matriz.printar()
  diagonais = Diagonais(matriz)  
  print ("\nListagem das Diagonais:\n")  
  diagonais.printar()
  


      



     
     
     



  
    
  


    