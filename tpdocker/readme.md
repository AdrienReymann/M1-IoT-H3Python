La commande Run lance un contenue a partir d'une image 
La commande  exec permet d'executé une commande dans un conteneur
La commande Build créer une image à partir d'un fichier dockerfile
La commande "docker ps" liste les container
La commande "docker stop" arrete un container
La commande "docker images" liste la totalité des images build
Le requierements.txt sert a indiqué les paquet pour d'installer les paquets requis

docker build tpdocker -t <NomImage> . -> permet de build l'image

exposition port: 

docker run -d -p 127.0.0.1:5001:5002 myimage   -> permet de changer l'ip de liaison et de plus avoir le http://0.0.0.0

Ensuite taper url 127.0.0.1:5000 pour avoir accès a l'app.

