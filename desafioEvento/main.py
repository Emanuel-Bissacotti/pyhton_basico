from menu import Menu
from arquivo import *

lista = []
lista = Arquivo.pegar_arquivo(lista)

while(True):
    Menu.menu(lista)