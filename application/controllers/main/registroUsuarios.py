import web
import app
import application.models.model_usuarios as model_usuarios

render = web.template.render('application/views/main/', base="master.html")

# FIXME: Este es el que no sirve
# FIXME: El GET Funciona bien, el POST solo hace el render xd los insert nel

class RegistroUsuarios():
    def GET(self):
        try:
            print("get registro usuarios")
            return render.registroUsuarios()
        except Exception as e:
            return "Error UsuarioGet Controller" + str(e.args)
    def POST(self):
        try:
            print("post registro usuarios")
            form = web.input() 
            nivel = form["nivel"]
            if (str(nivel) == '0'):
                print("nivel 0")
                raise web.seeother("/registrar/restaurante")
            elif (str(nivel) == '1'):
                print("nivel 1")
                raise web.seeother("/registrar/negocio")
                
            elif (str(nivel) == '2'):
                print("nivel 2")
                raise web.seeother("/registrar/cliente")
            else:
                return "algo fallo"
        except Exception as e:
            return "Error UsuarioPOST Controller" + str(e.args)




