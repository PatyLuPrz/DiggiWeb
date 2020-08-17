import web
import app
import application.models.model_locales as model_locales
render = web.template.render('application/views/locales/', base="master.html")

class Editar():
    def POST(self,uid):
        try:
            form = web.input()
            descripcion = {'cantidad_disponible':form['Cant_disponible'] ,
            'precio': form['Precio'] ,'presentacion': form['Presentacion']}
            marca = form['Marca']
            nombre = form['Nombre']

            if (form['Imagen']):
                imagen = model_locales.insertImage(form['Imagen'])
                insert = model_locales.update(nombre,marca,imagen,descripcion,uid)
            else:
                insert = model_locales.updateWithoutImage(nombre,marca,descripcion,uid)

            if(insert):
                return render.successMesage()
            else:
                return render.failMesage()
        except Exception as e:
            print("Error editar locales POST Controller" + str(e.args))
            return render.failMesage()

    def GET(self,uid):
        try:
            
            producto = model_locales.getProductoByID(uid)
            
            return render.editar(producto)
        except Exception as e:
            print("Error editar locales GET controller: " +str(e.args))
            return render.failMesage()