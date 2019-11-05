import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# Vamos a crear interfaces sin el uso de Glaide:
# Tendremos que heredar de Window
class VentanaPrincipal(Gtk.Window):

    def __init__(self):
        # Creamos la ventana principal:
        Gtk.Window.__init__(self, title="Ejemplo saludo GTK")

        # Creamos una caja y podemos aplicarle una separación a los elementos
        # Nuestro "box" por defecto define los elementos en horizontal, para cambiar y ponerla en vertical:
        # Añadir al constructor "Gtk.Orientation.VERTICAL"
        caja = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)

        #Ponemos los elementos como "self." para que se puedan usar en funciones (?)

        # Una vez creada la Ventana y la Caja, empezamos a CREAR Y CONFIGURAR los elementos de la interfaz
        self.btnSaludar = Gtk.Button(label="Saludo")
        # Configuramos la señal que tendrá este elemento y a que método accederá (definimos el método más adelante)
        self.btnSaludar.connect("clicked", self.on_btnSaludar_clicked)

        # Cada vez que introducimos un elemento nuevo, habrá que añadirlo con "pack_start()" o "pack_end()"
        # "pack_start" va de izq a derch, "pack_end" va de derech a izq
        #qué son los otros parámetros???
        caja.pack_end(self.btnSaludar, True, True, 6)

        self.txtNombre = Gtk.Entry()
        self.txtNombre.set_text("Escribe aquí tu nombre");
        # Para que funcione el botón cuando le damos a enter,debemos activarlo como antes con un método:
        self.txtNombre.connect("activate", self.on_txtNombre_activate)

        caja.pack_end(self.txtNombre, True, True, 6)

        self.lbSaludo = Gtk.Label()
        self.lbSaludo.set_text("Hola a todos")

        caja.pack_end(self.lbSaludo, True, True, 6)

        # Añadimos la caja
        self.add(caja)
        # Configuramos el cierre de la ventana
        self.connect("destroy", Gtk.main_quit)

        # Mostramos todos los elementos de la interfaz
        self.show_all()

    def on_btnSaludar_clicked(self, boton):
        nombre = self.txtNombre.get_text()
        self.lbSaludo.set_text("Hola " + nombre)

    def on_txtNombre_activate(self, cuadroTexto):
        self.on_btnSaludar_clicked(cuadroTexto)


if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()

