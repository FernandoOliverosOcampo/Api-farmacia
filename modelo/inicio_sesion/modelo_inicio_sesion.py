from librerias import *
from modelo.supabase.keys import *
from modelo.generales import *

class modeloIniciarSesion():
    
    def iniciar_sesion(self):
        
        usuario = request.json.get('usuario')
        contrasena = request.json.get('contrasena')
        
        # nombre_tabla = 'Tabla_usuarios'
        response = supabase.table('TABLA_USUARIOS').select('rol','cedula').eq('usuario', usuario).eq('contrasena', contrasena).execute()
        
        if (len(response.data) == 0 ):
            return jsonify({"msg": "Credenciales inválidas"}), 401
        
        cedula = response.data[0]['cedula']
        rol = response.data[0]['rol']
        access_token = create_access_token(identity = usuario)
            
        return jsonify({"access_token": access_token, "acceso": "AUTORIZADO", "cedula": cedula, "rol": rol}), 200
            