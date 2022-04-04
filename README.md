# projetReseau
Projet_Reseau

Ce projet a pour but de mettre en place un dispositif permettant d'analyser un packet et de mettre en évidence la compréhension de l'encapsulation des données et l'utilisation des bibliothèques adéquates.
 Notre environnement de travail etait constituer de 03 machines machines virtuelles:
Ces trois machines etaient repartis sur deux machines physiques differentes
Sur les deux machines physiques nous avons utiliser VirtualBox pour heberger nos machines virtuelles.

Sur la premiere machine physique nous avions installé  la machine serveur sur laquelle les configuration du DHCP, DNS, le serveur de base de donnees MysQl et le serveur de messagerie IredMail ont ete effectue.Sur cette meme machine nous avons aussi installe la machine client qui communique avec le serveur et sur laquelle nous avons ecrit les scripts python.

La deuxieme machine physique a heberge la machine client faisant office du Man In the Middle.
 
Informations relatives a l’execution des scripts:
Des scripts .sh pour les dépendances mysql et iredmail: 
INSTALL_MYSQL_DEPENPENCIES.SH: on démarre avec ./install_mysql.sh 
INSTALL_IREMAIL_DEPENPENCES.SH: on démarre avec ./iredmail_iredmail_dependencies.sh
Des scripts python dont server.py, client.py 
