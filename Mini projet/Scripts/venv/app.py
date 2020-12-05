from flask import Flask,render_template
#Flask : micro-framework en open source permettant de faire de developpement web en python

app=Flask(__name__)
#déclaration de l'objet

@app.route("/")
#objet.route -> permet de créer un lien afin de naviguer entre les différente page web
def home():
    # retourne la page About
    # render_template: permet d'afficher une page html et de lui retourné des information
    return render_template("About.html")

@app.route("/cv")
#objet.route -> permet de créer un lien afin de naviguer entre les différente page web
def CV():
    # retourne la page CV
    #render_template: permet d'afficher une page html et de lui retourné des information
    return render_template("Cv.html")

@app.route("/contact")
#objet.route -> permet de créer un lien afin de naviguer entre les différente page web
def contact():
    #retourne la page contact
    return "Contact"
if __name__ == "__main__" :
    #port = int(os.environ.get('PORT', 5000))
    #La variable port specifie le port a utilisé lors du lancement de l'application, le port d'utilisation doit être utilisé pour le lancement de l'application sur Heroku
    #server.run(host='0.0.0.0', port=port)
    #permet de lancer lapplication sur heroku le "host=0.0.0.0" permet à heroku de lui donnée une adresse.
    app.run(debug=True)
    #permet de lancer l'application en local sur l'adresse 127.0.0.1.
    #le paramètre debug permet de faire des modification sur les fichiers sans avoir à arrété et relancer le serveur a chaque modification celui-ci n'est pas obligatoire pour le deploiement sur heroku
