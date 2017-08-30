# -*- coding: utf-8 -*-

import argparse

#lista pixel
class LinhaPixel(object):
  def __init__(self,pixels): 
    super(LinhaPixel, self).__init__()
    self.pixels = pixels
  def __str__(self):
    return " ".join(map(lambda x:str(x),self.pixels))

#calcula a media da lista como parametro
class PixelsAjustados(object):
  def __init__(self,colunas,listas,linhas=None): 
    super(PixelsAjustados, self).__init__()
    self.colunas = colunas  
    self.listas  = listas
    self.linhas  = linhas
    self.imagemOriginalAjustada = []
    self.ajustar()    
  def criarListaUnica(self):
    unicaListaDePixels = set([y for x in self.listas for y in x])    
    return sorted(list(filter(lambda pixel:self.validarPixel(pixel),unicaListaDePixels)),key=int)  
  def validarPixel(self,pixel):
    return (pixel > 0)    
  def criarImagemOriginalAjustada(self,pixels):
    _lista = []    
    for indice,valor in enumerate(pixels):
      _lista.append(valor)
      if (len(_lista) == self.colunas or indice == len(pixels) - 1):
        self.imagemOriginalAjustada.append(LinhaPixel(_lista))
        if (self.linhas and self.linhas > 0 and self.linhas == len(self.imagemOriginalAjustada)):
          return    
        _lista = []  
  def ajustar(self):        
    self.criarImagemOriginalAjustada(self.criarListaUnica())        
  def printarImagemOriginalAjustada(self):           
    print("\n".join(list(map(lambda x:str(x),self.imagemOriginalAjustada))))     

def convertSequenciaPixel(strPixels):
  return list(map(lambda it:int(it.strip()),strPixels.split(",")))

def convertListaSequenciaPixel(listaSequenciaPixels):    
  return list(map(lambda it:convertSequenciaPixel(it),listaSequenciaPixels))

if (__name__ == "__main__"):
  # Recuperando parametros da execução num prompt de comando ou shell
  # python tratamento_imagem.py --colunas 4 --pixels "6,7,8,5" "10,11,12,9" "2,3,4,1" " -3,2" "5,7" "0,-2" --linhas 3
  # python tratamento_imagem.py --colunas 4 --pixels "6,7,8,5,60,4" "10,11,12,9,80" "2,3,4,1" "3,2" "5,7" "0,2" "5,3,50,20,35,14"
  parser = argparse.ArgumentParser()  
  parser.add_argument("--colunas", help="Informa a quantidade máxima de colunas da imagem original ajustada.",type=int)  
  parser.add_argument("--pixels", help="Informa a sequencia de pixels separadas por virgula.",nargs='+')  
  parser.add_argument("--linhas", help="Informa a quantidade máxima de linhas da imagem original ajustada.",nargs="?",type=int,default=None) 
  args = parser.parse_args()  
  pixels = convertListaSequenciaPixel(args.pixels)
  pixelAjustados = PixelsAjustados(args.colunas,pixels,args.linhas)
  pixelAjustados.printarImagemOriginalAjustada()

      



     
     
     



  
    
  


    