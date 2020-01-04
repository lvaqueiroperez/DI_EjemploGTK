"""EJERCICIO EN EL QUE TENEMOS QUE HACER LA VENTANA MOSTRADA EN CLASE, USANDO CÓDIGO Y GLADE"""
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class Ventana(Gtk.Window):
    def __init__(self):
        # Creamos e inicializamos la ventana main
        Gtk.Window.__init__(self, title="Ejercicio")
        # Le damos un tamaño inicial
        self.set_default_size(400, 200)

        # Creamos la caja vertical principal de la interfaz
        caixaVMain = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Creamos la caja horizontal de 2 casillas donde irán los elementos de la parte superior de la interfaz
        caixaH1 = Gtk.Box()

        # COMENTAMOS EL CODIGO DE LA GRID PARA PONERLO COMO GLADE
        """# Creamos la grid que será 3x2 e irá en la primera casilla de caixaH1
        grid = Gtk.Grid()
        # Añadimos elementos a la Grid:
        # Labels:
        lblData = Gtk.Label("Data:")
        grid.add(lblData)
        lblDende = Gtk.Label("Dende:")
        grid.attach_next_to(lblDende, lblData, Gtk.PositionType.BOTTOM, 1, 1)
        lblAta = Gtk.Label("Ata:")
        grid.attach(lblAta, 0, 2, 1, 1)
        # Entrada de texto:
        txtData = Gtk.Entry()
        grid.attach_next_to(txtData, lblData, Gtk.PositionType.RIGHT, 1, 1)
        # Combo box
        cmbDende = Gtk.ComboBox()
        grid.attach_next_to(cmbDende, lblDende, Gtk.PositionType.RIGHT, 1, 1)
        cmbAta = Gtk.ComboBox()
        grid.attach_next_to(cmbAta, lblAta, Gtk.PositionType.RIGHT, 1, 1)
        """

        # AÑADIMOS LA GRID DESDE GLADE
        builder = Gtk.Builder()
        builder.add_from_file("EjercicioInterfaz1Combinado.glade")

        grid1 = builder.get_object("grid1")

        # PODEMOS RECOGER ELEMENTOS ECHOS EN GLADE EN NUESTRO
        # CÓDIGO PARA TRABAJAR CON ELLOS O MODIFICARLOS
        # PONEMOS SELF. PARA PODER RECOGER Y USAR VARIABLES DE LA CLASE EN LAS FUNCIONES DE LA CLASE
        self.txtEntData = builder.get_object("txtEntData")
        self.cboxDende = builder.get_object("cboxDende")
        self.cboxAta = builder.get_object("cboxAta")
        # EN GLADE, DEFINIMOS EL MANIPULADOR DE "CHANGED" DE cboxDende para poder trabajar con señales
        # TAMBIÉN DEFINIMOS EL MANIPULADOR DE "ACTIVATE" DE extEntData

        # Creamos señales que accederán a métodos
        # OJO, AL USAR CON GLADE LAS SEÑALES ACTIVATE O CUALQUIERA QUE
        # USEMOS TIENEN QUE ESTAR ESPECIFICADAS EN EL PROPIO GLADE !!!
        # NO HEMOS CREADO UNA SEÑAL PARA EL CBOX ATA
        señales = {"on_txtEntData_activate": self.on_txtEntData_activate,
                   "on_cboxDende_changed": self.on_cboxDende_changed}

        builder.connect_signals(señales)

        # CREAMOS UNA LIST STORE PARA ALMACENAR LOS ITEMS DE cboxDende
        # Cada item constará de 1 int y 2 str
        lista_destinos = Gtk.ListStore(int, str, str)
        # Para añadir elementos:
        lista_destinos.append([1, "Vigo", "VGO"])
        lista_destinos.append([1, "Santiago de Compostela", "STO"])
        lista_destinos.append([5, "Madrid", "MD"])
        lista_destinos.append([3, "Barcelona", "BCN"])

        # AÑADIMOS UN MODELO CON LOS ITEMS LISTADOS A cboxDende
        self.cboxDende.set_model(lista_destinos)

        # PARA QUE LOS ITEMS PUESTOS SEAN VISIBLES, SE NECESITA UN "RENDERER"
        celdaTexto = Gtk.CellRendererText()

        self.cboxDende.pack_start(celdaTexto, True)
        # Y UN ATRIBUTO
        # Queremos que inicialmente muestre la columna 2 como texto
        self.cboxDende.add_attribute(celdaTexto, "text", 2)

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

        # Creamos el formulario de opciones a través de un frame que contendrá una caja con 3 RadioButtons
        frmOpcions = Gtk.Frame()
        frmOpcions.set_label("Opcións")
        # Creamos una caja dentro del frame
        caixaFrm = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        # Creamos los "RadioButton" que irán dentro de la caja del frame:
        rbtPrimeira = Gtk.RadioButton("Primeira clase")
        rbtNegocios = Gtk.RadioButton("Negocios")
        rbtTurista = Gtk.RadioButton("Turista")
        caixaFrm.pack_start(rbtPrimeira, True, True, 0)
        caixaFrm.pack_start(rbtNegocios, True, True, 0)
        caixaFrm.pack_start(rbtTurista, True, True, 0)

        # Añadimos la caja al frame
        frmOpcions.add(caixaFrm)

        # Añadimos a la grid el frame en la posición deseada (OJO, EXISTE LA POSICIÓN 0 !!!)
        # PARA QUE FUNCIONE LA COMBINACION CON GLADE, COMENTAMOS ESA LINEA (teníamos el frame como parte del grid, ahora ya no)

        # grid.attach(frmOpcions, 2, 0, 1, 3)

        # Añadimos a la caixaH1 la grid hecha con todos sus elementos
        # caixaH1.pack_start(grid, True, True, 0)
        # AÑADIMOS LA GRID DE GLADE:
        caixaH1.pack_start(grid1, True, True, 0)
        # PARA QUE FUNCIONE GLADE, AÑADIMOS EL FORMULARIO DIRECTAMENTE A LA CAJA H1 CON PACK_START:
        caixaH1.pack_start(frmOpcions, True, True, 0)

        # Añadimos a la caja principal la caixaH1 con todos sus elementos
        caixaVMain.pack_start(caixaH1, True, True, 0)

        # Creamos un frame para el segundo elemento de la caja principal
        frame2 = Gtk.Frame()
        # Dentro del frame tendremos una caja de texto "TextView"
        txvVoosDisponibles = Gtk.TextView()

        # PARA RECOGER UNA REFERENCIA AL BUFFER DEL TEXTVIEW QUE USAREMOS EN LOS MÉTODOS:
        self.bufferTxv = txvVoosDisponibles.get_buffer()

        # PONEMOS EL txtView "editable" A FALSE PARA QUE NO SE PUEDA ESCRIBIR EN ÉL DIRECTAMENTE Y QUE SUS TEXTOS ESTÉN SIEMPRE CENTRADOS
        txvVoosDisponibles.set_editable(False)
        txvVoosDisponibles.set_justification(Gtk.Justification.CENTER)

        # CREAMOS UNA VENTANA SCROLL PARA EL TXTVIEW Y AÑADIMOS A ESTA VENTANA DE SCROLL NUESTRO TXTVIEW
        ventanaScroll = Gtk.ScrolledWindow()
        ventanaScroll.set_hexpand(True)
        ventanaScroll.set_vexpand(True)
        # AÑADIMOS A LA VENTANA CON SCROLL NUESTRO TEXTVIEW
        ventanaScroll.add(txvVoosDisponibles)
        # Ponemos la label al frame
        frame2.set_label("Voos disponibles")
        # Añadimos al frame la textview (LO COMENTAMOS PARA IMPLEMENTAR EL SCROLL)
        # frame2.add(txvVoosDisponibles)
        # AÑADIMOS LA VENTANA SCROLL CON TODOS SUS ELEMENTOS AL FRAME
        frame2.add(ventanaScroll)
        # Añadimos a la caja principal el frame de su segundo elemento
        caixaVMain.pack_start(frame2, True, True, 0)

        # Como tercer elemento de la caja principal haremos una caja con 3 botones:
        caixaH3 = Gtk.Box()

        btnBuscar = Gtk.Button("Buscar")
        btnMercar = Gtk.Button("Mercar")
        btnSair = Gtk.Button("Sair")

        caixaH3.pack_start(btnBuscar, True, True, 0)
        caixaH3.pack_start(btnMercar, True, True, 0)
        caixaH3.pack_start(btnSair, False, False, 20)
        # Ponemos la caja de botones como tercer elemento de la caja principal
        caixaVMain.pack_start(caixaH3, True, True, 0)
        # Añadimos la caja principal a la ventana main
        self.add(caixaVMain)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    # MÉTODOS: (tienen que estar a la misma altura que el de __init__ !!!)

    # PARA ESCRIBIR EN LA TEXTVIEW
    def on_txtEntData_activate(self, control):
        # self.bufferTxv.set_text(self.txtEntData.get_text())
        # El métofo "set_text" del buffer sobreescribe el texto anterior
        # Para conseguir que no se sobreescriba, usaremos el método
        # "insert(posición,texto): la posición viene dada por un TextIterator"
        # SE HA IMPLEMENTADO QUE, AL  SUBRAYAR UNA PORCIÓN DEL TEXTO DE LA TEXTVIEW, PODAMOS SUSTITUIRLO CON OTRO AL DARLE ----PENDIENTE-----
        # AL ENTER EN EL TEXTENTRY
        # seleccion = self.bufferTxv.get_selection
        # fondo_naranja=self.bufferTxv.create_tag.....
        # self.bufferTxv.delete(seleccion[0])

        # OBTENEMOS EL ITERADOR PARA SABER DONDE ESTÁ EL FINAL DEL ÚLTIMO TEXTO ESCRITO (variable buffer definida anteriormente)
        posFin = self.bufferTxv.get_end_iter()
        # INSERTAMOS TEXTO SIN QUE LO SOBREESCRIBA Y CON MARCAS DE HTML (negrita)
        self.bufferTxv.insert_markup(posFin, "<b>" + self.txtEntData.get_text() + "</b>", -1)
        # INSERTAMOS UN SALTO DE LÍNEA PARA QUE SE ESCRIBA MEJOR
        self.bufferTxv.insert(posFin, "\n", -1)
        # -1 se pone para que imprima la totalidad del texto

    # PARA DEFINIR EL CONTENIDO DEL COMBOBOX DENDE Y MOSTRARLO POR EL TERMINAL CUANDO LO SELECCIONEMOS
    def on_cboxDende_changed(self, combo):
        # OBTENEMOS ITERADOR DEL CBOXDENDE
        puntero = self.cboxDende.get_active_iter()
        # OBTENEMOS EL MODELO DEL COMBO
        if puntero is not None:
            modelo = combo.get_model()
            # fila/columna LO IMPRIME EN EL TERMINAL
            print("El aeropuerto seleccionado es: " + modelo[puntero][1] + " (" + modelo[puntero][2] + ")")


if __name__ == "__main__":
    Ventana()
    Gtk.main()
