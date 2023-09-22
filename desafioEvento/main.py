from menu import *
from arquivo import *

Lista = []
Lista = Arquivo.pegar_arquivo(Lista)

while(True):
    menu(Lista)