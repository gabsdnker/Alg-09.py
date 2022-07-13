#Concatenar múltiplos arquivos.

#terminal: cat
#Escreva um programa Python que apresente o mesmo comportamento.
#O programa deve exibir uma mensagem de erro caso algum arquivo não puder ser lido, e então passa para a leitura do próximo arquivo. 
#O programa também deve exibir mensagem de erro caso não tenha sido passado nenhum argumento para o programa em linha de comando.

import sys 

if __name__=='__main__':

    try:
        
    arquivo.close()
    except FileNotFoundError:
       print("ERRO ESSE ARQUIVO NÃO EXITE")
