import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        # ventana
        Gtk.Window.__init__(self, title="Estudio1 sin Glade")

        # box1

        box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # btnSaludo

        self.btnSaludo = Gtk.Button(label="saludo")
        # OJO!! El nombre de las señales se simplifican cuando no usamos Glade
        self.btnSaludo.connect("clicked", self.on_btnSaludo_clicked)

        box1.pack_end(self.btnSaludo, True, True, 6)

        # txtEntNombre

        self.txtEntNombre = Gtk.Entry()
        self.txtEntNombre.connect("activate", self.on_txtEntNombre_activate)

        box1.pack_end(self.txtEntNombre, True, True, 6)

        # lblSaludo

        self.lblSaludo = Gtk.Label()
        self.lblSaludo.set_text("Hola a todos")

        box1.pack_end(self.lblSaludo, True, True, 6)

        self.add(box1)

        self.connect("destroy", Gtk.main_quit)

        self.show_all()

    def on_btnSaludo_clicked(self, boton):
        nombre = self.txtEntNombre.get_text()
        self.lblSaludo.set_text("Hola " + nombre)

    def on_txtEntNombre_activate(self, cuadroTexto):
        self.on_btnSaludo_clicked(cuadroTexto)


if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()
