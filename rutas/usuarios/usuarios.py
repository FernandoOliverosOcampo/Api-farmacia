from librerias import *
from controlador.usuarios.usuarios_controlador import *

con_usuario = controlador_usuario()

traer_info_usuario = Blueprint('traer_info_usuario', __name__)


@traer_info_usuario.route('/info-usuarios/<cedula>', methods= ['GET'])
@cross_origin()
def traer_info_usuarios(cedula):
    return con_usuario.info_usuario(cedula)