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

        # Ponemos los elementos como "self." para que se puedan usar en funciones (?)

        # Una vez creada la Ventana y la Caja, empezamos a CREAR Y CONFIGURAR los elementos de la interfaz QUE IRÁN EN LA CAJA
        self.btnSaludar = Gtk.Button(label="Saludo")
        # Configuramos la señal que tendrá este elemento y a que método accederá (definimos el método más adelante)
        #CADA SEÑAL TIENE UN NOMBRE ESPECÍFICO !!!
        self.btnSaludar.connect("clicked", self.on_btnSaludar_clicked)

        # Cada vez que introducimos un elemento nuevo, habrá que añadirlo con "pack_start()" o "pack_end()" al elemento que queramos (en este caso a la caja)
        # "pack_start" va de izq a derch, "pack_end" va de derech a izq /Y en Vertical de arriba a abajo, abajo a arriba
        # qué son los otros parámetros???
        caja.pack_end(self.btnSaludar, True, True, 6)

        #Creamos una entrada de texto:
        self.txtNombre = Gtk.Entry()
        self.txtNombre.set_text("Escribe aquí tu nombre");
        # Para que funcione el botón cuando le damos a enter,debemos activarlo como antes con un método:
        self.txtNombre.connect("activate", self.on_txtNombre_activate)

        caja.pack_end(self.txtNombre, True, True, 6)

        #Creamos un label
        self.lbSaludo = Gtk.Label()
        self.lbSaludo.set_text("Hola a todos")

        caja.pack_end(self.lbSaludo, True, True, 6)

        # Añadimos la caja a nuestra Ventana Principal
        self.add(caja)
        # Configuramos el cierre de la ventana principal
        self.connect("destroy", Gtk.main_quit)

        # Mostramos todos los elementos de la interfaz
        self.show_all()



    #Definimos funciones que van a usar algunos de los elementos:
    def on_btnSaludar_clicked(self, boton):
        nombre = self.txtNombre.get_text()
        self.lbSaludo.set_text("Hola " + nombre)
    #Para que funcione correctamente:
    def on_txtNombre_activate(self, cuadroTexto):
        self.on_btnSaludar_clicked(cuadroTexto)


#Por último, para que funcione:
if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()
