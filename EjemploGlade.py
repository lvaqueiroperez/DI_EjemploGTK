import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

#Ejemplo de creación de interfaces usando el programa Glade y Python:
#OJO !!! Si queremos usar las interfaces ya creadas en un proyecto Glade, tendremos que guardar ese proyecto Glade en la misma
#carpeta que nuestro proyecto Python
class VentanaPrincipal():
    def __init__(self):
        # Este "builder" permite construír en el código las ventanas hechas externamente en Glade, para poder manejar esos
        # objetos gtk e interactuar con ellos desde python
        builder = Gtk.Builder()
        #Asignamos a nuestro builder el archivo de nuestro proyecto Glade
        builder.add_from_file("EjemploGlade1.glade")

        #Una vez tenemos el builder, empezaremos a coger cada elemento de nuestra interfaz hecha en Glade
        #La ventana solo nos interesa que sea una variable temporal de la Clase
        ventanaMain1 = builder.get_object("ventanaMain1")

        #En cambio, los demás componentes como txtEntry queremos que sean variables de clase normales que se puedan modificar
        self.txtNombre = builder.get_object("txtNombre")
        self.lbSaludo = builder.get_object("lbSaludo")
        self.btnSaludar = builder.get_object("btnSaludar")

        #Para configurar lo que haŕa cada elemento, recurrimos a las "señales" asignadas en Glade
        #Poniendo el nombre que tiene la señal y asignándole de la siguiente manera un método que haremos
        #en este código, podemos configurar nuestra interfaz
        señales = {

            "on_btnSaludar_clicked": self.on_btnSaludar_clicked,
            "on_txtNombre_activate": self.on_txtNombre_activate,
            "on_ventanaMain1_destroy": Gtk.main_quit #Este método ya viene predefinido !!!
        }

        #Cuando acabemos de codificar las señales, las asignamos a nuestro builder
        builder.connect_signals(señales)

        #Y mostramos toda la ventana "main"
        ventanaMain1.show_all()

    #Hay que definir las señales del gtk como métodos del propio python:


    #Método que maneja el señal clicked del btnSaludar (tenemos que pasarle el self y un parámetro cualquiera)
    def on_btnSaludar_clicked (self,boton):

        nombre = self.txtNombre.get_text()
        self.lbSaludo.set_text("Hola " + nombre)

    #Para que funcione, tenemos que activar también el elemento "txtNombre" de la siguiente manera,
    def on_txtNombre_activate(self,cuadroTexto):
        self.on_btnSaludar_clicked(cuadroTexto)


#ACTIVAMOS NUESTRA INTERFAZ GRÁFICA
if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()




