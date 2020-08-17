import web
import config 
import firebase_admin
from firebase_admin import firestore

db = config.db


def getRestaurantes():
    try:
        restaurantes_ref = db.collection(u'restaurantes')
        docs = restaurantes_ref.stream()
        restaurantes = []
        diccionario = {}
        result  = docs
        for x in result:
            diccionario = {"id":x.id,"nombre":x.get("nombre"),"direccion":x.get("direccion")}
            restaurantes.append(diccionario)
        return restaurantes
    except Exception as e:
        return "Error getRestaurantes: " + str(e.args)

def getLocales():
    try:
        locales_ref = db.collection(u'locales')
        docs = locales_ref.stream()
        locales = []
        diccionario = {}
        result  = docs
        for x in result:
            diccionario = {"id":x.id,"nombre":x.get("nombre"),"direccion":x.get("direccion")}
            locales.append(diccionario)
        return locales
    except Exception as e:
        return "Error getLocales: " + str(e.args)

def getPlatillos():
    try:
        platillos_ref = db.collection(u'platillos')
        docs = platillos_ref.limit(9).stream()
        return docs
    except Exception as e:
        return "Error getPlatillos: " +str(e.args)
    

def getRestaurantesPlatillos():
    try:
        platillos_ref = db.collection(u'platillos')
        docs = platillos_ref.limit(9).stream()

        nombres = []
        for x in docs:
            uid = x.get("restaurante")
            new_ref = db.collection(u'restaurantes')
            query = new_ref.stream()
            for i in query:
                if i.id == uid:
                    nombres.append(i.get("nombre"))

        return nombres
    except Exception as e:
        return "Error getRestaurantePlatillos " +str(e.args)


def getRestaurantesPlatillosID():
    try:
        platillos_ref = db.collection(u'platillos')
        docs = platillos_ref.limit(9).stream()
        rest_id = []
        for x in docs:
            referencia = str(x.get("restaurante"))
            rest_id.append(referencia)
        return rest_id
    except Exception as e:
        return "Error getRestaurantePlatillos ID : " +str(e.args)

def getProductos():
    try:
        productos_ref = db.collection(u'productos')
        docs = productos_ref.stream()
        return docs
    except Exception as e:
        return "Error getProductos " + str(e.args)

def busqueda(palabra_clave):
    try:
        platillos = getPlatillos()
        locales = getLocales()
        productos = getProductos()
        restaurantes = getRestaurantes()

        lista = []
        for x in platillos:
            if (str(palabra_clave).upper() in str(x.get("nombre")) or str(palabra_clave) in str(x.get("nombre"))):
                lista.append(x)
        for x in locales:
            if (str(palabra_clave).upper() in str(x.get("nombre")) or str(palabra_clave) in str(x.get("nombre"))):
                lista.append(x)
        for x in productos:
            if (str(palabra_clave).upper() in str(x.get("nombre")) or str(palabra_clave) in str(x.get("nombre"))):
                lista.append(x)
        for x in restaurantes:
            if (str(palabra_clave).upper() in str(x.get("nombre")) or str(palabra_clave) in str(x.get("nombre"))):
                lista.append(x)

        return lista
    except Exception as e:
        return "Error model main busqueda: " + str(e.args)



