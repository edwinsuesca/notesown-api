class Notas():

    def __init__(self,nombre_nota,fk_id_carpeta,id_nota=None,fecha_creacion_nota=None,fecha_edicion_nota=None,descripcion_nota=None,ultimo_editor_nota=None,panel_nota=None) -> None:

        self.name = nombre_nota        
        self.parentFolder = fk_id_carpeta
        self.id = id_nota
        self.creationDate = fecha_creacion_nota
        self.updateDate = fecha_edicion_nota
        self.description = descripcion_nota
        self.lastEditor = ultimo_editor_nota
        self.panel = panel_nota
        
    
    def to_JSON(self):
        return{
            'name': self.name,
            'parentFolder': self.parentFolder,
            'id': self.id,
            'creationDate': self.creationDate,
            'updateDate': self.updateDate,
            'description': self.description,
            'lastEditor': self.lastEditor,
            'panel': self.panel,
        }

