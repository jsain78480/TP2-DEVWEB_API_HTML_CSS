#Import du FRAMEWORK Flask pour créer un serveur local pour tester notre API
from flask import Flask, request, jsonify 
from flask_cors import CORS

app = Flask(__name__)
cors=CORS(app)

#Page principal quand on va arriver sur l'url basique
#La fonction le_truc_marche va renvoyer au format JSON "welcome to my movies API" 
@app.route('/')
def le_truc_marche():
        return jsonify({
                "msg":" Welcome to my movies API"
        })

#Nous avons choisi de faire une liste de films pour ce TP avec un id, un nom, un genre, une annee de sortie, un nom de réalisateur et une image du film
liste_de_films = [
        {
                "id":1,
                "name":"Star Wars 1",
                "genre":"Science fiction",
                "annee de sortie":"1999",
                "nom réalisateur":"George Lucas",
                "imgUrl": "https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.wikia.nocookie.net%2Ffrstarwars%2Fimages%2Fe%2Fe0%2FLundi.png%2Frevision%2Flatest%3Fcb%3D20151011153017&tbnid=kudTWU1ClF4ZoM&vet=12ahUKEwi8tOn-wIGCAxXhuycCHc5AAd4QMygAegQIARBz..i&imgrefurl=https%3A%2F%2Fstarwars.fandom.com%2Ffr%2Fwiki%2FStar_Wars_%25C3%25A9pisode_I_%3A_La_Menace_Fant%25C3%25B4me&docid=6Yy4kChGzCi0cM&w=1230&h=1845&q=star%20wars%201&ved=2ahUKEwi8tOn-wIGCAxXhuycCHc5AAd4QMygAegQIARBz"
        },
        {
                "id":2,
                "name":"Die Hard 1 piege de cristal",
                "genre":"Action",
                "annee de sortie":"1988",
                "nom réalisateur":"John McTiernan",
                "imgUrl":"https://m.media-amazon.com/images/M/MV5BZjRlNDUxZjAtOGQ4OC00OTNlLTgxNmQtYTBmMDgwZmNmNjkxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"
        },
        {
                "id":3,
                "name":"La colline a des yeux 1",
                "genre":"Horreur",
                "annee de sortie":"1977",
                "nom réalisateur":"Alexandre Aja",
                "imgUrl": "https://fr.web.img3.acsta.net/pictures/16/10/18/14/19/345735.jpg"
        },
        {
                "id":4,
                "name":"Mission impossible 1",
                "genre":"Action",
                "annee de sortie":"1996",
                "nom réalisateur":"Brian De Palma",
                "imgUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiwT_xH1G_sQ0hxbs1XUqRte2zPfBxMtQ9sw&usqp=CAU"
        },
        {
                "id":5,
                "name":"Spiderman 1",
                "genre":"Science fiction",
                "annee de sortie":"2002",
                "nom réalisateur":"Ruben Fleisher",
                "imgUrl": "https://static.wikia.nocookie.net/ultimatepopculture/images/f/f3/Spider-Man2002Poster.jpg/revision/latest?cb=20190325154328"
        },
        {
                "id": 6,
                "name": "Inception",
                "genre": "Science fiction",
                "annee de sortie": "2010",
                "nom réalisateur": "Christopher Nolan",
                "imgUrl": "https://www.imdb.com/title/tt1375666/mediaviewer/rm2552295424/"
        },
        {
                "id": 7,
                "name": "Pulp Fiction",
                "genre": "Crime",
                "annee de sortie": "1994",
                "nom réalisateur": "Quentin Tarantino",
                "imgUrl": "https://www.imdb.com/title/tt0110912/mediaviewer/rm1298794496/"
        },
        {
                "id": 8,
                "name": "The Shawshank Redemption",
                "genre": "Drama",
                "annee de sortie": "1994",
                "nom réalisateur": "Frank Darabont",
                "imgUrl": "https://www.imdb.com/title/tt0111161/mediaviewer/rm1263800064/"
        },
        {
                "id": 9,
                "name": "The Godfather",
                "genre": "Crime",
                "annee de sortie": "1972",
                "nom réalisateur": "Francis Ford Coppola",
                "imgUrl": "https://www.imdb.com/title/tt0068646/mediaviewer/rm2111778048/"
        },
        {
                "id": 10,
                "name": "The Matrix",
                "genre": "Science fiction",
                "annee de sortie": "1999",
                "nom réalisateur": "The Wachowskis",
                "imgUrl": "https://www.imdb.com/title/tt0133093/mediaviewer/rm3897824000/"
        },
        {
                "id": 11,
                "name": "Gladiator",
                "genre": "Action",
                "annee de sortie": "2000",
                "nom réalisateur": "Ridley Scott",
                "imgUrl": "https://www.imdb.com/title/tt0172495/mediaviewer/rm4262548224/"
        },
        {
                "id": 12,
                "name": "The Dark Knight",
                "genre": "Action",
                "annee de sortie": "2008",
                "nom réalisateur": "Christopher Nolan",
                "imgUrl": "https://www.imdb.com/title/tt0468569/mediaviewer/rm2061867520/"
        },
        {
                "id": 13,
                "name": "Fight Club",
                "genre": "Drama",
                "annee de sortie": "1999",
                "nom réalisateur": "David Fincher",
                "imgUrl": "https://www.imdb.com/title/tt0137523/mediaviewer/rm2861990400/"
        },
        {
                "id": 14,
                "name": "Forrest Gump",
                "genre": "Drama",
                "annee de sortie": "1994",
                "nom réalisateur": "Robert Zemeckis",
                "imgUrl": "https://www.imdb.com/title/tt0109830/mediaviewer/rm4160741120/"
        },
        {
                "id": 15,
                "name": "Avatar",
                "genre": "Science fiction",
                "annee de sortie": "2009",
                "nom réalisateur": "James Cameron",
                "imgUrl": "https://www.imdb.com/title/tt0499549/mediaviewer/rm3655705088/"
        }
]

#On définit tout d'abord un nouveau chemin en disant qu'on va pouvoir utiliser les méthodes GET et POST sur cet url
#La méthode GET va renvoyer en JSON la liste de films
#La méthode POST définit en else va nous permettre d'ajouter de nouveaux films 
@app.route('/api/films',methods=["GET","POST"] )
def films():
        if request.method =='GET' :
            return jsonify({
                "Films": liste_de_films
        })
        else :
            new_film ={
                  "id" : len(liste_de_films)+1,
                  "name": request.json['name'],
                  "genre": request.json['genre'],
                  "annee de sortie":request.json['annee de sortie'],
                  "nom réalisateur":request.json['nom réalisateur'],
                  "imgUrl": request.json['imgUrl']
            }
            print(new_film)
            liste_de_films.append(new_film)
            return jsonify({
                "res": "post send"
        })

#On a définit un nouveau chemin en fonction de l'id pour les méthodes GET, PUT et DELETE
#La méthode GET va récupérer un seul film à l'id souhaité
#La méthode PUT va permettre de modifier un film à l'id souhaité
#La méthode DELETE va permettre de supprimer un film à l'id souhaité
@app.route('/api/films/<int:id>', methods=["GET","PUT","DELETE"])
def one_film(id):
        if request.method =='GET' :
                for film in liste_de_films :
                        if film['id'] == id: 
                                return jsonify({"film": film})
        elif request.method =='PUT': 
               data = request.get_json()
               for film in liste_de_films:
                 if film['id'] == id:
                        film['name'] = data.get('name', film['name'])
                        film['genre'] = data.get('genre', film['genre'])
                        film['annee de sortie'] = data.get('annee de sortie', film['annee de sortie'])
                        film['nom réalisateur'] = data.get('nom réalisateur', film['nom réalisateur'])
                        film['imgUrl'] = data.get('imgUrl', film['imgUrl'])
                        return jsonify({"message": "Film mis à jour avec succès"})
               return jsonify({"message": "Film non trouvé"})
        elif request.method =='DELETE' :
               for film in liste_de_films:
                 if film['id'] == id:
                        liste_de_films.remove(film)
                        return jsonify({"message": "Film supprimé avec succès"})
               return jsonify({"message": "Film non trouvé"})

        return jsonify({"message": "Méthode HTTP non gérée"})
               
#app.debug = True permet de prendre en compte les modifications sans devoir relancer le serveur
#app.run permet de lancer notre serveur     
app.debug = True
app.run()

