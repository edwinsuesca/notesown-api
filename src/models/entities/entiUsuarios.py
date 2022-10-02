class Usuarios():

    def __init__(self,nombres_usuario,apellidos_usuario,correo_usuario,clave_usuario,imagen_usuario,id_usuario=None) -> None:
        self.id = id_usuario
        self.name = nombres_usuario
        self.lastname = apellidos_usuario
        self.email = correo_usuario
        self.passw = clave_usuario
        self.img = imagen_usuario
    
    def to_JSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname,
            'email': self.email,
            'passw': self.passw,
            'img': self.img,
        }