import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        # ventana
        Gtk.Window.__init__(self, title="Estudio 2 sin glade")

        # Tamaño inicial:
        self.set_default_size(400, 200)
        # CAJA PRINCIPAL
        boxMain = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # CAJA HORIZONTAL 1
        boxH1 = Gtk.Box()

        # GRID DE BOXH1:

        grid1 = Gtk.Grid()

        # LABELS:
        lblData = Gtk.Label("Data:")
        # la añadimos a la grid en la posición 0,0
        grid1.add(lblData)

        lblDende = Gtk.Label("Dende:")
        grid1.attach_next_to(lblDende, lblData, Gtk.PositionType.BOTTOM, 1, 1)

        lblAta = Gtk.Label("Ata")
        grid1.attach_next_to(lblAta, lblDende, Gtk.PositionType.BOTTOM, 1, 1)

        # A LA DERECHA DE LAS LABELS:

        self.txtEntData = Gtk.Entry()
        # SEÑALES PARA EL txtEntData, que va a interactuar con el txtView
        self.txtEntData.connect("activate", self.on_txtEntData_activate)

        grid1.attach_next_to(self.txtEntData, lblData, Gtk.PositionType.RIGHT, 1, 1)

        self.cboxDende = Gtk.ComboBox()

        # CREAMOS UN LIST STORE PARA ALMACENAR LOS ITEMS DEL CBOX:
        self.listaDestinos = Gtk.ListStore(int, str, str)

        self.listaDestinos.append([1, "Vigo", "VGO"])
        self.listaDestinos.append([2, "Barcelona", "BCN"])
        self.listaDestinos.append([5, "Madrid", "MAD"])

        # AÑADIMOS COMO MODELO ESTA LIST STORE AL CBOX
        self.cboxDende.set_model(self.listaDestinos)

        # PARA QUE SEAN VISIBLES LOS ITEMS, PONEMOS UN RENDERER:
        cRender1 = Gtk.CellRendererText()
        self.cboxDende.pack_start(cRender1, True)
        # ATRIBUTO PARA QUE SE MUESTRE CIERTA COLUMNA CUANDO USAMOS EL CBOX (aquí las columnas empiezan en 1):
        self.cboxDende.add_attribute(cRender1, "text", 2)

        # AÑADIMOS UNA SEÑAL AL CBOXDENDE:
        self.cboxDende.connect("changed", self.on_cboxDende_changed)

        grid1.attach_next_to(self.cboxDende, lblDende, Gtk.PositionType.RIGHT, 1, 1)

        self.cboxAta = Gtk.ComboBox()
        grid1.attach_next_to(self.cboxAta, lblAta, Gtk.PositionType.RIGHT, 1, 1)

        # AÑADIMOS ITEMS A cboxAta:
        # VAMOS A AÑADIR ICONOS
        lista_iconos = Gtk.ListStore(str, str)
        lista_iconos.append(["novo", "document-new"])
        lista_iconos.append(["Abrir", "document-open"])
        lista_iconos.append(["Guardar", "document-save"])

        self.cboxAta.set_model(lista_iconos)

        celdaImagen = Gtk.CellRendererPixbuf()
        self.cboxAta.pack_start(celdaImagen, True)
        # PONER ICON_NAME PARA QUE FUNCIONEN LOS ICONOS !!!
        self.cboxAta.add_attribute(celdaImagen, "icon_name", 1)


        boxH1.pack_start(grid1, True, True, 0)

        # A LA DERECHA DE GRID1:

        # FRAME
        frameOpciones = Gtk.Frame()

        frameOpciones.set_label("Opciones")

        # CAJA DEL FRAME
        boxFrame = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # RADIOBUTTONS:

        rbtnPrimera = Gtk.RadioButton("Primera")
        boxFrame.pack_start(rbtnPrimera, True, True, 0)

        rbtnNegocios = Gtk.RadioButton("Negocios")
        boxFrame.pack_start(rbtnNegocios, True, True, 0)

        rbtnTurista = Gtk.RadioButton("Turista")
        boxFrame.pack_start(rbtnTurista, True, True, 0)

        frameOpciones.add(boxFrame)

        # Metiendo el frame como un pack_start de la boxH1:
        # boxH1.pack_start(frameOpciones,True,True,0)

        # Metiendo el frame como un elemento más de la guid1: (HAY POSICIÓN 0 !!!!)
        grid1.attach(frameOpciones, 2, 0, 1, 3)

        boxMain.pack_start(boxH1, True, True, 0)

        # SIGUIENTE CELDA DE LA BOXMAIN:

        # Frame

        frameVoos = Gtk.Frame()
        frameVoos.set_label("Voos")

        # TextView

        self.txtvVoos = Gtk.TextView()
        # PARA QUE NO LO PODAMOS EDITAR DIRECTAMENTE
        self.txtvVoos.set_editable(False)
        # BUFFER:
        self.bufferTxtv = self.txtvVoos.get_buffer()
        # PARA QUE LO QUE SE ESCRIBA EN ÉL ESTÉ CENTRADO
        self.txtvVoos.set_justification(Gtk.Justification.CENTER)

        # SCROLL PARA PODER MOVERNOS POR EL TXTVIEW
        ventanaScroll = Gtk.ScrolledWindow()

        ventanaScroll.set_hexpand(True)
        ventanaScroll.set_vexpand(True)

        # AÑADIMOS A LA VENTANA SCROLL EL TXTVIEW Y LUEGO LA VENTANA AL FRAME
        ventanaScroll.add(self.txtvVoos)

        # frameVoos.add(self.txtvVoos)
        frameVoos.add(ventanaScroll)

        boxMain.pack_start(frameVoos, True, True, 0)

        # TERCERA CELDA DE LA BOXMAIN:

        boxH3 = Gtk.Box()

        # Botones:

        btnBuscar = Gtk.Button("Buscar")
        boxH3.pack_start(btnBuscar, True, True, 0)

        btnComprar = Gtk.Button("Comprar")
        boxH3.pack_start(btnComprar, True, True, 0)

        btnSalir = Gtk.Button("Salir")
        boxH3.pack_start(btnSalir, True, True, 0)

        boxMain.pack_start(boxH3, True, True, 0)

        self.add(boxMain)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    # FUNCIONES

    # PARA PASAR EL TEXTO DE UN TXTENT A UN TXTVIEW CUANDO LO ACTIVAMOS (LE DAMOS AL ENTER)
    def on_txtEntData_activate(self, control):
        # OBTENEMOS EL ITERADOR CON SU POSICION FINAL
        final = self.bufferTxtv.get_end_iter()
        # INSERTAMOS EL TEXTO PUESTO EN EL TXTENTRY Y PONEMOS UN SALTO DE LÍNEA
        self.bufferTxtv.insert_markup(final, "<b>" + self.txtEntData.get_text() + "</b>", -1)

        self.bufferTxtv.insert(final, "\n", -1)

    # PARA QUE AL SELECCIONAR UN ITEM DE UN CBOX SE MUESTRE POR EL TERMINAL:
    def on_cboxDende_changed(self, combo):
        # OBTENEMOS UN PUNTERO DEL CBOX PARA SABER SU POSICIÓN:
        puntero = self.cboxDende.get_active_iter()

        if puntero is not None:
            # OBTENEMOS EL MODELO
            modelo = combo.get_model()

            print("El aeropuerto seleccionado es: " + modelo[puntero][1] + " " + modelo[puntero][2])


if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()
