from database.db import get_connection
from .entities.entiNotas import Notas

class NotasModel():
    #Buscar todos
    @classmethod
    def get_notas(self):
        try:
            connection=get_connection()
            notas=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_nota, nombre_nota, fecha_creacion_nota, fecha_edicion_nota, descripcion_nota, ultimo_editor_nota, fk_id_carpeta, panel_nota FROM notas ORDER BY id_nota")
                resultset=cursor.fetchall()

                for row in resultset:
                    nota = Notas(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    notas.append(nota.to_JSON())

            connection.close()
            return notas
        except Exception as ex:
            raise Exception(ex)
    
     #Buscar uno
    @classmethod
    def get_nota(self,id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_nota, nombre_nota, fecha_creacion_nota, fecha_edicion_nota, descripcion_nota, ultimo_editor_nota, fk_id_carpeta, panel_nota FROM notas WHERE id_nota = %s",(id))
                row = cursor.fetchone()

                nota = None
                if row != None:
                        nota = Notas(row[0],row[1],row[2],row[3],row[4], row[5],row[6],row[7])
                        nota = nota.to_JSON()
                    
            connection.close()
            return nota
        except Exception as ex:
            raise Exception(ex)

    # Añadir 
    @classmethod
    def add_nota(self, nota):
        try:
            connection = get_connection()
    
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO notas (nombre_nota, descripcion_nota,fk_id_carpeta) VALUES (%s, %s,%s)""", (nota.name, nota.description,nota.parentFolder))
                
                affected_rows  = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
     # Actualizar
    @classmethod
    def update_nota(self,nota):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("UPDATE notas SET nombre_nota = %s, fecha_creacion_nota = %s, fecha_edicion_nota = %s, descripcion_nota = %s, ultimo_editor_nota = %s , fk_id_carpeta = %s, panel_nota = %s WHERE id_nota = %s",(nota.name, nota.creationDate, nota.updateDate,  nota.description,  nota.lastEditor,  nota.parentFolder, nota.panel, nota.id))
                
                affected_rows  = cursor.rowcount
                connection.commit()
      
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)