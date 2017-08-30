# -*- coding: utf-8 -*-

import argparse


#calcula a media da lista como parametro
class MediaLista(object):   
   def __init__(self,lista): 
    super(MediaLista, self).__init__()   
    self.lista = lista
    self.media = sum(c for c in self.lista)/len(self.lista)

#calculos com lista como parametro
class CalculosMediaLista(object):   
   def criarMedias(self):     
     _lista = []
     for indice,valor in enumerate(self.lista):
       _lista.append(valor)
       if (len(_lista) == self.dias or indice == len(self.lista) - 1):
         self.medias.append(MediaLista(_lista)) 
         del _lista[0]
   def calculos(self): 
      self.menorMedia = min(c.media for c in self.medias)
      self.maiorMedia = max(c.media for c in self.medias)
   def __init__(self,dias,lista):  
     super(CalculosMediaLista, self).__init__()  
     self.lista = lista
     self.dias = dias
     self.medias = []
     self.criarMedias()
     self.calculos()    
   def printMenorMaiorMedia(self):
     print ("{0} {1}".format(round(self.menorMedia,2),round(self.maiorMedia,2)))   
     
     
#informações da cidade
class Cidade(object):     
  def __init__(self,nome,qtdDiasMedicoesChuva,listaMedicoesChuva):
    super(Cidade, self).__init__()
    self.nome = nome
    self.qtdDiasMedicoesChuva = qtdDiasMedicoesChuva
    self.listaMedicoesChuva = listaMedicoesChuva
    self.calculosMediaListaChuva = CalculosMediaLista(qtdDiasMedicoesChuva,listaMedicoesChuva)
  def printarCidade(self):
    print ("Cidade {0}".format(self.nome))         
  def printarMenorMaiorMediaChuva(self):
    self.calculosMediaListaChuva.printMenorMaiorMedia()
   
def printarMenorMaiorMediaChuvaCidades(sequencias):
    for indice,itSequencia in enumerate(sequencias):           
      arraySequencias = itSequencia.split(":")
      if (len(arraySequencias) == 2):
        qtdDiasMedicoesChuva = int(arraySequencias[0].strip())
        listaMedicoesChuva = list(map(lambda it:float(it.strip()),arraySequencias[1].split(",")))
        cidade = Cidade(indice + 1,qtdDiasMedicoesChuva,listaMedicoesChuva)
        cidade.printarCidade()
        cidade.printarMenorMaiorMediaChuva()
        print ("")     
      else:  
        raise NotImplementedError('Formato da cidade-> qtdDiasMedicoesChuva:listaMedicoesChuva(separado por virgula).') 
            

if (__name__ == "__main__"):
  # Recuperando parametros da execução num prompt de comando ou shell
  # python indice_chuva.py --sequencias 3:100,120,0,0,247,30 1:10 2:50,50,0,0
  parser = argparse.ArgumentParser()  
  parser.add_argument("--sequencias", help="Sequencias de medições das cidades ", nargs='+')  
  args = parser.parse_args()  
  printarMenorMaiorMediaChuvaCidades(args.sequencias)

      



     
     
     



  
    
  


    