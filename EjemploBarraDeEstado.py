import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


class Ventana(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo barra de estado")
        self.set_default_size(400, 300)
        # PARA QUE NO DE FALLO LA PRIMERA VEZ QUE SE EJECUTA
        self.modoActivo = False
        # Creamos una caja con orientación Vertical
        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # Creamos la barra de progreso y la añadimos a la cajaVertical
        self.barraProgreso = Gtk.ProgressBar()
        cajaV.pack_start(self.barraProgreso, True, True, 0)
        # Creamos unos chkButtons para interactuar con nuestra barra de progreso
        chkTexto = Gtk.CheckButton("Mostrar texto")
        # les ponemos su señal de toggled y los añadimos a la caja vertical
        chkTexto.connect("toggled", self.on_chkTexto_toggled)
        cajaV.pack_start(chkTexto, True, True, 0)

        chkModoActividad = Gtk.CheckButton("Modo activo")
        chkModoActividad.connect("toggled", self.on_chkModoActividad_toggled)
        cajaV.pack_start(chkModoActividad, True, True, 0)

        chkIzquierdaDerecha = Gtk.CheckButton("Izquierda a derecha")
        chkIzquierdaDerecha.connect("toggled", self.on_chkIzquierdaDerecha_toggled)
        cajaV.pack_start(chkIzquierdaDerecha, True, True, 0)

        # Variables necesarioas para el funcionamiento de la barra de estado
        self.timeout_id = GLib.timeout_add(50, self.on_timeout, None)
        self.activity_mode = False

        # Añadimos a nuestra ventana main la caja vertical... etc
        self.add(cajaV)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    # FUNCIONES

    # Para que al clickar en en chkButton "chkTexto" la barra de estado se ponga por la mitad y muestre un mensaje
    def on_chkTexto_toggled(self, control):
        # Recogemos el estado del chkButton con "control.get_active()" cada vez que clickamos en él
        mostrarTexto = control.get_active()
        if mostrarTexto:
            texto = "Mensaje a mostrar"
        else:
            texto = None

        self.barraProgreso.set_fraction(0.50)
        self.barraProgreso.set_text(texto)
        self.barraProgreso.set_show_text(mostrarTexto)

    # Para que al clickar en "chkModoActividad" la barra de progreso vaya de un lado a otro
    def on_chkModoActividad_toggled(self, control):
        self.modoActivo = control.get_active()
        if self.modoActivo:
            # actualiza la barra de progreso
            self.barraProgreso.pulse()
        else:
            self.barraProgreso.set_fraction(0.0)

    # Para que al clickar en "chkIzquierdaDerecha" la barra avance en sentido contrario !!!
    def on_chkIzquierdaDerecha_toggled(self, control):
        izqDer = control.get_active()
        self.barraProgreso.set_inverted(izqDer)

    # PARA QUE SE GENERE UN "PULSO" REGULARMENTE
    def on_timeout(self, datos_usuario):
        if self.modoActivo:
            self.barraProgreso.pulse()
        else:
            novo_valor = self.barraProgreso.get_fraction() + 0.01
            if novo_valor > 1:
                novo_valor = 0
            self.barraProgreso.set_fraction(novo_valor)

        return True


if __name__ == "__main__":
    Ventana()
    Gtk.main()
