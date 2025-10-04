from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
import random
import webbrowser
import urllib.parse
from datetime import datetime


data = [
    ["heureux", "Pop"], ["motivé", "Rap"], ["dynamique", "Rock"],
    ["fatigué", "Chill"], ["calme", "Classique"], ["nostalgique", "Jazz"],
    ["stressé", "Ambient"], ["triste", "Blues"], ["amoureux", "Slow"],
    ["joyeux", "Pop"], ["angoissé", "Instrumental"], ["énergique", "Dance"],
    ["zen", "Classique"], ["déprimé", "Blues"], ["rêveur", "Lofi"],
    ["concentré", "Lofi"], ["relaxé", "Chill"], ["excité", "Electro"],
    ["posé", "Classique"], ["heureuse", "Pop"], ["motivante", "Rap"]
]

# séparer les données
X = [d[0] for d in data]  # les humeurs
y = [d[1] for d in data]  # les genres

# transformer le texte en vecteurs
vectorizer = CountVectorizer()
X_vect = vectorizer.fit_transform(X)

#modèle KNN 
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_vect, y)


chansons = {
    "Pop": ["Happy - Pharrell Williams", "Levitating - Dua Lipa", "Can't Stop the Feeling - Justin Timberlake"],
    "Rap": ["Lose Yourself - Eminem", "SICKO MODE - Travis Scott", "God’s Plan - Drake"],
    "Rock": ["Bohemian Rhapsody - Queen", "Smells Like Teen Spirit - Nirvana", "Sweet Child O' Mine - Guns N' Roses"],
    "Classique": ["Clair de Lune - Debussy", "Canon in D - Pachelbel", "Moonlight Sonata - Beethoven"],
    "Jazz": ["Feeling Good - Nina Simone", "Take Five - Dave Brubeck", "What a Wonderful World - Louis Armstrong"],
    "Blues": ["The Thrill Is Gone - B.B. King", "I'd Rather Go Blind - Etta James", "Crossroads - Eric Clapton"],
    "Chill": ["Sunset Lover - Petit Biscuit", "Weightless - Marconi Union", "Ocean Eyes - Billie Eilish"],
    "Lofi": ["Dreaming - Kupla", "Snowman - WYS", "Coffee Breath - Sofia Mills"],
    "Slow": ["All of Me - John Legend", "Perfect - Ed Sheeran", "I Will Always Love You - Whitney Houston"],
    "Ambient": ["Resonance - HOME", "Night Owl - Galimatias", "An Ending - Brian Eno"],
    "Instrumental": ["Time - Hans Zimmer", "Experience - Ludovico Einaudi", "Comptine d’un autre été - Yann Tiersen"],
    "Electro": ["Animals - Martin Garrix", "Levels - Avicii", "Lean On - Major Lazer"]
}


def ouvrir_musique(chanson):
    query = urllib.parse.quote(chanson)
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# sauvegarder l’historique 
def sauvegarder_historique(humeur, genre, chanson):
    moment = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne = f"[{moment}] Humeur: {humeur} | Genre: {genre} | Chanson: {chanson}\n"
    with open("historique_vectorizer.txt", "a", encoding="utf-8") as f:
        f.write(ligne)

# PP
humeur_input = input("Décris ton humeur actuelle : ").lower()

X_input = vectorizer.transform([humeur_input]) # transformer l'entrée utilisateur en vecteur

genre_pred = model.predict(X_input)[0]


chanson = random.choice(chansons.get(genre_pred, ["Aucune chanson disponible"]))


print("\n🧠 Analyse de ton humeur :", humeur_input.capitalize())
print("🎵 Genre musical recommandé :", genre_pred)
print("🎶 Suggestion :", chanson)

sauvegarder_historique(humeur_input, genre_pred, chanson)


choix = input("\nSouhaites-tu écouter cette chanson sur YouTube ? (o/n) : ").lower()
if choix == "o":
    ouvrir_musique(chanson)
else:
    print(" D’accord, à une prochaine session musicale ! ")
