# COPIAMOS EL EJERCICIO INTERFAZ 1 Y QUITAMOS TODOS LOS ELEMENTOS PUESTOS A TRAVÉS DE GLADE (LA GRID DONDE ESTAABAN LOS COMBOBOX ETC) Y LO MOFICAMOS
# (al final hemos copiado el código del profe)


import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class Fiestra(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Reserva de voos")
        self.set_default_size(400, 200)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaH1 = Gtk.Box()

        """
        builder = Gtk.Builder()
        builder.add_from_file("aplicacionGrid.glade")
        grade = builder.get_object("grdGrade")
        self.txtData = builder.get_object("txtData")
        self.cmbDende = builder.get_object("cmbDende")
        self.cmbAta = builder.get_object("cmbAta")

        sinais = {"on_txtData_activate": self.on_txtData_activate,
                  "on_cmbDende_changed": self.on_cmbDende_changed}
        builder.connect_signals(sinais)

        lista_destinos = Gtk.ListStore(int, str, str)
        lista_destinos.append([1, "Vigo", "VGO"])
        lista_destinos.append([2, "Santiago de Compostela", "SCO"])
        lista_destinos.append([3, "Madrid", "MAD"])
        lista_destinos.append([4, "Barcelona", "BCN"])
        self.cmbDende.set_model(lista_destinos)
        celdaTexto = Gtk.CellRendererText()
        self.cmbDende.set_entry_text_column(1)

        self.cmbDende.pack_start(celdaTexto, True)
        self.cmbDende.add_attribute(celdaTexto, "text", 2)

        lista_iconos = Gtk.ListStore(str, str)
        lista_iconos.append(["Novo", "document-new"])
        lista_iconos.append(["Abrir", "document-open"])
        lista_iconos.append(["Gardar", "document-save"])
        self.cmbAta.set_model(lista_iconos)
        celdaImaxe = Gtk.CellRendererPixbuf()
        self.cmbAta.pack_start(celdaImaxe, True)
        self.cmbAta.add_attribute(celdaImaxe, "icon_name", 1)
        """

        grid = Gtk.Grid()
        lblData = Gtk.Label("Data:")
        grid.add(lblData)  # lo pone en el primero
        lblDende = Gtk.Label("Dende:")
        grid.attach_next_to(lblDende, lblData, Gtk.PositionType.BOTTOM, 1, 1)
        lblAta = Gtk.Label("Ata:")
        grid.attach(lblAta, 0, 2, 1, 1)
        txtData = Gtk.Entry()
        grid.attach_next_to(txtData, lblData, Gtk.PositionType.RIGHT, 1, 1)

        lista_destinos = Gtk.ListStore(int, str, str)
        lista_destinos.append([1, "Vigo", "VGO"])
        lista_destinos.append([2, "Santiago de Compostela", "SCO"])
        lista_destinos.append([3, "Madrid", "MAD"])
        lista_destinos.append([4, "Barcelona", "BCN"])
        # VAMOS A HACER QUE, ADEMÁS DE PODER SELECCIONAR LOS ITEMS DEL CBOX, TAMBIÉN PODAMOS ESCRIBIR EN ÉL Y AÑADIRLE ELEMENTOS ADICIONALES
        # y le introducimos su modelo
        self.cmbDende = Gtk.ComboBox.new_with_model_and_entry(lista_destinos)
        # Preparamos el renderer
        celdaTexto = Gtk.CellRendererText()
        # Ponemos el text entry al cbox
        self.cmbDende.set_entry_text_column(1)
        # Añadimos al cbox y configuramos su atributo
        self.cmbDende.pack_start(celdaTexto, True)
        self.cmbDende.add_attribute(celdaTexto, "text", 1)

        # CONECTAMOS LAS SEÑALES (PARA QUE FUNCIONE, NECESITAMOS UNA REFERENCIA AL ELEMENTO DE TXTENTRY, PARA QUE AL PULSAR ENTER NOS VAYA)
        self.cmbDende.connect("changed", self.on_cmbDende_changed)
        # RELACIONAMOS EL TXT QUE TENDRÁ EL CBOX DENDE CON EL PROPIO CBOXDENDE:
        self.txtDende = self.cmbDende.get_child()
        # LE PONEMOS LA SEÑAL ACTIVATE Y SU FUNCIÓN
        self.txtDende.connect("activate", self.on_txtDende_activate)

        # AÑADIMOS A LA GRID EL CBOX DENDE
        grid.attach_next_to(self.cmbDende, lblDende, Gtk.PositionType.RIGHT, 1, 1)
        # (y el ata)
        cmbAta = Gtk.ComboBox()
        grid.attach_next_to(cmbAta, lblAta, Gtk.PositionType.RIGHT, 1, 1)

        # AHORA, PARA EL FRAME DE LA BOX1
        frmOpcions = Gtk.Frame()
        frmOpcions.set_label("Opcións")
        caixaFrm = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frmOpcions.add(caixaFrm)

        # HACER QUE LOS BOTONES SE PUEDAN SELECCIONAR BIEN Y QUE APAREZCA SU TEXTO ABAJO EN LA TXTVIEW:
        rbtPrimeira = Gtk.RadioButton("Primeira clase")
        rbtNegocios = Gtk.RadioButton("Negocios")
        rbtTurista = Gtk.RadioButton("Turista")
        # Hacemos grupos (siempre queda uno sin unirse, el primero, y los demás se unen a su botón anterior)
        rbtNegocios.join_group(rbtPrimeira)
        rbtTurista.join_group(rbtNegocios)
        # PONEMOS SEÑALES, EL TERCER PARÁMETRO ES EL TEXTO QUE SE ESCRIBIRÁ
        rbtPrimeira.connect("toggled", self.on_rbts_toggle, "Primera\n")
        rbtNegocios.connect("toggled", self.on_rbts_toggle, "Negocios\n")
        rbtTurista.connect("toggled", self.on_rbts_toggle, "Turista\n")
        # Y AÑADIMOS
        caixaFrm.pack_start(rbtPrimeira, True, True, 0)
        caixaFrm.pack_start(rbtNegocios, True, True, 0)
        caixaFrm.pack_start(rbtTurista, True, True, 0)
        # grid.attach(frmOpcions, 2, 0, 1, 3)

        caixaH1.pack_start(grid, True, True, 0)
        # caixaH1.pack_start(grade, True, True, 0)
        caixaH1.pack_start(frmOpcions, True, True, 0)
        caixaV.pack_start(caixaH1, True, True, 0)

        # EL FRAME SIGUE IGUAL PERO SIN LOS TEXTOS EN NEGRITA
        frame2 = Gtk.Frame()
        frame2.set_label("Voos disponibles")
        caixaV.pack_start(frame2, True, True, 0)
        fiestraScroll = Gtk.ScrolledWindow()
        fiestraScroll.set_hexpand(True)
        fiestraScroll.set_vexpand(True)
        txvVoosDisponibles = Gtk.TextView()
        self.bufferTxv = txvVoosDisponibles.get_buffer()
        txvVoosDisponibles.set_editable(False)
        txvVoosDisponibles.set_justification(Gtk.Justification.CENTER)
        txvVoosDisponibles.set_wrap_mode(True)
        # frame2.add(txvVoosDisponibles)
        fiestraScroll.add(txvVoosDisponibles)
        frame2.add(fiestraScroll)

        caixaH3 = Gtk.Box()
        caixaV.pack_start(caixaH3, True, True, 0)
        btnBuscar = Gtk.Button("Buscar")
        btnComprar = Gtk.Button("Comprar")
        btnSair = Gtk.Button("Sair")
        caixaH3.pack_start(btnBuscar, True, True, 0)
        caixaH3.pack_start(btnComprar, True, True, 0)
        caixaH3.pack_start(btnSair, False, False, 20)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    # (no va?)
    def on_txtData_activate(self, control):

        seleccion = self.bufferTxv.get_selection_bounds()
        fondo_laranxa = self.bufferTxv.create_tag("f_laranxa", background="orange")

        if len(seleccion) != 0:
            # self.bufferTxv.delete(seleccion[0], seleccion[1])
            # self.bufferTxv.insert_markup(seleccion[0], "<b>" + self.txtData.get_text() + "</b>", -1)
            self.bufferTxv.apply_tag(fondo_laranxa, seleccion[0], seleccion[1])
        else:
            fin = self.bufferTxv.get_end_iter()
            self.bufferTxv.insert_markup(fin, "<b>" + self.txtData.get_text() + "</b>", -1)
            self.bufferTxv.insert(fin, "\n", -1)

    # PARA QUE EL CBOX DENDE IMPRIMA LAS SELECCIONES POR CONSOLA:
    def on_cmbDende_changed(self, combo):
        punteiro = combo.get_active_iter()
        if punteiro is not None:
            modelo = combo.get_model()
            print("O aeroporto seleccionado é: " + modelo[punteiro][1] + " (" + modelo[punteiro][2] + ")")

            # CON SOLO EL "CHANGED" DE CBOX NO VA, NECESITAMOS UNA REFERENCIA DEL TXTENTRY QUE TIENE EL CBOX
        """else:
            # Si el puntero no se activa, significaría que estamos usando el cuadro de búsqueda del cbox
            entry = combo.get_child()
            fin = self.bufferTxv.get_end_iter()
            self.bufferTxv.insert(fin,entry.get_text())"""

    # PARA QUE EL TEXTO DE CBOX DENDE SE AÑADA COMO ITEM AL CBOXDENDE
    def on_txtDende_activate(self, entry):

        fin = self.bufferTxv.get_end_iter()
        texto = entry.get_text()
        self.bufferTxv.insert(fin, texto)

        modelo = self.cmbDende.get_model()

        modelo.append([1, texto, "txt"])

    # PARA QUE LOS RADIOBUTTON IMPRIMAN EN EL TXTVIEW SU NOMBRE INDICANDO QUE SE HAN ACTIVADO:
    def on_rbts_toggle(self, control, nombre):

        if control.get_active():
            # pillamos la posicion de buffer (la última)
            fin = self.bufferTxv.get_end_iter()
            self.bufferTxv.insert(fin, "Activado el RadioButton: " + nombre)


if __name__ == "__main__":
    Fiestra()
    Gtk.main()
