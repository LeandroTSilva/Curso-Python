'''
    Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
No exercício original é usado o pacote pygame, porém não consegui instalar nem fazer rodar.

    Para fazer este exercício optei por usar uma solução alternativa usando a bibliteca webbrowser
como estou usando uma Distro Linux (Pop Os) ao executar o programa ele abre uma janela pedindo para escolher um programa
para reproduzir o audio no meu caso o VLC.

    Não testei em outros sistemas, mas acredito que no Windows/Mac Os dever abrir uma aba no navegador que reproduz o arquivo


    Segue link da documentação:
https://docs.python.org/3/library/webbrowser.html

'''


from webbrowser import open
open('jazz.mp3')

