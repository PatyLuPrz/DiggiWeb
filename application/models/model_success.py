import web
import config 
import firebase_admin


db = config.db

def getRestaurante(email):
    try:
        restruante_ref = db.collection(u'restaurantes')
        docs = restruante_ref.stream()
        for item in docs:
            if item.get('email') == email:
                print("Id del restaurante")
                print(item.id)
                return item.id
            else:
                print("Email no localizado - Restaurante")
                return None
    except Exception as e:
        print( "Error restaurantes: " +str(e.args))
        return None

def getLocal(email):
    try:
        local_ref = db.collection(u'locales')
        docs = local_ref.stream()
        for item in docs:
            if item.get('email') == email:
                print("Id del local")
                print(item.id)
                return item.id
            else:
                print("Email no localizado - Locales")
                return None
    except Exception as e:
        print( "Error locales: " +str(e.args))
        return None

def getUsuario(email):
    try:
        user_ref = db.collection(u'clientes')
        docs = user_ref.stream()
        for item in docs:
            if item.get('email') == email:
                print("Id del cliente")
                print(item.id)
                return item.id
            else:
                print("Email no localizado - Clientes")
                return None
    except Exception as e:
        print( "Error usuarios: " +str(e.args))
        return None

