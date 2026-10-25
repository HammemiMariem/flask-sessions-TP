# Les sessions avec Flask

**TP du cours « Framework web Python »**

Petite application web Flask réalisée dans le cadre d'un TP de la matière *Framework web Python*. Elle illustre la gestion des sessions : inscription, connexion avec mot de passe haché, et page d'accueil affichant le nom de l'utilisateur et son ID de session.

## Objectifs du TP

- Comprendre le fonctionnement des sessions avec Flask et Flask-Session
- Mettre en place un système d'inscription et de connexion
- Hacher les mots de passe au lieu de les stocker en clair
- Utiliser les templates Jinja2 (héritage avec `layout.html`)

## Fonctionnalités

- Inscription avec nom, adresse e-mail et mot de passe
- Mot de passe haché avec Werkzeug (jamais stocké en clair)
- Connexion : un utilisateur non inscrit est redirigé vers la page d'inscription
- Page d'accueil avec message de bienvenue, nom et ID de session
- Déconnexion (suppression de la session)
- Sessions stockées côté serveur avec Flask-Session

## Installation

1. Cloner le dépôt :
   ```powershell
   git clone https://github.com/VOTRE-NOM/NOM-DU-DEPOT.git
   cd NOM-DU-DEPOT
   ```

2. Créer et activer l'environnement virtuel :
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Installer les dépendances :
   ```powershell
   pip install -r requirements.txt
   ```

4. Lancer l'application :
   ```powershell
   python app.py
   ```

5. Ouvrir <http://127.0.0.1:5000> dans le navigateur.

## Structure du projet

```
Session/
├── app.py              # Routes et logique de l'application
├── requirements.txt    # Dépendances Python
└── Templates/
    ├── layout.html     # Structure commune des pages
    ├── index.html      # Page d'accueil (nom + ID de session)
    ├── login.html      # Formulaire de connexion
    └── register.html   # Formulaire d'inscription
```

## Routes

| Route | Méthodes | Description |
|-------|----------|-------------|
| `/` | GET | Accueil (redirige vers `/login` si non connecté) |
| `/register` | GET, POST | Inscription |
| `/login` | GET, POST | Connexion |
| `/logout` | GET | Déconnexion |

## Remarques

- Les utilisateurs sont stockés dans un dictionnaire Python (`USERS`) dans `app.py` : les comptes créés via `/register` sont perdus à l'arrêt du serveur.
- Projet à but pédagogique : ne pas l'utiliser tel quel en production.
