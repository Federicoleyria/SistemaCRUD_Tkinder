import tkinter as tk
import tkinter.messagebox as mb
from tkinter.ttk import Button, Label, Style , Treeview
from empleado import Empleado

class EmpleadoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x500")
        self.root.title("Mi primer Login")
        
        fondo = "#88FFB4"
        
        # Estilo del botón
        self.style = Style()
        self.style.configure('TButton', font=("Arial", 12))
        
        # Partes del frame
        self.frame_superior = tk.Frame(self.root, bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)

        self.frame_inferior = tk.Frame(self.root, bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)

        # Título
        self.label_titulo = Label(self.frame_superior, text="Login", font=("Calisto MT", 36, "bold"), background=fondo)      
        self.label_titulo.pack(side="top", pady=20)

        # Usuario
        self.label_usuario = Label(self.frame_inferior, text="Usuario", font=("Arial", 18), background=fondo, foreground="black")
        self.label_usuario.grid(row=0, column=0, padx=10, sticky="e")
        
        self.entry_usuario = tk.Entry(self.frame_inferior, bd=0, width=14, font=("Arial", 18))
        self.entry_usuario.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        # Contraseña
        self.label_contraseña = Label(self.frame_inferior, text="Contraseña", font=("Arial", 18), background=fondo, foreground="black")
        self.label_contraseña.grid(row=1, column=0, padx=10, sticky="e")
        
        self.entry_contraseña = tk.Entry(self.frame_inferior, bd=0, width=14, font=("Arial", 18), show="*")
        self.entry_contraseña.grid(row=1, column=1, columnspan=3, padx=5, sticky="w")
        
        # Botón
        self.boton_ingresar = Button(self.frame_inferior, text="Ingresar", width=16, command=self.entrar, style='TButton')
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.root.mainloop()
        
    def entrar(self):
        nombre = self.entry_usuario.get()
        contra = self.entry_contraseña.get()
        
        if nombre == "Elon Musk" and contra == "1234":
            self.ventana_crud()
            self.root.withdraw()  
        else:
            mb.showinfo("Acceso Incorrecto", "Su nombre o contraseña están incorrectos")
    
    def ventana_crud(self):
        self.ven = tk.Toplevel(self.root)  # Usar Toplevel para crear una nueva ventana
        self.ven.title('Crud de Empleados')
        self.ven.geometry('1200x600')

        Label(self.ven, text="Gestión de empleados", font=("arial 15")).pack(pady=10)

        # Crear un frame para los inputs
        input_frame = tk.Frame(self.ven)
        input_frame.pack(pady=10)

        # Nombre
        Label(input_frame, text="Nombre", font=("arial 10")).grid(row=0, column=0, padx=5, pady=5)
        self.txtNombre = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.txtNombre, font=("arial 10")).grid(row=0, column=1, padx=5, pady=5)
        # Apellido
        Label(input_frame, text="Apellido", font=("arial 10")).grid(row=1, column=0, padx=5, pady=5)
        self.txtApellido = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.txtApellido, font=("arial 10")).grid(row=1, column=1, padx=5, pady=5)
        # Correo
        Label(input_frame, text="Correo", font=("arial 10")).grid(row=2, column=0, padx=5, pady=5)
        self.txtCorreo = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.txtCorreo, font=("arial 10")).grid(row=2, column=1, padx=5, pady=5)
        # Edad
        Label(input_frame, text="Edad", font=("arial 10")).grid(row=3, column=0, padx=5, pady=5)
        self.txtEdad = tk.IntVar()
        tk.Entry(input_frame, textvariable=self.txtEdad, font=("arial 10")).grid(row=3, column=1, padx=5, pady=5)
        # Dirección
        Label(input_frame, text="Dirección", font=("arial 10")).grid(row=4, column=0, padx=5, pady=5)
        self.txtDireccion = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.txtDireccion, font=("arial 10")).grid(row=4, column=1, padx=5, pady=5)
        # Salario
        Label(input_frame, text="Salario", font=("arial 10")).grid(row=5, column=0, padx=5, pady=5)
        self.txtSalario = tk.DoubleVar()
        tk.Entry(input_frame, textvariable=self.txtSalario, font=("arial 10")).grid(row=5, column=1, padx=5, pady=5)

        # Botones de acción
        action_frame = tk.Frame(self.ven)
        action_frame.pack(pady=10)

        Button(action_frame, text="Guardar", command=self.guardar).grid(row=0, column=0, padx=10)
        Button(action_frame, text="Consultar", command=self.consultar).grid(row=0, column=1, padx=10)
        Button(action_frame, text="Actualizar", command=self.actualizar).grid(row=0, column=2, padx=10)
        Button(action_frame, text="Eliminar", command=self.borrar).grid(row=0, column=3, padx=10)
        Button(action_frame, text="Datos de la tabla", command=self.consultar_tablas).grid(row=0, column=4, padx=10)

        # Tabla para mostrar los datos
        self.tree = Treeview(self.ven, columns=("Nombre", "Apellido", "Correo", "Dirección", "Edad", "Salario"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("Dirección", text="Dirección")
        self.tree.heading("Edad", text="Edad")
        self.tree.heading("Salario", text="Salario")
        self.tree.pack(fill="both", expand=True, pady=10)
        
    def guardar(self):
        if not all([self.txtNombre.get(), self.txtApellido.get(), self.txtCorreo.get(), self.txtEdad.get(), self.txtDireccion.get(), self.txtSalario.get()]):
            mb.showerror("Verificar", "El campo no puede estar vacío")
        else:
            empleado = Empleado()
            res = empleado.guardar(
                nombre=self.txtNombre.get(),
                apellido=self.txtApellido.get(),
                correo=self.txtCorreo.get(),
                edad=self.txtEdad.get(),
                direccion=self.txtDireccion.get(),
                salario=self.txtSalario.get()
            )
            if res:
                mb.showinfo("Éxito", "Se guardó correctamente")
                self.limpiarCampos()
            else:
                mb.showerror("Error", "No se pudo guardar")
            
    def consultar(self):
        if not self.txtCorreo.get():
            mb.showerror("Verificar", "Debe ingresar el correo")
        else:
            empleado = Empleado()
            res = empleado.consultar(correo=self.txtCorreo.get())
            if res:
                self.txtNombre.set(res[1])
                self.txtApellido.set(res[2])
                self.txtCorreo.set(res[3])
                self.txtEdad.set(res[4])
                self.txtDireccion.set(res[5])
                self.txtSalario.set(res[6])
                mb.showinfo("Éxito", "Estos son los resultados de tu consulta")
            else:
                mb.showerror("Error", "No se encontró el correo")
                self.limpiarCampos()
                
    def actualizar(self):
        if not all([self.txtNombre.get(), self.txtApellido.get(), self.txtCorreo.get(), self.txtEdad.get(), self.txtDireccion.get(), self.txtSalario.get()]):
            mb.showerror("Verificar", "Debe ingresar el correo")
        else:
            empleado = Empleado()
            res = empleado.actualizar(
                nombre=self.txtNombre.get(),
                apellido=self.txtApellido.get(),
                correo=self.txtCorreo.get(),
                edad=self.txtEdad.get(),
                direccion=self.txtDireccion.get(),
                salario=self.txtSalario.get()
            )
            if res:
                mb.showinfo("Éxito", "Estos son los resultados de tu actualización")
                self.limpiarCampos()
            else:
                mb.showerror("Error", "No se pudo actualizar")
                
    def borrar(self):
        if not self.txtCorreo.get():
            mb.showerror("Verificar", "Debe ingresar el correo")
        else:
            empleado = Empleado()
            res = empleado.eliminar(correo=self.txtCorreo.get())
            if res:
                mb.showinfo("Éxito", "Se eliminó correctamente")
                self.limpiarCampos()
            else:
                mb.showerror("Error", "No se pudo eliminar")
                
    def consultar_tablas(self):
        empleado = Empleado()
        res = empleado.consultar_tabla()
        if res:
            self.tree.delete(*self.tree.get_children())
            for row in res:
                self.tree.insert("", "end", values=(row[1], row[2], row[3], row[4], row[5], row[6]))
        else:
            mb.showerror("Error", "No se pudo consultar")
            
    def limpiarCampos(self):
        self.txtNombre.set("")
        self.txtApellido.set("")
        self.txtCorreo.set("")
        self.txtEdad.set("")
        self.txtDireccion.set("")
        self.txtSalario.set("")
        

if __name__ == "__main__":
    EmpleadoApp()
