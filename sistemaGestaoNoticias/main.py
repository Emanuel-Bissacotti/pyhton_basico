from menu import Menu
from file import File

list = []

list = File.get_noticias()

Menu.menu(list)