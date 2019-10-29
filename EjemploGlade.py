import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class VentanaPrincipal():
    def __init__(self):
        builder = Gtk.Builder()
        # Este "builder" permite construír en el código las ventanas hechas externamente en Glade, para poder manejar esos
        # objetos gtk e interactuar con ellos desde python

        builder.add_from_file("EjemploGlade1.glade")

        # la ventana solo nos interesa que sea una variable temporal de la clase
        ventanaMain1 = builder.get_object("ventanaMain1")
        # en cambio, los demás componentes como txtEntry queremos que sean variables de clase normales que se puedan modificar
        self.txtNombre = builder.get_object("txtNombre")
        self.lbSaludo = builder.get_object("lbSaludo")
        self.btnSaludar = builder.get_object("btnSaludar")

        señales = {

            "on_btnSaludar_clicked": self.on_btnSaludar_clicked,
            "on_txtNombre_activate": self.on_txtNombre_activate,
            "on_ventanaMain1_destroy": Gtk.main_quit #Este método ya viene definido
        }

        builder.connect_signals(señales)

        ventanaMain1.show_all()

    #Hay que definir las señales del gtk como métodos del propio python:

    def on_btnSaludar_clicked (self,boton):
        "Método que maneja el señal clicked del btnSaludar"
        nombre = self.txtNombre.get_text()
        self.lbSaludo.set_text("Hola " + nombre)


    def on_txtNombre_activate(self,cuadroTexto):
        self.on_btnSaludar_clicked(cuadroTexto)


#activamos nuestra interfaz gráfica
if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()




