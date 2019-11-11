import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# LA MAYOR DIFERENCIA ENTRE STACK Y NOTEBOOK ES QUE EL NOTEBOOK TIENE MÁS MÉTODOS ÚTILES
# NO VA EL EFECTO DE TRANSICIÓN??? PARA QUÉ SIRVE LA CAJA CREADA???
class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo stack")

        # Creamos una caja
        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        # Creamos el Stack
        stack = Gtk.Stack()
        # Podemos poner un efecto de transición a sus elementos
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        casillaVerification = Gtk.CheckButton("Pulsame")

        stack.add_titled(casillaVerification, "check", "Casilla verificacion")

        etiqueta = Gtk.Label()
        etiqueta.set_markup("<big>Una etiqueta simple</big>")
        stack.add_titled(etiqueta, "etiqueta", "una etiqueta simple")

        panel = Panel()
        stack.add_titled(panel, "Panel", "Panel con botones")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

        caja.pack_start(stack_switcher, True, True, 0)
        caja.pack_start(stack, True, True, 0)

        self.add(caja)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

        # Usamos clase panel que contiene la Grid()
        ####################################################


class Panel(Gtk.Grid):
    def __init__(self):
        # ESTO NO HACE FALTA --->  Gtk.Window.__init__(self, title="EJemplo con Gtk.Grid")

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

        #################################################


if __name__ == "__main__":
    Ventana()
    Gtk.main()
