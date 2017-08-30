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
   def __init__(self,apostador,valor,par_ou_impar):
    #validações dos valores da aposta
    super(Aposta, self).__init__()
    if (valor < 0):  
      raise NotImplementedError('Valor não pode ser menor que 0.')  
    if (valor > 5):  
      raise NotImplementedError('Valor não pode ser maior que 5.')    
    self.apostador = apostador;
    self.valor = valor;
    self.par_ou_impar = par_ou_impar

class Partida(object):
  def carregarDadosPartida(self):    
    self.__total__ = sum(c.valor for c in self.__apostas__)
    self.__apostasVencedoras__ = list(filter(lambda aposta:aposta.par_ou_impar.verificar(self.__total__),self.__apostas__))     
  def __init__(self,nome,listaApostas):
    if (len(listaApostas) < 2):
      raise NotImplementedError('É necessário mais de uma aposta por sequência.')
    #veririfica se na partida alguem apostou em par ou impar
    #par ou impar sem ter pelo menos um dos dois não tem sentido
    listaPar = list(filter(lambda aposta:aposta.par_ou_impar == Par_Ou_Impar.par,listaApostas))
    listaImpar = list(filter(lambda aposta:aposta.par_ou_impar == Par_Ou_Impar.impar,listaApostas))
    if (len(listaPar) == 0 and len(listaImpar)):
     raise NotImplementedError('É necessário na partida que tenha pelo menos uma aposta no par ou no impar.')     
     
    super(Partida, self).__init__()
    self.__nome__    = nome
    self.__apostas__ = listaApostas       
    self.carregarDadosPartida()     
  def printarTitulo(self):    
    print("Sequência {0}".format(self.__nome__))
  def printarApostasVencedoras(self):
    print("\n".join(map(lambda x:x.apostador,self.__apostasVencedoras__))) 


#converte string para partida -> apostador:valor:par_ou_impar  
def convertAposta(strPartida):    
  arr=strPartida.split(":")       
  if (len(arr) == 3):
    apostador = arr[0];
    valor = int(arr[1]);
    par_ou_impar = Par_Ou_Impar[arr[2]]
    if (not par_ou_impar):
     raise NotImplementedError('Informe no indicde 3 se o valor é par ou impar.')
    return Aposta(apostador,valor,par_ou_impar)
  else:
    raise NotImplementedError('Informa a string dividia com ":" em tres partes:apostador,valor e par_ou_impar(par ou impar).')

def convertListaApostas(strListaApostas):
  return list(map(lambda it:convertAposta(it),strListaApostas.split(",")))   

def convertPartida(nome,strListaApostas):
  return Partida(nome,convertListaApostas(strListaApostas))

def convertListaPartidas(listaSequencia):
  return list(map(lambda (i,it):convertPartida(i + 1,it),enumerate(listaSequencia)))
   
def printarPartidas(partidas):
 for partida in partidas:
   partida.printarTitulo()           
   partida.printarApostasVencedoras() 
   print ("")

if (__name__ == "__main__"):
  # Recuperando parametros da execução num prompt de comando ou shell
  # python par_ou_impar.py --partidas joao:5:impar,maria:4:impar joao:5:par,maria:3:impar
  parser = argparse.ArgumentParser()  
  parser.add_argument("--partidas", help="Sequencias de partidas -> array separado por virgula no formato apostador:valor:(par ou impar)", nargs='+')  
  args = parser.parse_args()  
  partidas = convertListaPartidas(args.partidas)
  printarPartidas(partidas)

      



     
     
     



  
    
  


    