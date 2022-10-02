class Carpetas():

    def __init__(self,nombre_carpeta,id_carpeta=None,fecha_creacion_carpeta=None,fecha_edicion_carpeta=None,panel_carpeta=None) -> None:
        self.id = id_carpeta
        self.name = nombre_carpeta        
        self.creationDate = fecha_creacion_carpeta
        self.updateDate = fecha_edicion_carpeta
        self.panel = panel_carpeta
        
    
    def to_JSON(self):
        return{
            'id': self.name,
            'name': self.id,
            'creationDate': self.creationDate,
            'updateDate': self.updateDate,
            'panel': self.panel
        }