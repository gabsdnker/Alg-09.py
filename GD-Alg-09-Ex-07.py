#Frequência de letras.

#Escreva um programa Python que faz a primeira parte deste processo, determinando e exibindo a frequência (percentual) de ocorrência de todas as letras em um arquivo.
#Ignore espaços, números e sinais de pontuação.
#Seu programa não deve diferenciar letras maiúsculas e minúsculas (portento deve tratar A e a como sendo a mesma letra).
#O usuário deve fornecer o nome do arquivo como argumento em linha de comando.

from curses.ascii import isalpha
import numbers


with open("bla.txt", 'r') as fonte:
    while letras:= fonte.readline(1):
        if letras == " " and letras == numbers and letras == isalpha():
            
