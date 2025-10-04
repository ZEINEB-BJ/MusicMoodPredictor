# 🎵 MusicMoodPredictor

📌 **Présentation**  
MusicMoodPredictor est un mini-projet Python qui recommande une chanson en fonction de l’humeur de l’utilisateur.  
Il utilise une approche **IA simple** avec `CountVectorizer` et `KNeighborsClassifier` pour analyser le texte et prédire le genre musical adapté.

---

🚀 **Fonctionnalités principales**

👤 **Humeur → Musique**

- L’utilisateur entre son humeur (ex : "heureux", "fatigué", "nostalgique",..).
- L’IA prédit le genre musical correspondant.
- Une chanson réelle est proposée aléatoirement dans ce genre.
- Possibilité d’écouter la chanson directement sur **YouTube**.
- Historique des recommandations sauvegardé dans `historique_vectorizer.txt`.

---

🧱 **Technologies utilisées**

🔧 **Backend / IA**

- Python 3
- scikit-learn (`KNeighborsClassifier`, `CountVectorizer`)
- random (choix aléatoire de la chanson)
- webbrowser (ouvrir YouTube)
- datetime (sauvegarde des historiques)

---

📊 **Cahier de charges**

**Objectifs**

- Recommander une musique adaptée à l’humeur de l’utilisateur
- Démontrer l’utilisation de Machine Learning simple avec scikit-learn
- Gérer des humeurs jamais vues grâce à la vectorisation de texte

**Contraintes**

- Précision des recommandations basée sur un mini dataset
- Sauvegarde correcte de l’historique
- Interface console simple mais interactive

---

⚙️ **Installation & Lancement**

1. Cloner le projet :

```bash
git clone https://github.com/ZEINEB-BJ/MusicMoodPredictor.git
cd MusicMoodPredictor
```

Installer les packages nécessaires :

```bash
pip install scikit-learn
```

Lancer le script :

``bash

python music_predictor_vectorizer.py

```
Suivre les instructions dans la console :

Entrer votre humeur

Recevoir le genre et la suggestion de chanson

Optionnel : écouter la chanson sur YouTube

📄 Exemple d’utilisation

Décris ton humeur actuelle : épuisé
🧠 Analyse de ton humeur : Épuisé
🎵 Genre musical recommandé : Chill
🎶 Suggestion : Ocean Eyes - Billie Eilish
Souhaites-tu écouter cette chanson sur YouTube ? (o/n) : o


**👩‍💻 Auteure**
Zeineb Ben Jeddou – Étudiante en Génie Logiciel
📧 Contact : zeinebbenjeddou01@gmail.com
```
