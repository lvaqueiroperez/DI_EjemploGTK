# importamos la libreria
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WPrincipal1(Gtk.Window):

    def __init__(self):
        # al heredar de window heradmos su constructor
        Gtk.Window.__init__(self, title="Ejemplo TreeView")
        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)

        # Modelo
        modelo = Gtk.ListStore(str, str, float, bool, int)
        modelo.append(["Hotel 1", "Calle 1", 72.0, True, 1])
        modelo.append(["Hotel 2", "Calle 2", 50.0, False, 2])
        modelo.append(["Hotel 3", "Calle 3", 35.0, True, 3])

        # Vista
        vista = Gtk.TreeView(model=modelo)

        # Renderer
        celdaText = Gtk.CellRendererText()
        celdaText.set_property("editable", False)  # No podemos modificar esta celda
        columnaHotel = Gtk.TreeViewColumn('Alojamiento', celdaText, text=0)

        celdaDireccion = Gtk.CellRendererText()
        celdaDireccion.set_property("editable", True)
        celdaDireccion.connect("edited", self.on_celdaDireccion_edited, modelo)
        columnaHotel2 = Gtk.TreeViewColumn('Dirección', celdaDireccion, text=1)

        # columnaHote3 = Gtk.TreeViewColumn('Precio', celdaText, text=2)
        # columnaHote4 = Gtk.TreeViewColumn('Ocupación', celdaText, text=3)
        celdaOcupacion = Gtk.CellRendererProgress()
        columnaHote3 = Gtk.TreeViewColumn('Ocupación', celdaOcupacion, value=2)

        celdaCheck = Gtk.CellRendererToggle()
        # para que se pueda realizar el evento sobre los checks y pasar como parametro el modelo
        celdaCheck.connect("toggled", self.on_celdaCheck_toggled, modelo)
        columnaHote4 = Gtk.TreeViewColumn('Mascota', celdaCheck, active=3)

        columnaHote5 = Gtk.TreeViewColumn("Categoria", celdaText, text=4)

        vista.append_column(columnaHotel)
        vista.append_column(columnaHotel2)
        vista.append_column(columnaHote3)
        vista.append_column(columnaHote4)
        vista.append_column(columnaHote5)

        # box horizontal para añadir nuevo hotel
        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.txtHotel = Gtk.Entry()
        self.txtDireccion = Gtk.Entry()
        self.txtOcupacion = Gtk.Entry()
        self.chkMascota = Gtk.CheckButton()
        self.cmbCategoria = Gtk.ComboBox()
        btnNovo = Gtk.Button("Nuevo")
        btnNovo.connect("clicked", self.on_btnNovo_clicked, modelo)

        box2.pack_start(self.txtHotel, True, True, 0)
        box2.pack_start(self.txtDireccion, True, True, 0)
        box2.pack_start(self.txtOcupacion, True, True, 0)
        box2.pack_start(self.chkMascota, True, True, 0)
        box2.pack_start(self.cmbCategoria, True, True, 0)
        box2.pack_start(btnNovo, True, True, 0)

        box.pack_start(box2, True, True, 0)
        self.add(box2)

        modeloCat = Gtk.ListStore(str, int)
        modeloCat.append(["*", 1])
        modeloCat.append(["**", 2])
        modeloCat.append(["***", 3])
        modeloCat.append(["****", 4])
        modeloCat.append(["*****", 5])
        self.cmbCategoria.set_model(modeloCat)
        self.cmbCategoria.pack_start(celdaText, True)
        self.cmbCategoria.add_attribute(celdaText, "text", 0)

        # permite añadir un control
        box.pack_start(vista, True, True, 0)

        self.add(box)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_celdaCheck_toggled(self, control, fila, modelo):
        # recojo el evento que hay en la celda y le doy inverso para cambiar el modelo de false a true
        modelo[fila][3] = not modelo[fila][3]

    def on_celdaDireccion_edited(self, control, fila, texto, modelo):
        modelo[fila][1] = texto

    def on_btnNovo_clicked(self, boton, modelo):
        # para la categoria
        modCat = self.cmbCategoria.get_model()
        # cual es el elemento seleccionado
        indice = self.cmbCategoria.get_active_iter()

        modelo.append([self.txtHotel.get_text(),
                       self.txtDireccion.get_text(),
                       float(self.txtOcupacion.get_text()),
                       self.chkMascota.get_active(),
                       modCat[indice][1]
                       ])


if __name__ == "__main__":
    WPrincipal1()
    Gtk.main()
