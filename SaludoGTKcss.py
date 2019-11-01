import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# EJEMPLO DE USO DE UNA HOJA DE ESTILOS .CSS PARA NUESTRA INTERFAZ GRÁFICA:
# (para ello, podemos crear en el proyecto mismo un nuevo archivo con extensión ".css")
from gi.repository import Gdk


class VentanaPrincipal(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self, title="Ejemplo saludo GTK")

        # Creamos un "css provider"  y lo asignamos a una variable
        cssProvider = Gtk.CssProvider()
        # Cargamos nuestra hoja de estilos en ese "provider"
        cssProvider.load_from_path('./estilos.css')
        # Configuramos lo necesario para su correcto uso:
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        caja = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)

        self.btnSaludar = Gtk.Button(label="Saludo")

        self.btnSaludar.connect("clicked", self.on_btnSaludar_clicked)

        caja.pack_end(self.btnSaludar, True, True, 6)

        self.txtNombre = Gtk.Entry()
        self.txtNombre.set_text("Escribe aquí tu nombre");

        self.txtNombre.connect("activate", self.on_txtNombre_activate)

        caja.pack_end(self.txtNombre, True, True, 6)

        self.lbSaludo = Gtk.Label()
        self.lbSaludo.set_text("Hola a todos")

        caja.pack_end(self.lbSaludo, True, True, 6)

        self.add(caja)
        self.connect("destroy", Gtk.main_quit)

        self.show_all()

    def on_btnSaludar_clicked(self, boton):
        "Método que maneja el señal clicked del btnSaludar"
        nombre = self.txtNombre.get_text()

        if (nombre == ""):

            self.lbSaludo.set_markup("<span color='red'>Introduzca su nombre</span>")


        else:
            self.lbSaludo.set_text("Hola " + nombre)

    def on_txtNombre_activate(self, cuadroTexto):
        self.on_btnSaludar_clicked(cuadroTexto)


if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()
