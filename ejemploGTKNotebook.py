import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#LO MUESTRA MAL?????????
# Cración de Notebook GTK usando solo código Y REUTILIZANDO EL CÓDIGO DE "EjemploGTKGrid" DE ANTES
class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="EJemplo con Gtk Notebook")

        notebook = Gtk.Notebook()
        self.add(notebook)

        pagina1 = Gtk.Box()
        pagina1.set_border_width(10)
        pagina1.add(Gtk.Label("Página por defecto"))

        notebook.append_page(pagina1, Gtk.Label("Título de la solapa"))

        # Creamos un objeto de la Clase reutilizada "Panel"
        pagina2 = Panel()
        notebook.append_page(pagina2, Gtk.Label("Botones"))

        pagina3 = Panel()

        notebook.append_page(pagina3, Gtk.Label("Botones pag 3"))


        # Añadimos la función de salir de la ventana
        self.connect("destroy", Gtk.main_quit)

        # Y las mostramos
        self.show_all()

        # VAMOS A USAR EL CÓDIGO DE "EJEMPLOGTKGRID"

        ####################################################


class Panel(Gtk.Grid):
    def __init__(self):
        # ESTO NO HACE FALTA --->  Gtk.Window.__init__(self, title="EJemplo con Gtk.Grid")

        Gtk.Grid.__init__(self)

        grid = Gtk.Grid()
        self.add(grid)

        boton1 = Gtk.Button(label="Boton1")
        boton2 = Gtk.Button(label="Boton2")
        boton3 = Gtk.Button(label="Boton3")
        boton4 = Gtk.Button(label="Boton4")
        boton5 = Gtk.Button(label="Boton5")
        boton6 = Gtk.Button(label="Boton6")
        boton7 = Gtk.Button(label="Boton7")

        # El primer botón solo hace falta añadirlo, los demás se añadirán tomándolo como referencia
        # AQUÍ, COMO EN ESTA CLASE HEREDAMOS DE GRID, LOS MÉTODOS DEBEN TENER EL "SELF" !!!!
        self.add(boton1)

        # tras indicar el parámetro, podemos indicar su posición COLUMNA-FILA,y su ancho y alto

        self.attach(boton2, 1, 0, 2, 1)

        # Podemos añadir y situar botones con "next_to" de manera más fácil
        self.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach(boton4, 1, 1, 2, 1)

        # Creamos una caja
        # Por defecto, las cajas tienen orientación horizontal
        caja = Gtk.Box()

        caja.pack_start(boton5, True, True, 0)
        caja.pack_start(boton6, True, True, 0)
        caja.pack_start(boton7, True, True, 0)

        self.attach_next_to(caja, boton4, Gtk.PositionType.BOTTOM, 1, 1)

        # Una vez tengamos todos listo, añadimos la grid
        self.add(grid)



        #################################################


if __name__ == "__main__":
    Ventana()
    Gtk.main()
