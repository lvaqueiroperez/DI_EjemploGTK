import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# Creación de Grid usando solo código (ver dibujo en libreta)
#OJO!!! ESTA GRID SE HA CREADO COMO UNA VENTANA CON UN COMPONENTE GRID, PERO PODRÍAMOS HABER CREADO UNA GRID COMO UN COMPONENTE
#HEREDANDO DE "GTk.Grid"
class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="EJemplo con Gtk.Grid")

        grid = Gtk.Grid()

        boton1 = Gtk.Button(label="Boton1")
        boton2 = Gtk.Button(label="Boton2")
        boton3 = Gtk.Button(label="Boton3")
        boton4 = Gtk.Button(label="Boton4")
        boton5 = Gtk.Button(label="Boton5")
        boton6 = Gtk.Button(label="Boton6")
        boton7 = Gtk.Button(label="Boton7")

        # El primer botón solo hace falta añadirlo para que aparezca en 0,0 (esquina superior izquierda), los demás se añadirán tomándolo como referencia
        grid.add(boton1)

        # Tras indicar el parámetro, podemos indicar su posición COLUMNA-FILA,y su ancho y alto

        grid.attach(boton2, 1, 0, 2, 1)

        # Podemos añadir y situar botones con "next_to" de manera más fácil
        grid.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach(boton4, 1, 1, 2, 1)

        #Si vemos que un elemento no se añade como esperamos en la interfaz, probar a ponerlo dentro de otros, como
        #dentro de una caja o de un grid !!!!
        # Creamos una caja para los botones 5,6,7
        # Por defecto, las cajas tienen orientación horizontal
        caja = Gtk.Box()

        caja.pack_start(boton5, True, True, 0)
        caja.pack_start(boton6, True, True, 0)
        caja.pack_start(boton7, True, True, 0)

        grid.attach_next_to(caja, boton4, Gtk.PositionType.BOTTOM, 1, 1)

        # Una vez tengamos todos listo, añadimos la grid
        self.add(grid)

        # Añadimos la función de salir de la ventana
        self.connect("destroy", Gtk.main_quit)

        # Y las mostramos
        self.show_all()


if __name__ == "__main__":
    Ventana()
    Gtk.main()
