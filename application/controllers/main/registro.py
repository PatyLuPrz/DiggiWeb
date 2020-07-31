import web
import app
import application.models.model_registro as model_registro
render = web.template.render('application/views/main/', base="master.html")

# TODO: Este es el registro para la autenticacion con correo y contraseña :B

class Registro():
    def GET(self):
        try:
            return render.registro()
        except Exception as e:
            return "Error RegistroGet Controller" + str(e.args)
    def POST(self):
        try:
            print("post registro de usuario")
            form = web.input()
            correo = form["email"]
            contrasena = form["contrasena"]
            result = model_registro.registrarUsuarios(correo,contrasena)
            print(result)
            if(result):
                raise  web.seeother("/usuarios")
            else:
                return render.registroErroneo()
        except Exception as e:
            print( "Error RegistroPost Controller" + str(e.args))
            return render.registroErroneo()
            




