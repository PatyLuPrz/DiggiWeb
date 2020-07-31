import web
import app
import application.models.model_contactanos as model_contactanos
render = web.template.render('application/views/main/', base="master.html")

class Index():
    def POST(self):
        try:
            return render.loginSucess()
        except Exception as e:
            return "Error index restaurante POST Controller" + str(e.args)

    def GET(self):
        try:
            return render.loginSucess()
        except Exception as e:
            return "Error index restaurante GET controller: " +str(e.args)