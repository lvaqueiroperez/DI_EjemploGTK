import gi
#ver como habilitar más autocompletados relativos a GTK
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gio


class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo HeaderBar")

        self.set_default_size(400,200)


        cabecera = Gtk.HeaderBar()


        cabecera.set_show_close_button(True)
        #props es una alternativa de poner/modificar propiedades en vez de usar ".set_title()...etc"
        cabecera.props.title = "Muestra de uso de HeaderBar"
        self.set_titlebar(cabecera)

        boton=Gtk.Button()
        icon = Gio.ThemedIcon(name='mail-send-receive-symbolic')

        imagen = Gtk.Image.new_from_gicon(icon,Gtk.IconSize.BUTTON)

        boton.add(imagen)
        cabecera.pack_end(boton)

        caja = Gtk.Box()
        Gtk.StyleContext.add_class(caja.get_style_context(),"linked")

        #OJO!!!, en python se puede (no se debe) usar el mismo identificador para varias variables
        boton2=Gtk.Button()

        boton2.add(Gtk.Arrow(Gtk.ArrowType.LEFT,Gtk.ShadowType.NONE))

        caja.add(boton2)

        boton3 = Gtk.Button()

        boton3.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))

        caja.add(boton3)

        cabecera.pack_start(caja)

        self.add((Gtk.TextView()))






        self.connect("destroy", Gtk.main_quit)
        self.show_all()




if __name__ == "__main__":
    Ventana()
    Gtk.main()