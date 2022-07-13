import sys 
import os

try:
    arquivo= open("bla.txt", "r")
    y=0
    while True:
        x= arquivo.read(1)
        y+=1 
        tamanho = os.path.getsize("bla.txt")
        if y > tamanho:    
            break
        else:
         y > tamanho-10
    print(x)
    arquivo.close()
except FileNotFoundError:
    print("ERRO ESSE ARQUIVO NÃO EXISTE")