#coding:utf-8
import json
import socket


class Objetmail:
    def __init__(self,add_src,add_dest,obj_mail,corp_message):
        self.add_src= add_src
        self.add_dest = add_dest
        self.obj_mail = obj_mail
        self.corp_message = corp_message

host= '192.168.10.3'
port = 39938


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation du socket
try:
    #connexion du client au serveur et echange entre eux
    client.connect((host, port))  
    data = client.recv(1024)
    data = data.decode("utf8")
    print(data)

    Info = []  # liste qui contiendra les informations sur le client
    nom = input("Entrer votre nom svp :")
    passwd = input("Entrer votre mot de passse:")
    mail = input("Entrer votre addresse mail :")
    
    Info.append(nom)
    Info.append(passwd)
    Info.append(mail)
    
    infoEnv = json.dumps(Info)
    infoEnv = infoEnv.encode("utf8")
    client.sendall(infoEnv)

    data = client.recv(1024)
    data = data.decode("utf8")
    print(data)

except Exception as e:
    print(e)
finally:
    client.close()

