"""EJERCICIO EN EL QUE TENEMOS QUE HACER LA VENTANA MOSTRADA EN CLASE, PODEMOS USAR O NO GLADE """
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


# HEMOS USADO SOLO CÓDIGO DE MOMENTO
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
        self.txtEntData = builder.get_object("txtEntData")
        # Creamos señales que accederán a métodos
        # OJO, AL USAR CON GLADE LAS SEÑALES ACTIVATE O CUALQUIERA QUE
        # USEMOS TIENEN QUE ESTAR ESPECIFICADAS EN EL PROPIO GLADE !!!
        señales = {"on_txtEntData_activate": self.on_txtEntData_activate}

        builder.connect_signals(señales)

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
        # PARA QUE FUNCIONE LA COMBINACION CON GLADE, COMENTAMOS ESA LINEA
        # grid.attach(frmOpcions, 2, 0, 1, 3)

        # Añadimos a la caixaH1 la grid hecha con todos sus elementos
        # caixaH1.pack_start(grid, True, True, 0)
        # AÑADIMOS LA GRID DE GLADE:
        caixaH1.pack_start(grid1, True, True, 0)
        # PARA QUE FUNCIONE GLADE, AÑADIMOS ESTA LINEA:
        caixaH1.pack_start(frmOpcions, True, True, 0)

        # Añadimos a la caja principal la caixaH1 con todos sus elementos
        caixaVMain.pack_start(caixaH1, True, True, 0)

        # Creamos un frame para el segundo elemento de la caja principal/home/dam2/Documentos/PyCharmProjects/EjemploGTK
        frame2 = Gtk.Frame()
        # Dentro del frame tendremos una caja de texto "TextView"
        txvVoosDisponibles = Gtk.TextView()
        # PARA RECOGER UNA REFERENCIA AL BUFFER DEL TEXTVIEW:
        self.bufferTxv = txvVoosDisponibles.get_buffer()
        frame2.set_label("Voos disponibles")
        # Añadimos al frame la textview
        frame2.add(txvVoosDisponibles)
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

    # MÉTODOS: (tienen que estar fuera del self !!!)
    def on_txtEntData_activate(self, control):
        # self.bufferTxv.set_text(self.txtEntData.get_text())
        # El métofo "set_text" del buffer sobreescribe el texto anterior
        # Para conseguir que no se sobreescriba, usaremos el método
        # "insert(posición,texto): la posición viene dada por un TextIterator"
        posFin = self.bufferTxv.get_end_iter()

        self.bufferTxv.insert_markup(posFin, "<b>" + self.txtEntData.get_text() + "</b>", -1)

        self.bufferTxv.insert(posFin, "\n", -1)
        # -1 se pone para que imprima la totalidad del texto


if __name__ == "__main__":
    Ventana()
    Gtk.main()
