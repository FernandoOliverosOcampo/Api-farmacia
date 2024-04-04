from librerias import *
from modelo.supabase.keys import *
from modelo.generales import *


class Usuarios():
    
    def traer_datos_usuarios(self, cedula):
        
        try:
            response = supabase.table(tabla_usuarios).select('*').eq( 'cedula', cedula).execute()
            
            if 'error' in response:
                jsonify({"msg": "Error de usuario"}), 401
                
                
            response_data = response.data[0]
            
            return jsonify({
                "id": response_data['id'],
                "nombre": response_data['nombre'],
                "fecha_nacimiento": response_data['fecha_nacimiento'],
                "cedula": response_data['cedula'],
                "celular":response_data['celular'],
                "rol": response_data['rol'],
                "correo": response_data['email'],
                "password": response_data['password']
            })
            
            # return jsonify({ "data": response_data})
        
        except Exception as e:
            return jsonify({"msg": "Error al obtener los datos del usuario: " + str(e)}), 500