import gi

# ver como habilitar más autocompletados relativos a GTK
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


# Creacuión de una ventana con "HeaderBar": (se pueden poner elementos en una cabecera/headerbar)
class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo HeaderBar")

        self.set_default_size(400, 200)
        # Creamos la HeaderBar
        cabecera = Gtk.HeaderBar()
        # Podemos ponerle un botón de cerrado:
        cabecera.set_show_close_button(True)
        # props es una alternativa de poner/modificar propiedades en vez de usar ".set_title()...etc"
        cabecera.props.title = "Muestra de uso de HeaderBar"
        # cabecera.set_title("Muestra de uso de una cabecera/headerbar")

        boton = Gtk.Button()
        # Creamos un icono basado en los que ya están guardados en el SO !!!
        icon = Gio.ThemedIcon(name='mail-send-receive-symbolic')
        # Creamos la imagen del icono
        imagen = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        # Y se la asignamos a nuestro botón
        boton.add(imagen)
        # Ponemos el botón en nuestra CABECERA !
        cabecera.pack_end(boton)

        # Creamos caja
        caja = Gtk.Box()
        # ????
        Gtk.StyleContext.add_class(caja.get_style_context(), "linked")

        # OJO!!!, en python se puede (no se debe) usar el mismo identificador para varias variables
        # Añadimos 2 botones a la caja con forma de flecha que estarán en pack_start
        boton2 = Gtk.Button()

        boton2.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))

        caja.add(boton2)

        boton3 = Gtk.Button()

        boton3.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))

        caja.add(boton3)

        cabecera.pack_start(caja)

        # Ponemos la cabecera a nuestra ventana como una "titlebar":
        self.set_titlebar(cabecera)

        # Añadimos, por probar, una caja de texto a la eventana principal:
        self.add((Gtk.TextView()))

        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Ventana()
    Gtk.main()
