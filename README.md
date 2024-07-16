# Proyecto sistema de gestión

Este proyecto es una aplicación de escritorio diseñada para facilitar la gestión de empleados en una organización. La aplicación está desarrollada en Python, utilizando Tkinter para la interfaz gráfica de usuario y MySQL como sistema de gestión de bases de datos para almacenar y administrar la información de los empleados.

### Interfaz visual
![](https://github.com/Federicoleyria/SistemaCRUD_Tkinder/blob/main/imagenes_proyecto/login.PNG)![](https://github.com/Federicoleyria/SistemaCRUD_Tkinder/blob/main/imagenes_proyecto/sistema.PNG)

### Características
Login de usuario: Verifica el acceso a la aplicación.
CRUD de empleados: Permite crear, leer, actualizar y eliminar registros de empleados.
Interfaz intuitiva: Una interfaz de usuario amigable desarrollada con Tkinter.
Persistencia de datos: Utiliza MySQL para almacenar y gestionar la información de los empleados.
### Requisitos
Python 3.x
Tkinter
MySQL
mysql-connector-python
### Instalación
Clona el repositorio:

### bash
Copiar código

git clone https://github.com/tu_usuario/tu_repositorio.git

cd tu_repositorio

Instala las dependencias:

bash
Copiar código

pip install mysql-connector-python

Configura la base de datos MySQL:

Crea una base de datos llamada crud.
Ejecuta el siguiente script SQL para crear la tabla necesaria:
### sql
Copiar código
CREATE TABLE tb_empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    edad INT,
    direccion VARCHAR(255),
    salario DECIMAL(10, 2)
);
Configura la conexión a la base de datos:

Abre el archivo conexion.py y asegúrate de que las credenciales de la base de datos sean correctas:
### python
Copiar código
self.con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='tu_contraseña',
    database='crud'
)
### Ejecución
Para ejecutar la aplicación, simplemente ejecuta el archivo main.py:

bash
Copiar código
python main.py

### Estructura del Proyecto
main.py: Archivo principal que contiene la interfaz de usuario y la lógica de la aplicación.
empleado.py: Contiene la clase Empleado con métodos para interactuar con la base de datos.
conexion.py: Maneja la conexión a la base de datos MySQL.
### Uso
Login: Ingresa con el nombre de usuario "Elon Musk" y la contraseña "1234".
Gestión de empleados:
Guardar: Ingresa los datos de un empleado y haz clic en "Guardar".
Consultar: Ingresa el correo de un empleado y haz clic en "Consultar" para ver sus datos.
Actualizar: Ingresa los datos actualizados de un empleado y haz clic en "Actualizar".
Eliminar: Ingresa el correo de un empleado y haz clic en "Eliminar".
Datos de la tabla: Haz clic en "Datos de la tabla" para ver todos los registros de empleados.
### Contribuciones
Las contribuciones son bienvenidas. Puedes abrir un issue o enviar un pull request para discutir cualquier cambio que desees realizar.

