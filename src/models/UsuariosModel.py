from database.db import get_connection
from .entities.Usuarios import Usuarios

class UsuariosModel():

    @classmethod
    def get_usuarios(self):
        try:
            connection=get_connection()
            usuarios=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_usuario, nombres_usuario, apellidos_usuario, correo_usuario, clave_usuario, imagen_usuario FROM usuarios")
                resultset=cursor.fetchall()

                for row in resultset:
                    usuario=Usuarios(row[0],row[1],row[2],row[3],row[4],row[5])
                    usuarios.append(usuario.to_JSON)
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)