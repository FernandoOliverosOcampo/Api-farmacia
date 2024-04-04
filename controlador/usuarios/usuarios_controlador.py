from modelo.usuarios.modelo_usuarios import *

mod_usuario = Usuarios()
 
class controlador_usuario():
    
    def info_usuario(self, cedula):
        query = mod_usuario.traer_datos_usuarios(cedula)
        return query