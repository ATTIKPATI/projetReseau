#!bin/bash
[ $1 -eq 0]; then
    sudo wget https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz && tar xvf 1.5.2.tar.gz && sudo cd iRedMail-1.5.2 && sudo chmod +x iRedMail.sh && sudo bash iRedMail.sh 
else
    exit
fi
#sudo wget https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz : commande pour télécharger en ligne le dossier tar de iredmail
# tar xvf 1.5.2.tar.gz : decompresser le dossier
#sudo cd iRedMail-1.5.2 : entrer dans le dossier iredmail
#sudo chmod +x iRedMail.sh : donner le droit d'execution
#sudo bash iRedMail.sh : exécuter les fichier .sh