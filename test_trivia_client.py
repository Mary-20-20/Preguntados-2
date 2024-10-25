import trivia_client

# Intenta registrar un usuario
name="brandon"
categoria="1"
password="1529"
url="http://192.168.40.3:80"
print(trivia_client.registerUser(url,name,password))


# Inicia sesión con usuario
print(trivia_client.openSession(url,name,password))

# Actualiza puntaje del usuario
score=129
print(trivia_client.updateScore(url,name,password,score))

# Obtiene puntaje del usuario
print(trivia_client.getScore(url,name,password))

# Obtiene lista de usuarios conectados
print(trivia_client.getList(url,name,password))

# Obtiene pregunta de la categoría 0
cat = 1
question = trivia_client.getQuestion(url, name, password, cat)
print(question)

# Cierra sesión con usuario
print(trivia_client.closeSession(url,name,password))