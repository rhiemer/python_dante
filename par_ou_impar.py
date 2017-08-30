# -*- coding: utf-8 -*-

import argparse
from enum import Enum

class Par_Ou_Impar(Enum):
   par = 0
   impar = 1

   def verificar(self,numero):    
    #resto da divisão por 2, verifica se é par ou impar
    return (numero%2 == self.value)

class Aposta(object):   
   def __init__(self,aposta):    
    #formato apostador:valor:par_ou_impar    
    arr=aposta.split(":")       
    if (len(arr) == 3):
      self.apostador = arr[0];
      self.valor = int(arr[1]);
      self.par_ou_impar = Par_Ou_Impar[arr[2]]
      #validações dos valores da aposta
      if (self.valor < 0):  
        raise NotImplementedError('Valor não pode ser menor que 0.')  
      if (self.valor > 5):  
        raise NotImplementedError('Valor não pode ser maior que 5.')    
      if (not self.par_ou_impar):
        raise NotImplementedError('Informe no 3 valor par ou impar.')  
    else:
      raise NotImplementedError('Informa a string dividia com ":" em tres partes:apostador,par_ou_impar(par ou impar) e o valor.')      

class VerificarApostas(object):
  def __init__(self):
    self.__apostas__ = []  
    self.__apostasVencedoras__ = []
    self.__total__ = None 
  def carregarAposta(self):    
    self.__total__ = sum(c.valor for c in self.__apostas__)
    self.__apostasVencedoras__ = list(filter(lambda aposta:aposta.par_ou_impar.verificar(self.__total__),self.__apostas__))     
  def __init__(self,listaApostas):
    super(VerificarApostas, self).__init__()
    self.__apostas__ = list(map(lambda itAposta: Aposta(itAposta), listaApostas))       
    self.carregarAposta()     
  def printarVencedoras(self):
    print("\n".join(map(lambda x:x.apostador,self.__apostasVencedoras__))) 

class SequenciaApostas(object):  
  def __init__(self,indice,listaApostas):
    super(SequenciaApostas, self).__init__()
    if (len(listaApostas) <= 1):
      raise NotImplementedError('É necessário mais de uma aposta por sequência.')   
    self.__indice__ = indice
    self.__verificarApostas__ = VerificarApostas(listaApostas)
  def printar(self):
    print("Sequência {0}".format(self.__indice__))
    self.__verificarApostas__.printarVencedoras() 
   
def printarSequenciasApostas(sequencias):
    for indice,itSequencia in enumerate(sequencias):           
      arraySequencias = itSequencia.split(",")      
      SequenciaApostas(indice + 1,arraySequencias).printar() 
      print ("")     

if (__name__ == "__main__"):
  # Recuperando parametros da execução num prompt de comando ou shell
  # python par_ou_impar.py --sequencias joao:5:impar,maria:4:impar joao:5:par,maria:3:impar
  parser = argparse.ArgumentParser()  
  parser.add_argument("--sequencias", help="Sequencias de apostas ", nargs='+')  
  args = parser.parse_args()  
  printarSequenciasApostas(args.sequencias)

      



     
     
     



  
    
  


    