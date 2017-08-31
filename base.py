# -*- coding: utf-8 -*-
import argparse

class CalculoBase(object):
  def __init__(self,valor,base):
    assert base > 0
    assert valor > 0

    super(CalculoBase, self).__init__()
    self.valor=valor
    self.base=base
    self.calculo = self.calcular()        
    self.calculoStr = "Base {0}: {1}".format(str(self.base),self.calculo) 
  def calcular(self):
    decimal = int(self.valor)
    base = self.base    
    list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    other_base = ""
    while decimal != 0 :
        other_base = list[int(decimal % base)] + other_base
        decimal    = decimal / base
    return other_base.lstrip("0")        
  def printar(self):
    print(self.calculoStr)

class ListaCalculaBase(object):
  def __init__(self,valor,baseMinima,baseMaxima):
    assert baseMaxima >= baseMinima

    super(ListaCalculaBase, self).__init__()    
    self.valor=valor
    self.baseMinima=baseMinima
    self.baseMaxima=baseMaxima
    self.lista = self.gerarLista()
    self.listaStr = self.gerarListaStr()
  def gerarLista(self):
    return list(map(lambda it:CalculoBase(self.valor,it),range(self.baseMinima,self.baseMaxima)))  
  def gerarListaStr(self):
    return "\n".join(list(map(lambda it:it.calculoStr,self.lista)))
  def printar(self):
    print(self.listaStr)  
          
if (__name__ == "__main__"):
  
  while (True):      
    valor = int(input("Digite um valor inteiro não negativo (negativo para sair):"))
    if (valor < 0):
      print("Sair")
      break     
    listaCalculaBase = ListaCalculaBase(valor,2,17)
    print ("\nResultado das Conversões:\n")
    listaCalculaBase.printar()
    print("")
    
    
 
  


      



     
     
     



  
    
  


    