# COPIAMOS EL EJERCICIO INTERFAZ 1 Y QUITAMOS TODOS LOS ELEMENTOS PUESTOS A TRAVÉS DE GLADE (LA GRID DONDE ESTAABAN LOS COMBOBOX ETC) Y LO MOFICAMOS
# (al final hemos copiado el código del profe)
# PREGUNTAR QUÉ SE HA HECHO
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
        # Vamos a buscar dentro del combo box sus items, para ello primero ponemos una modelo con Entry:
        cmbDende = Gtk.ComboBox.new_with_model_and_entry(lista_destinos)
        celdaTexto = Gtk.CellRendererText()
        cmbDende.set_entry_text_column(1)
        cmbDende.pack_start(celdaTexto, True)
        cmbDende.add_attribute(celdaTexto, "text", 1)

        # CONECTAMOS LAS SEÑALES (PARA QUE FUNCIONE, NECESITAMOS UNA REFERENCIA AL ELEMENTO DE TXTENTRY, PARA QUE AL PULSAR ENTER NOS VAYA)
        cmbDende.connect("changed", self.on_cmbDende_changed)
        # Esto !!!
        self.txtDende = cmbDende.get_child()
        self.txtDende.connect("activate", self.on_txtDende_activate)



        grid.attach_next_to(cmbDende, lblDende, Gtk.PositionType.RIGHT, 1, 1)
        cmbAta = Gtk.ComboBox()
        grid.attach_next_to(cmbAta, lblAta, Gtk.PositionType.RIGHT, 1, 1)

        frmOpcions = Gtk.Frame()
        frmOpcions.set_label("Opcións")
        caixaFrm = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        frmOpcions.add(caixaFrm)
        rbtPrimeira = Gtk.RadioButton("Primeira clase")
        rbtNegocios = Gtk.RadioButton("Negocios")
        rbtTurista = Gtk.RadioButton("Turista")
        caixaFrm.pack_start(rbtPrimeira, True, True, 0)
        caixaFrm.pack_start(rbtNegocios, True, True, 0)
        caixaFrm.pack_start(rbtTurista, True, True, 0)
        # grid.attach(frmOpcions, 2, 0, 1, 3)

        caixaH1.pack_start(grid, True, True, 0)
        # caixaH1.pack_start(grade, True, True, 0)
        caixaH1.pack_start(frmOpcions, True, True, 0)
        caixaV.pack_start(caixaH1, True, True, 0)

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

    #ARREGLAR !!!!!!!
    def on_txtDende_activate(self, entry):

        fin = self.bufferTxv.get_end_iter()
        texto = entry.get_text()
        self.bufferTxv.insert(fin, texto)

        modelo = self.cmbDende.get_model()

        modelo.append([1,texto,"txt"])

if __name__ == "__main__":
    Fiestra()
    Gtk.main()
