"""EJERCICIO EN EL QUE TENEMOS QUE HACER LA VENTANA MOSTRADA EN CLASE, PODEMOS USAR O NO GLADE """
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


# ORDENAR!!!! HEMOS USADO SOLO CÓDIGO DE MOMENTO
class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejercicio")

        self.set_default_size(400, 200)

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        caixaH1 = Gtk.Box()
        grid = Gtk.Grid()
        lblData = Gtk.Label("Data:")
        grid.add(lblData)  # lo pone en el primero
        lblDende = Gtk.Label("Dende:")
        grid.attach_next_to(lblDende, lblData, Gtk.PositionType.BOTTOM, 1, 1)
        lblAta = Gtk.Label("Ata:")
        grid.attach(lblAta, 0, 2, 1, 1)
        txtData = Gtk.Entry()
        grid.attach_next_to(txtData, lblData, Gtk.PositionType.RIGHT, 1, 1)
        cmbDende = Gtk.ComboBox()
        grid.attach_next_to(cmbDende, lblDende, Gtk.PositionType.RIGHT, 1, 1)
        cmbAta = Gtk.ComboBox()
        grid.attach_next_to(cmbAta, lblAta, Gtk.PositionType.RIGHT, 1, 1)

        txvVoosDisponibles = Gtk.TextView()


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
        grid.attach(frmOpcions, 2, 0, 1, 3)

        caixaH1.pack_start(grid, True, True, 0)
        # caixaH1.pack_start(frmOpcions, True, True, 0)
        caixaV.pack_start(caixaH1, True, True, 0)

        #En vez del otro frame, usamos uno nuevo en el que ponemos un textView
        frame2 = Gtk.Frame()
        frame2.set_label("Voos disponibles")

        frame2.add(txvVoosDisponibles)

        caixaV.pack_start(frame2, True, True, 0)
        caixaH3 = Gtk.Box()
        caixaV.pack_start(caixaH3, True, True, 0)

        btnBuscar = Gtk.Button("Buscar")
        btnMercar = Gtk.Button("Mercar")
        btnSair = Gtk.Button("Sair")

        caixaH3.pack_start(btnBuscar,True,True,0)
        caixaH3.pack_start(btnMercar, True, True, 0)
        caixaH3.pack_start(btnSair, False, False, 20)



        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Ventana()
    Gtk.main()
