import web
import config
import firebase_admin
import cloudinary.uploader

db = config.db

cloudinary.config( 
  cloud_name = "patyluprz", 
  api_key = "448467956332495", 
  api_secret = "iovK969N-ZReTDBMukFZp8JKrq0" 
)

def insertFoto(image):
    try:
        result = cloudinary.uploader.upload(image)
        return result['secure_url']
    except Exception as e:
        print("error insertImage: " +str(e.args))
        return False


def insertarRestaurante(nombre,telefono,direccion,email,foto):
    try:
        doc_ref = db.collection(u'restaurantes').document() 
        doc_ref.set({
            u'direccion': direccion,
            u'foto': u'default.jpg',
            u'nombre': nombre,
            u'telefono': telefono,
            u'email': email,
            u'foto':foto
        }) 
        return True
    except Exception as e:
        print("error model insertar restaurante" + str(e.args))
        return False
        

def insertarNegocio(nombre,telefono,direccion,email,foto):
    try:
        doc_ref = db.collection(u'locales').document() 
        doc_ref.set({
            u'direccion': direccion,
            u'foto': u'default.jpg',
            u'nombre': nombre,
            u'telefono': telefono,
            u'email': email,
            u'foto':foto
        }) 
        return True
    except Exception as e:
        print("error model insertar local" + str(e.args))
        return False
        
    

def insertarCliente(nombre,telefono,direccion,email,foto):
    try:
        doc_ref = db.collection(u'clientes').document() 
        doc_ref.set({
            u'direccion': direccion,
            u'foto': u'default.jpg',
            u'nombre': nombre,
            u'telefono': telefono,
            u'email': email,
            u'foto':foto
        }) 
        return True
    except Exception as e:
        print("error model insertar cliente" + str(e.args))
        return False
        
