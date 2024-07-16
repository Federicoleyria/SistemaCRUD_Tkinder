# conexion.py
import mysql.connector

class Conexion:
    
    def __init__(self):
        with open("C:/Users/Windows/Downloads/password.txt",'r') as f:
            pwd= f.read()
       
        try:
            self.con = mysql.connector.connect(
                host='localhost',
                user='root',
                password=pwd,
                database='crud'
            )
            print("Conexión exitosa")
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.con = None 
            
    def conectar(self):
        return self.con

    def obtener_cursor(self):
        return self.con.cursor()

if __name__ == '__main__':
    # Crear una instancia de la clase Conexion para pruebas
    base_datos = Conexion()
    # Obtener el cursor utilizando el método obtener_cursor()
    cursor = base_datos.obtener_cursor()
