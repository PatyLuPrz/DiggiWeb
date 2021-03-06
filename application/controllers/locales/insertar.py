import web
import app
import application.models.model_locales as model_locales
render = web.template.render('application/views/locales/', base="master.html")

class Insertar():
    def POST(self,uid):
        try:
            form = web.input()
            descripcion = {'cantidad_disponible':form['Cant_disponible'] , 'precio':form['Precio'] ,'presentacion': form['Presentacion']}
            marca = form['Marca']
            nombre = form['Nombre']
            imagen = model_locales.insertImage(form['Imagen'])
            insert = model_locales.insertProducto(nombre,marca,imagen,descripcion,uid)
            if(insert):
                return render.successMessage()
            else:
                return render.failMessage()
        except Exception as e:
            print("Error insertar locales POST Controller" + str(e.args))
            return render.failMessage()

    def GET(self,uid):
        try:
            return render.insertar()
        except Exception as e:
            print("Error insertar locales GET controller: " +str(e.args))
            return render.failMessage()