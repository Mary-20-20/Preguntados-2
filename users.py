import json
import os

USERS_FILE = "users_data.json"
SESSIONS_FILE = "sessions.json"


# Cargar los datos desde el archivo JSON
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as file:
        return json.load(file)


# Guardar los datos en el archivo JSON
def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file)


# Cargar las sesiones
def load_sessions():
    if not os.path.exists(SESSIONS_FILE):
        # Si no existe el archivo de sesiones, devolvemos un diccionario vacío
        return {}
    with open(SESSIONS_FILE, "r") as file:
        return json.load(file)

def test_load_sessions():
    


# Guardar las sesiones activas en el archivo JSON
def save_sessions(sessions):
    with open(SESSIONS_FILE, "w") as file:
        json.dump(sessions, file)


# Registrar un nuevo usuario si no existe previamente
def registerUser(name, password):
    users = load_users()

    # Verificamos si el nombre de usuario ya está registrado
    if name in users:
        return "El usuario ya está registrado"

    # Creamos un nuevo usuario con la contraseña y un puntaje inicial de 0
    users[name] = {"password": password, "score": 0}
    save_users(users)
    return "Usuario registrado exitosamente"


# Abrir o cerrar la sesión de un usuario
def openCloseSession(name, password, flag):
    users = load_users()
    sessions = load_sessions()

    # Comprobamos que el usuario exista y que la contraseña sea correcta
    if name not in users or users[name]["password"] != password:
        return "Credenciales incorrectas"

    # Si flag es True, abrimos sesión; si es False, la cerramos
    if flag:
        sessions[name] = True
        message = "Sesión abierta exitosamente"
    else:
        if name in sessions:
            del sessions[name]  # Cerrar sesión eliminando del diccionario de sesiones
        message = "Sesión cerrada exitosamente"
    
    save_sessions(sessions)
    return message


# Actualizar el puntaje de un usuario si su sesión está activa
def updateScore(name, password, score):
    users = load_users()
    sessions = load_sessions()

    # Validar credenciales y comprobar que la sesión esté activa
    if name not in users or users[name]["password"] != password or name not in sessions:
        return "Error: no se puede actualizar el puntaje"

    # Actualizamos el puntaje del usuario
    users[name]["score"] = int(score)
    save_users(users)
    return "Puntaje actualizado correctamente"


# Obtener el puntaje de un usuario si su sesión está activa
def getScore(name, password):
    users = load_users()
    sessions = load_sessions()

    # Validar credenciales y comprobar que la sesión esté activa
    if name not in users or users[name]["password"] != password or name not in sessions:
        return "Error: no se puede obtener el puntaje"

    # Devolvemos el puntaje del usuario
    return users[name]["score"]


# Obtener la lista de usuarios conectados (con sesión abierta)
def usersList(name, password):
    users = load_users()
    sessions = load_sessions()

    # Validar credenciales del usuario solicitante
    if name not in users or users[name]["password"] != password or name not in sessions:
        return "Error: acceso no autorizado"

    # Devolvemos una lista de los usuarios que tienen sesión abierta
    connected_users = [
        {"name": u, "score": users[u]["score"]}
        for u in sessions
    ]
    return connected_users


# Generar una pregunta según la categoría seleccionada
def question(name, password, cat):
    users = load_users()
    sessions = load_sessions()

    # Validar credenciales y comprobar que la sesión esté activa
    if name not in users or users[name]["password"] != password or name not in sessions:
        return "Error: no se puede acceder a la pregunta"

    # Diccionario de categorías y preguntas
    categories = {
        "0": "science",
        "1": "history",
    }

    # Verificamos si la categoría existe
    category_name = categories.get(str(cat))  # Convertimos cat a string para prevenir errores
    if not category_name:
        return "Categoría no encontrada"

    # Diccionario de preguntas por categoría
    questions = {
        "science": "¿Cuál es el símbolo químico del agua?",
        "history": "¿Quién fue el primer presidente de los EE.UU.?",
    }

    # Devolvemos la pregunta correspondiente a la categoría solicitada
    return questions.get(category_name, "Pregunta no disponible")
