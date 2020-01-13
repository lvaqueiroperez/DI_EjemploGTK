import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

#IMPORTAMOS MÓDULO "OS"
#OJO!! En python, hasta que no usemos lo que hemos importado, aparecerá en gris
import os
from os import path

#EJERCICIO:HACER UN TREE STORE CON LOS ARCHIVOS DE CUALQUIER DIRECTORIO, USANDO EL MÓDULO "OS" Y SUS FUNCIONES
#"is file", "listdir"...
class Fiestra(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo TreeStore")

        #PRUEBA
        print(os.listdir("/home/dam2/Documentos/"))




if __name__ == "__main__":
    Fiestra()
    Gtk.main()
