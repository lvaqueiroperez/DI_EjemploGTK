import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


# HEMOS QUITADO LA FUNCIÓN QUE HACE QUE AL CLICKAR EN "OCUPACIÓN" SE ORDENEN LAS CELDAS DE MOMENTO
class Fiestra(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo TreeStore")

        modeloTreeStore = Gtk.TreeStore(str, int)

        # bucle for usando "range" (creará 5 punteros avo)
        for avo in range(5):
            punteroAvo = modeloTreeStore.append(None,["Avo", avo])

            for pai in range(4):
                punteroPai = modeloTreeStore.append(punteroAvo, ["Pai", pai])

                for fillo in range(3):
                    modeloTreeStore.append(punteroPai, ["Fillo", fillo])


        vista = Gtk.TreeView(modeloTreeStore)
        tvcolumna = Gtk.TreeViewColumn("Parentesco")
        vista.append_column(tvcolumna)
        celda = Gtk.CellRendererText()
        tvcolumna.pack_start(celda,True)
        tvcolumna.add_attribute(celda,"text",0)

        tvcolumna = Gtk.TreeViewColumn("Orde")
        vista.append_column(tvcolumna)
        celda = Gtk.CellRendererText()
        tvcolumna.pack_start(celda,True)
        tvcolumna.add_attribute(celda,"text",1)


        self.add(vista)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

        #EJERCICIO:
        """
        
        """


if __name__ == "__main__":
    Fiestra()
    Gtk.main()
