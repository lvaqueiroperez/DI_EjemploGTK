 # IMPORTANDO LA GRID DESDE GLADE
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VentanaGrid():
    def __init__(self):
        builder = Gtk.Builder()

        builder.add_from_file("GridGlade1.glade")
        # muchas veces, con importar la ventana principal y sus elementos llega, el contenedor/panel no suele hacer falta
        # ponerlo en el código

        ventanaMain = builder.get_object("ventanaMain")

        boton1 = builder.get_object("boton1")
        boton2 = builder.get_object("boton2")
        boton3 = builder.get_object("boton3")
        boton4 = builder.get_object("boton4")
        boton5 = builder.get_object("boton5")
        boton6 = builder.get_object("boton6")

        ventanaMain.connect("destroy",Gtk.main_quit)

        ventanaMain.show_all()


if __name__ == "__main__":
    VentanaGrid()
    Gtk.main()
