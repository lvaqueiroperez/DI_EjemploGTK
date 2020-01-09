import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

#HEMOS QUITADO LA FUNCIÓN QUE HACE QUE AL CLICKAR EN "OCUPACIÓN" SE ORDENEN LAS CELDAS DE MOMENTO
class Fiestra(Gtk.Window):

    def __init__(self):  # constructor
        Gtk.Window.__init__(self, title="Exemplo con Gtk.TreeView")
        self.set_default_size(400, 300)

        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.modelo = Gtk.ListStore(str, str, float, bool, int, str)
        self.modelo.append(["Hotel Melia", "García Barbón 48", 75.38, True, 1, "*"])  # nombre, direccion, precio, admite animales, num estrellas
        self.modelo.append(["Hotel Galeones", "Avda Madrid", 80.88, False, 2, "**"])
        self.modelo.append(["Hotel Bahia", "Paseo as Avenidas 55", 60.38, True, 5, "*****"])
        self.filtradoOcupacion = False
        modeloFiltrado = self.modelo.filter_new()
        modeloFiltrado.set_visible_func(self.ocupacion, 80.0)  # parametros que se van a filtrar
        self.modelo.set_sort_func(0,self.ordeAlfabetico)

        modeloCat = Gtk.ListStore(str, int)
        modeloCat.append(["*", 1])
        modeloCat.append(["**", 2])
        modeloCat.append(["***", 3])
        modeloCat.append(["****", 4])
        modeloCat.append(["*****", 5])

        vista = Gtk.TreeView(model=modeloFiltrado)
        # vista = Gtk.TreeView(model=modelo)
        seleccion = vista.get_selection()
        seleccion.connect("changed", self.on_vista_changed)
        boxV.pack_start(vista, True, True, 0)

        celdaText = Gtk.CellRendererText()
        celdaText.set_property("editable", False)  # con false no se pueden editar las celdas

        columnaHotel = Gtk.TreeViewColumn('Aloxamento', celdaText, text=0)  # de la columna del modelo qué columna va a mostrar la vista: la 0 "Hotel ..."

        celdaDireccion = Gtk.CellRendererText()
        celdaDireccion.set_property("editable", True)
        celdaDireccion.connect("edited", self.on_celdaDireccion_edited, self.modelo)

        columnaDireccion = Gtk.TreeViewColumn('Dirección', celdaDireccion, text=1)
        celdaOcupacion = Gtk.CellRendererProgress()
        columnaOcupacion = Gtk.TreeViewColumn('Ocupación', celdaOcupacion, value=2)
        columnaOcupacion.set_sort_column_id(0)  # si hacemos clic en la columna ocupacion la ordena

        celdaCheck = Gtk.CellRendererToggle()
        celdaCheck.connect("toggled", self.on_celdaCheck_toggled, self.modelo)

        columnaMascotas = Gtk.TreeViewColumn('Mascotas', celdaCheck, active=3)
        # columnaMascotas.add_attribute(celdaCheck, "active", 3)  # hace lo mismo que la linea de arriba


        celdaCombo = Gtk.CellRendererCombo()
        celdaCombo.set_property("editable", True)  # que sea editable
        celdaCombo.set_property("model", modeloCat)
        celdaCombo.set_property("text-column", 0)  # muestra la columna 0
        celdaCombo.set_property("has-entry", False)  # le da la oportunidad al usuario de añadir nuevos valores
        celdaCombo.connect("changed", self.on_celdaCombo_changed, self.modelo, modeloCat)

        columnaCategoria = Gtk.TreeViewColumn('Categoría', celdaCombo, text=5)
        vista.append_column(columnaHotel)  # añadir al treeview la columna
        vista.append_column(columnaDireccion)
        vista.append_column(columnaOcupacion)
        vista.append_column(columnaMascotas)
        vista.append_column(columnaCategoria)

        # self.add(boxV)  # al añadir el boxH esta línea sobra

        boxH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.txtHotel = Gtk.Entry()
        self.txtDireccion = Gtk.Entry()
        self.txtOcupacion = Gtk.Entry()
        self.chkMascota = Gtk.CheckButton()
        self.cmbCategoria = Gtk.ComboBox()
        btnNovo = Gtk.Button("Novo")
        btnNovo.connect("clicked", self.on_btnNovo_clicked, self.modelo)
        boxH.pack_start(self.txtHotel, True, False, 0)
        boxH.pack_start(self.txtDireccion, True, False, 0)
        boxH.pack_start(self.txtOcupacion, True, False, 0)
        boxH.pack_start(self.chkMascota, True, False, 0)
        boxH.pack_start(self.cmbCategoria, True, False, 0)
        boxH.pack_start(btnNovo, True, False, 0)
        boxV.pack_start(boxH, True, False, 0)
        caixaFiltro = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.chkFiltro = Gtk.CheckButton(label='Filtro ocupación')
        self.chkFiltro.connect("toggled", self.on_chkFiltro_toggled, modeloFiltrado)
        caixaFiltro.pack_start(self.chkFiltro, True, True, 0)

        boxV.pack_start(caixaFiltro, True, False, 0)
        self.add(boxV)

        self.cmbCategoria.set_model(modeloCat)
        self.cmbCategoria.pack_start(celdaText, True)
        self.cmbCategoria.add_attribute(celdaText, "text", 0)

        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def on_celdaCheck_toggled(self, control, fila, modelo):  # nos deja marcar/desmarcar las opciones
        modelo[fila][3] = not modelo[fila][3]

    def on_celdaDireccion_edited(self, control, fila, texto, modelo):  # podemos editar la celda de direcciones
        modelo[fila][1] = texto

    def on_btnNovo_clicked(self, boton, modelo):
        modCat = self.cmbCategoria.get_model()
        indice = self.cmbCategoria.get_active_iter()
        modelo.append([self.txtHotel.get_text(),
                       self.txtDireccion.get_text(),
                       float(self.txtOcupacion.get_text()),
                       self.chkMascota.get_active(),
                       modCat[indice][1],
                       modCat[indice][0]])  # indice y columna

    def on_celdaCombo_changed(self, control, posicion, indice, modelo, modeloCat):
        modelo[int(posicion)][5] = modeloCat[indice][0]
        # modelo[int(posicion)][4] = modeloCat[indice][1]
        print(modelo[int(posicion)][5], str(modelo [int(posicion)][4]))

    def on_vista_changed(self, seleccion):
        (modelo, punteiro) = seleccion.get_selected()
        self.txtHotel.set_text(modelo[punteiro][0])
        self.txtDireccion.set_text(modelo[punteiro][1])
        self.txtOcupacion.set_text(str(modelo[punteiro][2]))
        if modelo[punteiro][3]:
            self.chkMascota.set_active(True)
        else:
            self.chkMascota.set_active(False)
        print(modelo[punteiro][4]-1)
        self.cmbCategoria.set_active(modelo[punteiro][4]-1)
        # print(modelo[punteiro][0], modelo[punteiro][1], modelo[punteiro][2])

    def ocupacion(self, modelo, punteiro, porcentaxeOcupacion):
        if self.filtradoOcupacion is None or self.filtradoOcupacion is False:
            return True
        else:
            return self.modelo[punteiro][2] > porcentaxeOcupacion

    def on_chkFiltro_toggled(self, control, modeloFiltrado):
        self.filtradoOcupacion = not self.filtradoOcupacion
        modeloFiltrado.refilter()

    def ordeAlfabetico(modelo,fila1,fila2,datosUsuario):
        #DEVUELVE 2 VALORES, EL SEGUNDO NO NOS IMPORTA POR ESO LO GUARDAMS EN UNA BARRA BAJA
        columna_ordear, _ = modelo.get_sort_column_id()
        valor1 = modelo.get_value(fila1,columna_ordear)
        valor2 = modelo.get_value(fila2,columna_ordear)

        if valor1 < valor2:
            return -1
        elif valor1 == valor2:
            return 0
        else:
            return 1


if __name__ == "__main__":
    Fiestra()
    Gtk.main()