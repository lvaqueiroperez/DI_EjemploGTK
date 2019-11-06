import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Ventana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Ejemplo stack")

        caja = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)

        self.add(caja)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)







        self.connect("destroy",Gtk.main_quit)
        self.show_all()



if __name__ == "__main__":
    Ventana()
    Gtk.main()
