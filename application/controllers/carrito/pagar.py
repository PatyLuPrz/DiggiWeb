import web
import app
import application.models.model_main as model_main
render = web.template.render('application/views/carrito/', base="master.html")


class Pagar():
    def GET(self):
        try:
            return render.pagar()
        except Exception as e:
            return "Error Pagar Controller" + str(e.args) 

    def POST(self):
        try:
            return render.pagar()
        except Exception as e:
            return "Error Pagar Controller POST: " + str(e.args)

