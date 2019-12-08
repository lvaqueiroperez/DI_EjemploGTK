import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Estudio 3")

        grid = Gtk.Grid()

        b1 = Gtk.Button("B1")
        grid.attach(b1, 0, 0, 1, 1)

        b2 = Gtk.Button("B2")
        grid.attach(b2, 1, 0, 2, 1)

        b3 = Gtk.Button("B3")
        grid.attach(b3, 0, 1, 1, 2)

        b4 = Gtk.Button("B4")
        grid.attach(b4, 1, 1, 2, 1)

        box = Gtk.Box()

        b5 = Gtk.Button("B5")
        box.pack_start(b5, True, True, 0)
        b6 = Gtk.Button("B6")
        box.pack_start(b6, True, True, 0)
        # b7 usado como prueba
        b7 = Gtk.Button("B7")
        box.pack_start(b7, True, True, 0)

        # TRUCO: CUANDO NO TENGAMOS CLARO QUÉ COORDENADA UTILIZAR, PODEMOS USAR EL ATTACH_NEXT_TO Y PROBAR
        # AL PONER LAS DIMENSIONES A LA CAJA, LOS BOTONES QUE TIENE DENTRO SE REDIMENSIONAN CON ELLA
        # VEMOS QUE, EN EL CASO DE TENER 3 BOTONES(QUE EN TEORÍA CAUSARÍA UN CONFLICTO CON LAS DIMENSIONES),
        # EL ATTACH_NEXT_TO REDIMENSIONA NUESTROS ELEMENTOS AUTOMÁTICAMENTE !!!
        grid.attach_next_to(box, b4, Gtk.PositionType.BOTTOM, 2, 1)

        self.add(grid)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()
