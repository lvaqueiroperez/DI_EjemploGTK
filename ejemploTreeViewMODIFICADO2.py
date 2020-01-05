import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


class Fiestra(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo con Gtk.TreeView")
        self.set_default_size(400, 300)

        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # nombre, direccion, precio, si admite animales, num estrellas
        modelo = Gtk.ListStore(str, str, float, bool, int, str)
        modelo.append(["Hotel Melia", "García Barbón 48", 75.38, True,
                       1, "*"])
        modelo.append(["Hotel Galeones", "Avda Madrid", 80.88, False, 2, "**"])
        modelo.append(["Hotel Bahia", "Paseo as Avenidas 55", 60.38, True, 5, "*****"])

        # otro listStore para las categorías
        modeloCat = Gtk.ListStore(str, int)
        modeloCat.append(["*", 1])
        modeloCat.append(["**", 2])
        modeloCat.append(["***", 3])
        modeloCat.append(["****", 4])
        modeloCat.append(["*****", 5])

        # Creamos el TreeView añadiéndole un modelo
        vista = Gtk.TreeView(model=modelo)
        # PARA PODER TRABAJAR CON LAS SELECCIONES DEL TREEVIEW
        seleccion = vista.get_selection()
        seleccion.connect("changed", self.on_vista_changed)

        #RECOGEMOS EL MODELO Y EL ITERADOR DEL TREEVIEW PARA PODER MODIFICAR DATOS EN LAS CELDAS DEL TREEVIEW (ver función de modificar)
        self.modeloTV = vista.get_model()
        self.iteradorTV = self.modeloTV.get_iter("0")

        boxV.pack_start(vista, True, True, 0)

        # AÑADIR ELEMENTOS AL TREEVIEW:
        # Podemos crear un renderer para cada elemento que añadamos (columnas)
        celdaText = Gtk.CellRendererText()
        # con false no se pueden editar las celdas
        celdaText.set_property("editable", False)

        # Creamos una columna con un nombre, un renderer y una variable(text para string, value para nums....) con un valor numérico para
        # establecer qué columna va a mostrar la vista (valores diferentes paar cada columna siempre??)
        columnaHotel = Gtk.TreeViewColumn('Aloxamento', celdaText,
                                          text=0)
        # A la celda "Dirección" le ponemos una señal
        celdaDireccion = Gtk.CellRendererText()
        celdaDireccion.set_property("editable", True)
        celdaDireccion.connect("edited", self.on_celdaDireccion_edited, modelo)

        columnaDireccion = Gtk.TreeViewColumn('Dirección', celdaDireccion, text=1)

        # La celda "Ocupación" tendrá una barra de progreso
        celdaOcupacion = Gtk.CellRendererProgress()
        columnaOcupacion = Gtk.TreeViewColumn('Ocupación', celdaOcupacion, value=2)

        # La celda "Check" tendrá checkButtons
        celdaCheck = Gtk.CellRendererToggle()
        celdaCheck.connect("toggled", self.on_celdaCheck_toggled, modelo)

        columnaMascotas = Gtk.TreeViewColumn('Mascotas', celdaCheck, active=3)
        # columnaMascotas.add_attribute(celdaCheck, "active", 3)  # hace lo mismo que la linea de arriba

        # Y la última celda tendrá un comboBox para elegir las estrellas del hotel
        celdaCombo = Gtk.CellRendererCombo()
        celdaCombo.set_property("editable", True)  # que sea editable
        celdaCombo.set_property("model", modeloCat)
        celdaCombo.set_property("text-column", 0)  # muestra la columna 0
        celdaCombo.set_property("has-entry", False)  # le da la oportunidad al usuario de añadir nuevos valores(?)
        # Le ponemos el modelo de categorías
        celdaCombo.connect("changed", self.on_celdaCombo_changed, modelo, modeloCat)

        columnaCategoria = Gtk.TreeViewColumn('Categoría', celdaCombo, text=5)

        # AÑADIMOS A LA VISTA TODAS LAS COLUMNAS
        vista.append_column(columnaHotel)  # añadir al treeview la columna
        vista.append_column(columnaDireccion)
        vista.append_column(columnaOcupacion)
        vista.append_column(columnaMascotas)
        vista.append_column(columnaCategoria)

        # self.add(boxV)  # al añadir el boxH esta línea sobra

        # MONTAMOS TODOS EN LA VENTANA MAIN Y AÑADIMOS LABELS PARA COMPLETAR LA INTERFAZ
        boxH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.txtHotel = Gtk.Entry()
        self.txtDireccion = Gtk.Entry()
        self.txtOcupacion = Gtk.Entry()
        self.chkMascota = Gtk.CheckButton()
        self.cmbCategoria = Gtk.ComboBox()
        btnNovo = Gtk.Button("Novo")
        btnNovo.connect("clicked", self.on_btnNovo_clicked, modelo)

        # PARA EL BOTÓN DE MODIFICAR:
        btnModificar = Gtk.Button("Modificar")
        btnNovo.connect("clicked", self.on_btnModificar_clicked, modelo)

        boxH.pack_start(self.txtHotel, True, False, 0)
        boxH.pack_start(self.txtDireccion, True, False, 0)
        boxH.pack_start(self.txtOcupacion, True, False, 0)
        boxH.pack_start(self.chkMascota, True, False, 0)
        boxH.pack_start(self.cmbCategoria, True, False, 0)
        boxH.pack_start(btnNovo, True, False, 0)
        boxH.pack_start(btnModificar, True, False, 0)

        boxV.pack_start(boxH, True, False, 0)

        self.add(boxV)

        self.cmbCategoria.set_model(modeloCat)
        self.cmbCategoria.pack_start(celdaText, True)
        self.cmbCategoria.add_attribute(celdaText, "text", 0)

        self.show_all()
        self.connect("destroy", Gtk.main_quit)

        self.add(boxV)

        self.cmbCategoria.set_model(modeloCat)
        self.cmbCategoria.pack_start(celdaText, True)
        self.cmbCategoria.add_attribute(celdaText, "text", 0)

        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    # FUNCIONES:
    # PARA MARCAR/DESMARCAR LOS CHECKBUTTONS E INFORMAR DE SU ESTADO
    def on_celdaCheck_toggled(self, control, fila, modelo):
        modelo[fila][3] = not modelo[fila][3]

    # PARA EDITAR LA CELDA DE DIRECCIONES:
    def on_celdaDireccion_edited(self, control, fila, texto, modelo):
        modelo[fila][1] = texto

    # PARA CREAR UNA NUEVA COLUMNA EN EL TREEVIEW CON TODOS LOS DATOS PUESTOS
    def on_btnNovo_clicked(self, boton, modelo):
        modCat = self.cmbCategoria.get_model()
        indice = self.cmbCategoria.get_active_iter()
        modelo.append([self.txtHotel.get_text(),
                       self.txtDireccion.get_text(),
                       float(self.txtOcupacion.get_text()),
                       self.chkMascota.get_active(),
                       modCat[indice][1],
                       modCat[indice][0]])  # indice y columna

    # PARA PODER USAR EL COMBOBOX
    def on_celdaCombo_changed(self, control, posicion, indice, modelo, modeloCat):
        modelo[int(posicion)][5] = modeloCat[indice][0]
        # modelo[int(posicion)][4] = modeloCat[indice][1]
        print(modelo[int(posicion)][5], str(modelo[int(posicion)][4]))

    # PARA RECOGER LOS DATOS DE LA CELDA SELECCIONADA EN EL TREEVIEW
    def on_vista_changed(self, seleccion):
        (modelo, punteiro) = seleccion.get_selected()
        self.txtHotel.set_text(modelo[punteiro][0])
        self.txtDireccion.set_text(modelo[punteiro][1])
        self.txtOcupacion.set_text(str(modelo[punteiro][2]))
        if modelo[punteiro][3]:
            self.chkMascota.set_active(True)
        else:
            self.chkMascota.set_active(False)
        print(modelo[punteiro][4] - 1)

        self.cmbCategoria.set_active(modelo[punteiro][4] - 1)
        # print(modelo[punteiro][0], modelo[punteiro][1], modelo[punteiro][2])

    # BOTÓN MODIFICAR: acceder a la celda seleccionada y modificar los datos(utilizamos como parámetro nuestra variable ya creada "selección")
    def on_btnModificar_clicked(self, boton, modelo,seleccion):

        """borrar y volver a poner? o usar un método de modificación?"""




if __name__ == "__main__":
    Fiestra()
    Gtk.main()
