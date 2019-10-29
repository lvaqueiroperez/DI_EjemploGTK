import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

#Vamos a crear interfaces sin el uso de Glaide:
#Tendrenis que heredar de Window
class VentanaPrincipal(Gtk.Window):

    def __init__(self):

        Gtk.Window.__init__(self,title = "Ejemplo saludo GTK")

        #Creamos una caja y podemos aplicarle una separación a los elementos
        # Nuestro "box" por defecto define los elementos en horizontal, para cambiar y ponerla en vertical:
        #Añadir al constructor "Gtk.Orientation.VERTICAL
        caja = Gtk.Box(spacing = 6,orientation = Gtk.Orientation.VERTICAL)

        self.btnSaludar = Gtk.Button (label = "Saludo")

        self.btnSaludar.connect("clicked",self.on_btnSaludar_clicked)

        #Cada vez que introducimos un elemento nuevo, habrá que añadirlo con "pack_start()"
        #"pack_start" va de izq a derch, "pack_end" va de derech a izq
        caja.pack_end(self.btnSaludar,True,True,6)

        self.txtNombre = Gtk.Entry()
        self.txtNombre.set_text("Escribe aquí tu nombre");
        #Para que funcione el botón cuando le damos a enter:
        self.txtNombre.connect("activate",self.on_txtNombre_activate)

        caja.pack_end(self.txtNombre,True,True,6)

        self.lbSaludo = Gtk.Label()
        self.lbSaludo.set_text("Hola a todos")

        caja.pack_end(self.lbSaludo,True,True,6)





        self.add(caja)
        self.connect("destroy",Gtk.main_quit)



        self.show_all()


    def on_btnSaludar_clicked (self,boton):
        "Método que maneja el señal clicked del btnSaludar"
        nombre = self.txtNombre.get_text()
        self.lbSaludo.set_text("Hola " + nombre)


    def on_txtNombre_activate(self,cuadroTexto):
        self.on_btnSaludar_clicked(cuadroTexto)



if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()



"""EJERCICIO:
    Modificación de este programa: detectar que el nombre puesto no pueda estar vacío, escribiendo un mensaje qu e diga 'debes escribir tu nombre'
     en color rojo o con background en rojo"""
"""Buscar propiedades en la API"""