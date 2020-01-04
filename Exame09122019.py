import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 9-12-2019")
        self.set_border_width(10)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(caixaV)

        # CAJA VERTICAL PRINCIPAL
        # GRID DE ARRIBA
        grid = Gtk.Grid()

        imaxe = Gtk.Image()
        imaxe.set_from_icon_name("media-optical", 64)
        chkAnimado = Gtk.CheckButton("Animado")
        txvAreaTexto = Gtk.TextView()
        txvAreaTexto.set_size_request(420, 100)
        btnReproducir = Gtk.Button("Reproducir")
        btnPausa = Gtk.Button("Pausa")
        btnParar = Gtk.Button("Parar")
        btnSaltar = Gtk.Button("Saltar")
        self.cmbNumeros = Gtk.ComboBox()
        btnAbrirFicheiro = Gtk.Button("Abrir ficheiro...")
        btnFalarFicheiro = Gtk.Button("Reproducir ficheiro...")
        btnGardarComo = Gtk.Button("Gardar como...")
        btnReload = Gtk.Button("Recargar")

        grid.add(imaxe)
        grid.attach_next_to(chkAnimado, imaxe, Gtk.PositionType.BOTTOM, 1, 1)

        # OBTENEMOS BUFFER DEL TXTVIEW:
        txvAreaTexto.set_editable(False)
        self.txvBuffer = txvAreaTexto.get_buffer()

        # AÑADIMOS BARRA DE DESPLAZAMIENTO AL txtView
        ventanaScroll = Gtk.ScrolledWindow()
        ventanaScroll.set_hexpand(True)
        ventanaScroll.set_vexpand(True)

        ventanaScroll.add(txvAreaTexto)

        # Hay que poner en el margen izquierdo los botones:
        # Añadimos los botones y el textView
        grid.attach(ventanaScroll, 1, 0, 1, 8)
        grid.attach(btnReproducir, 2, 0, 4, 1)
        grid.attach_next_to(btnPausa, btnReproducir, Gtk.PositionType.BOTTOM, 4, 1)
        grid.attach_next_to(btnParar, btnPausa, Gtk.PositionType.BOTTOM, 4, 1)
        grid.attach_next_to(btnSaltar, btnParar, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.cmbNumeros, btnSaltar, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(btnAbrirFicheiro, btnSaltar, Gtk.PositionType.BOTTOM, 4, 1)
        grid.attach_next_to(btnFalarFicheiro, btnAbrirFicheiro, Gtk.PositionType.BOTTOM, 4, 1)
        grid.attach_next_to(btnGardarComo, btnFalarFicheiro, Gtk.PositionType.BOTTOM, 4, 1)
        grid.attach_next_to(btnReload, btnGardarComo, Gtk.PositionType.BOTTOM, 4, 1)

        # AÑADIMOS ITEMS AL CBOX:
        lista_formatos = Gtk.ListStore(str)
        lista_formatos.append(["mp3"])
        lista_formatos.append(["wav"])
        lista_formatos.append(["wma"])
        lista_formatos.append(["ogg"])

        self.cmbNumeros.set_model(lista_formatos)
        celdaTexto = Gtk.CellRendererText()

        self.cmbNumeros.pack_start(celdaTexto, True)
        self.cmbNumeros.add_attribute(celdaTexto, "text", 0)

        # Metemos señales al cbox:
        self.cmbNumeros.connect("changed", self.on_cmbNumeros_changed)

        caixaV.pack_start(grid, True, True, 0)

        # CAJA DE ABAJO (hay 2 archivos de glade)
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        builder = Gtk.Builder()
        builder.add_from_file("./cadroSonGlade.glade")
        contedorH1 = builder.get_object("grid2")
        caixaH.pack_start(contedorH1, False, False, 0)
        # He cambiado el nombre a "cadroOpcionsSonGlade2.glade"
        builder.add_from_file("cadroOpcionsSonGlade2.glade")
        contedorH2 = builder.get_object("frame1")

        # OBTENEMOS LOS CHKBUTTONS Y LES PONEMOS LAS SEÑALES
        self.chkB1 = builder.get_object("chkAsincrono")
        self.chkB1.connect("toggled", self.on_chk_toggled, "Asíncrono")
        self.chkB2 = builder.get_object("chkENomeFicheiro")
        self.chkB2.connect("toggled", self.on_chk_toggled, "É nome de ficheiro")
        self.chkB3 = builder.get_object("chkXmlPersistente")
        self.chkB3.connect("toggled", self.on_chk_toggled, "XML persistente")
        self.chkB4 = builder.get_object("chkFiltrarAntesReproducir")
        self.chkB4.connect("toggled", self.on_chk_toggled, "Filtrar antes de reproducir")
        self.chkB5 = builder.get_object("chkEXml")
        self.chkB5.connect("toggled", self.on_chk_toggled, "É XML")
        self.chkB6 = builder.get_object("chkReproduccionNPL")
        self.chkB6.connect("toggled", self.on_chk_toggled, "Reproducción NPL")

        caixaH.pack_start(contedorH2, False, False, 0)

        caixaV.pack_start(caixaH, False, False, 0)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    # Para mostrar por el terminal el formato selccionado
    def on_cmbNumeros_changed(self, combo):
        puntero = self.cmbNumeros.get_active_iter()

        if puntero is not None:
            modelo = combo.get_model()

            print("Opción seleccionada: " + modelo[puntero][0])

    def on_chk_toggled(self, control, nombre):
        if control.get_active():
            fin = self.txvBuffer.get_end_iter()
            self.txvBuffer.insert(fin, "Modo de reprodución: " + nombre + " seleccionado\n")


if __name__ == "__main__":
    Exame()
    Gtk.main()
