import web
import firebase_admin
import application.models.model_success
render = web.template.render('application/views/main/', base="master.html")
class LoginSuccess:
    def GET(self,email):
        try:
            
            return "GET"
        except Exception as e:
            return "Error RegistroGet Controller" + str(e.args)
    def POST(self,email):
        try:
            return "POST"
        except Exception as e:
            return "Error RegistroGet Controller" + str(e.args)
