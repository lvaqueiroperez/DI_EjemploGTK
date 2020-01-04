import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# LO MUESTRA MAL?????????
# Creación de Notebook GTK usando solo código Y REUTILIZANDO EL CÓDIGO DE "EjemploGTKGrid" DE ANTES
class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo con Gtk Notebook")
        # Creamos componente Notebook
        notebook = Gtk.Notebook()

        # Creamos "páginas" del notebook a partir de los componentes que queramos, una caja por ejemplo:
        pagina1 = Gtk.Box()
        # PARA SEPARAR LOS ELEMENTOS DEL BORDE DE LA CAJA, PONEMOS UNA "ANCHURA DE BORDE" QUE LOS SEPARA
        pagina1.set_border_width(10)
        pagina1.add(Gtk.Label("Página por defecto"))
        # Añadimos la "página" a nuestro notebook, pudiendo darle un título a la solapa:
        notebook.append_page(pagina1, Gtk.Label("Título de la solapa"))

        # Creamos un objeto de la Clase reutilizada "Panel" y lo añadimos como página
        # ESE OBJETO DE LA CLASE "Panel" CONTIENE YA DIRECTAMENTE UNA GRID
        pagina2 = Panel()
        notebook.append_page(pagina2, Gtk.Label("Botones"))

        pagina3 = Panel()

        notebook.append_page(pagina3, Gtk.Label("Botones pag 3"))

        pagina4 = Gtk.Box()
        pagina4.set_border_width(10)
        pagina4.add(Gtk.Label("Página con icono en la pestaña"))
        # SI QUEREMOS QUE EL TÍTULO DE LA SOLAPA SEA UN ICONO:
        notebook.append_page(pagina4, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

        self.add(notebook)

        # Añadimos la función de salir de la ventana
        self.connect("destroy", Gtk.main_quit)

        # Y las mostramos
        self.show_all()


# VAMOS A USAR EL CÓDIGO DE "EJEMPLOGTKGRID"
# AQUÍ, EN VEZ DE CREAR UNA VENTANA CON UN GRID CREAMOS SOLO EL COMPONENTE GRID PARA ASÍ PODER USARLO EN OTRAS CLASES DE MANERA FÁCIL !!!
####################################################
class Panel(Gtk.Grid):
    def __init__(self):
        # ESTO NO HACE FALTA --->  Gtk.Window.__init__(self, title="EJemplo con Gtk.Grid")
        # NECESITAREMOS UN GRID, NO UNA VENTANA:
        Gtk.Grid.__init__(self)

        grid = Gtk.Grid()

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
        self.attach_next_to(boton4, boton2, Gtk.PositionType.BOTTOM, 2, 1)
        self.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)

        # Creamos una caja
        # Por defecto, las cajas tienen orientación horizontal
        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        caja.pack_start(boton7, True, True, 0)

        self.attach_next_to(caja, boton1, Gtk.PositionType.BOTTOM, 1, 1)

        # Una vez tengamos todos listo, añadimos la grid
        self.add(grid)
        # Esto es una clase Grid que usaremos en nuestra interfaz, NO ES LA VENTANA PRINCIPAL DE LA INTERFAZ
        #################################################


if __name__ == "__main__":
    Ventana()
    Gtk.main()
