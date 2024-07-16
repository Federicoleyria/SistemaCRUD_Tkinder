# empleado.py
from conexion import Conexion

class Empleado:
    
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.apellido = ""
        self.correo = ""
        self.edad = 0
        self.direccion = ""
        self.salario = 0.0
        self.con = Conexion()
        self.sql = ""

    def guardar(self, nombre, apellido, correo, edad, direccion, salario):
        try:
            conn = self.con.conectar()
            cursor = conn.cursor()
            self.sql = '''
            INSERT INTO tb_empleados(nombre, apellido, correo, edad, direccion, salario)             
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            # Ejecutamos la query con parámetros
            cursor.execute(self.sql, (nombre, apellido, correo, edad, direccion, salario))
            # Se confirman los cambios en la base de datos.
            conn.commit()
            # Se verifica cuántas filas fueron afectadas por la consulta.
            resp = cursor.rowcount
            cursor.close()
            conn.close()
            if resp == 1:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al guardar el empleado: {e}")
            return False

    def consultar(self, correo):
        try:
            conn = self.con.conectar()
            cursor = conn.cursor()
            self.sql = '''
            SELECT id, nombre, apellido, correo, edad, direccion, salario
            FROM tb_empleados
            WHERE correo = %s
            '''
            # Ejecutamos la query con parámetros
            cursor.execute(self.sql, (correo,))
            # Obtenemos el resultado de la consulta
            resultado = cursor.fetchone()
            cursor.close()
            conn.close()
            return resultado
        except Exception as e:
            print(f"Error al consultar el empleado: {e}")
            return False
        
        
    def actualizar(self, nombre, apellido, edad, direccion, salario, correo):
        try:
            conn = self.con.conectar()
            cursor = conn.cursor()
            self.sql = '''
            UPDATE tb_empleados 
            SET nombre=%s, apellido=%s,edad=%s,direccion=%s, salario=%s
            WHERE correo = %s
            '''
            # Ejecutamos la query con parámetros
            cursor.execute(self.sql, (nombre, apellido, edad, direccion, salario, correo))
            # Obtenemos el resultado de la consulta
            conn.commit()
            resultado = cursor.rowcount
            cursor.close()
            conn.close()
            return resultado == 1
        except Exception as e:
            print(f"Error al actualizar el empleado: {e}")
            return False
    
    def eliminar(self, correo):
            try:
                conn = self.con.conectar()
                cursor = conn.cursor()
                self.sql = '''
                DELETE FROM tb_empleados 
                WHERE correo = %s
                '''
                cursor.execute(self.sql, (correo,))
                conn.commit()
                resultado = cursor.rowcount
                cursor.close()
                conn.close()
                return resultado == 1
            except Exception as e:
                print(f"Error al borrar el empleado: {e}")
                return False
    
    def consultar_tabla(self):
        try:
            conn = self.con.conectar()
            cursor = conn.cursor()
            self.sql = '''
            SELECT id, nombre, apellido, correo, edad, direccion, salario
            FROM tb_empleados
            '''
            # Ejecutamos la query con parámetros
            cursor.execute(self.sql)
            # Obtenemos el resultado de la consulta
            resultado = cursor.fetchall()
            cursor.close()
            conn.close()
            return resultado
        except Exception as e:
            print(f"Error al consultar el empleado: {e}")
            return False