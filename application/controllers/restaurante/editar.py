import web
import app
import application.models.model_restaurante as model_restaurante
render = web.template.render('application/views/restaurante/', base="master.html")

class Editar():
    def POST(self,uid):
        try:
            form = web.input()
            if form['Imagen']:
                imagen = model_restaurante.insertImage(form['Imagen'])
                edit = model_restaurante.update(uid,form['Nombre'],form['Descripcion'],imagen,form['Ingredientes_extra'],form['Tiempo_preparacion'])
            else:
                edit = model_restaurante.updateWithoutImage(uid,form['Nombre'],form['Descripcion'],form['Ingredientes_extra'],form['Tiempo_preparacion'])            
            
            if(edit):
                return render.successMessage()
            else:
                return render.failMessage()
        except Exception as e:
            return "Error editar restaurante POST Controller" + str(e.args)

    def GET(self,uid):
        try:
            platillo = model_restaurante.getPlatilloByID(uid)
            return render.editar(platillo)
        except Exception as e:
            return "Error editar restaurante GET controller: " +str(e.args)