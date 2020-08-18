import web
import pyrebase


config = {
  "apiKey":"AIzaSyCRgTvKgLZVLLoeiL6J7lI4O5lwAwXqEVo",
  "authDomain":"diggi-49418.firebaseapp.com",
  "databaseURL":"https://diggi-49418.firebaseio.com",
  "storageBucket":"diggi-49418.appspot.com",
  "serviceAccount":"CuentaServicio.json"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()



 

def registrarUsuarios(correo,contrasena):
    try:
        auth.get_user_by_email(correo)
        return False
    except:
        user = auth.create_user_with_email_and_password(correo, contrasena)
        return True

