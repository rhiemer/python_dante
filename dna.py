# -*- coding: utf-8 -*-

import argparse
import random
from enum import Enum

class Letra(Enum):
   A = {"letra":"A","inversa":"C"}
   C = {"letra":"C","inversa":"A"}
   G = {"letra":"G","inversa":"T"}
   T = {"letra":"T","inversa":"G"}


class DNA(object):
  def __init__(self,comprimento): 
    super(DNA, self).__init__()    
    self.comprimento      = comprimento
    self.cadeia           = self.random()
    self.cadeiaInvertida  = self.inverter()
    
  def random(self):
    return ''.join(random.choices(list(map(lambda it:it.value["letra"],Letra)),k=self.comprimento))
  def inverter(self):
    return ''.join(list(map(lambda it:Letra[it].value["inversa"],self.cadeia)))
  
class SerVivo(object):
  def __init__(self,dna): 
    super(SerVivo, self).__init__()
    self.dna = dna   

class Doenca(object):
  def __init__(self,dna,serVivo): 
    super(Doenca, self).__init__()
    self.dna = dna 
    self.serVivo = serVivo
    self.ocorrenciasSerVivo = self.countarOcorrenciasSerVivo()
    self.ocorrenciasSerVivoInvertida = self.countarOcorrenciasSerVivoInvertida()
  def countarOcorrenciasSerVivo(self):
    return self.serVivo.dna.cadeia.count(self.dna.cadeia)
  def countarOcorrenciasSerVivoInvertida(self):
    return self.serVivo.dna.cadeiaInvertida.count(self.dna.cadeia)       

if (__name__ == "__main__"):  
  comprimentoDNASerVivo = int(input("Comprimento do DNA do ser vivo:"))
  dnaSerVivo = DNA(comprimentoDNASerVivo)
  print ("DNA do ser vivo gerado aleatoriamente: {0}".format(dnaSerVivo.cadeia))
  comprimentoDNADoenca = int(input("Comprimento do DNA da doença:"))
  dnaDoenca = DNA(comprimentoDNADoenca)
  print ("DNA da doença gerada aleatoriamente: {0}".format(dnaDoenca.cadeia))
  serVivo = SerVivo(dnaSerVivo)
  doenca = Doenca(dnaDoenca,serVivo)
  print ("Contagem das ocorrências direta da doença no ser vivo: {0}".format(doenca.ocorrenciasSerVivo))
  print ("DNA do ser vivo, complementar invertido: {0}".format(dnaSerVivo.cadeiaInvertida))
  print ("Contagem das ocorrências da doença no DNA complementar invertido: {0}".format(doenca.ocorrenciasSerVivoInvertida))


      



     
     
     



  
    
  


    