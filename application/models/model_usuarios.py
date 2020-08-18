import web
import config


db = config.db

def insertUsuario(email,nivel):
    try:
        usuarios_ref = db.collection(u'usuarios').document() 
        usuarios_ref.set({
            u'email': email,
            u'nivel': nivel,
        })
        return True
    except Exception as e:
        print( "Error Model insertUsuarios: "+str(e.args))
        return False
