import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VentanaPrincipal():
    def __init__(self):
        builder = Gtk.Builder()

        builder.add_from_file("ESTUDIO1.glade")

        ventanaMain = builder.get_object("ventanaMain")
        box1 = builder.get_object("box1")
        self.txtEntNombre = builder.get_object("txtEntNombre")
        self.lblSaludo = builder.get_object("lblSaludo")
        self.btnSaludo = builder.get_object("btnSaludo")

        señales = {

            "on_txtEntNombre_activate": self.on_txtEntNombre_activate,
            "on_btnSaludo_clicked": self.on_btnSaludo_clicked,
            "on_ventanaMain_destroy": Gtk.main_quit

        }

        builder.connect_signals(señales)

        ventanaMain.show_all()

    def on_btnSaludo_clicked(self, boton):
        nombre = self.txtEntNombre.get_text()
        self.lblSaludo.set_text("Hola " + nombre)

    def on_txtEntNombre_activate(self, cuadroTexto):
        self.on_btnSaludo_clicked(cuadroTexto)


if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()
