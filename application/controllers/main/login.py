import web
import config
import app
from application.models.model_login import verificarUsuarios
from application.models.model_success import getUsuario,getLocal,getRestaurante
render = web.template.render('application/views/main/', base="master.html")

db = config.db
# TODO: Generar login

class Login():
    def GET(self):
        try:
            return render.login()
        except Exception as e:
            return "Error RegistroGet Controller" + str(e.args)
    def POST(self):
        try:
            form = web.input()
            result = verificarUsuarios(form['email'],form['contrasena'])
            if result:
                ref_niveles = db.collection(u'usuarios')
                docs = ref_niveles.stream()
                for item in docs:
                    print("for")
                    if str(item.get("email")) == str(form['email']):
                        print("if")
                        nivel = item.get("nivel")
                        
                        if nivel == '0':
                            print("restaurante")
                            cosa = getRestaurante(form['email'])
                            return render.loginSucess("Restaurante",str(form['email']),cosa)
                        elif nivel == '1':
                            print("negocio")
                            cosa = getLocal(form['email'])
                            return render.loginSucess("Negocio",str(form['email']),cosa)
                        elif nivel == '2':
                            print("cliente")
                            cosa = getUsuario(form['email'])
                            return render.loginSucess("Cliente",str(form['email']),cosa)
                    else:
                        print("no jalo xd")
            else:
                return "algo salio mal :(" 
        except Exception as e:
            return "Error RegistroPost Controller" + str(e.args)



# import web
# import app
# import application.models.model_login as model_login
# render = web.template.render('application/views/main/', base="master.html")

# # TODO: Generar login

# class Login():
#     def GET(self):
#         try:
#             return render.login()
#         except Exception as e:
#             return "Error RegistroGet Controller" + str(e.args)
#     def POST(self):
#         try:
            
#             return render.login()
#             # form = web.input()
#             # correo = form["email"]
#             # password = form["password"]
#             # result = model_login.verificarUsuarios(correo, password)
#             # print(result)
#             # if(result):
#             #     raise  web.seeother("/index")
#             # else:
#             #     return render.registroErroneo()
#         except Exception as e:
#             return "Error RegistroPost Controller" + str(e.args)

