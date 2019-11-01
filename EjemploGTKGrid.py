import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="EJemplo con Gtk.Grid")

        grid = Gtk.Grid()
        self.add(grid)

        boton1 = Gtk.Button(label = "Boton1")
        boton2 = Gtk.Button(label="Boton2")
        boton3 = Gtk.Button(label="Boton3")

        grid.add(boton1)
        grid.attach(boton2,1,0,2,1)
        grid.attach_nect_to(boton3,boton1,Gtk.PositionType.BOTTOM,1,2)