#coding:utf-8
import json
import mysql.connector as MC
import socket


"""
faire la connexion à la base de donnée et vérifier si elle a réussi
"""
def ConnexionBd():
    
    try:
        connexion = MC.connect(host='localhost', database='python', user='root', password='root')
        curseur = connexion.cursor()
        req = "select * from user"
        curseur.execute(req)
        resultat = curseur.fetchall()
        return resultat
    except MC.Error as err:
        print(err)
    finally:
        connexion.close()


host= ''
port = 39938 # port d'écoute du serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creation de socket
 #demarrage du serveur       
server.bind((host, port))
print("Demarrage de server....")
"""
si le serveur arrive à écouter le client , il lui demande 
d'entrer ses informations
"""
while True:
    server.listen(5) 
    conn, addr = server.accept()

    #Demander au client d'entrer les informations
    infoEnv = f"Please verify your login information"
    infoEnv = infoEnv.encode("utf8")
    conn.sendall(infoEnv)
    print("En cours ....")

    
    infoRec = conn.recv(1024)  
    infoRec  = infoRec.decode("utf8")
    data = json.loads(infoRec)

    #verrifier si les informations sont correctes : si oui donc
    #on envoie un message de réussite de connexion , sinon un message d'erreur
    info = VerificationInfoBd()
    for element in info:
        if element[2] == data[1] and element[3]== data[2]:
            
            infoEnv1 = f"successful connexion"
            infoEnv1  = infoEnv1 .encode("utf8")
            conn.sendall(infoEnv1)
        else:
            
            infoEnv1  = f"wrong information"
            infoEnv1  = infoEnv1 .encode("utf8")
            conn.sendall(infoEnv1 )

conn.close()
server.close()


