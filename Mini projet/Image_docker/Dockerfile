FROM python:3.8

# le dossier /code sera le dossier courant du container
WORKDIR /code

# Copie du fichier dans le container 
COPY requirements.txt .

# installation des bibliothéques spécifié dans le fichier 
RUN pip install -r requirements.txt

# Copie du contenu du dossier 'src' dans le container
COPY src/ .

# commande a executer au lancement du container 
CMD [ "python", "./app.py" ] 