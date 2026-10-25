from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import secrets

app = Flask(__name__)

# Configuration de Flask-Session
app.config["SECRET_KEY"] = secrets.token_hex()  # Génère une clé aléatoire sécurisée.
app.config["SESSION_PERMANENT"] = False         # Désactive la durée de vie permanente de la session.
app.config["SESSION_TYPE"] = "filesystem"       # Stocke les données de session dans des fichiers sur le serveur.

Session(app)  # Active l'extension Flask-Session.

# Utilisateurs stockés dans le code : email -> nom + mot de passe haché
# Le mot de passe n'est jamais conservé en clair, seulement son hash.
USERS = {
    "mariem@example.com": {
        "name": "mariem",
        "password_hash": generate_password_hash("123456"),
    }
}


@app.route("/")
def index():
    # Si l'utilisateur n'est pas connecté, on le renvoie vers la page de connexion
    if not session.get("name"):
        return redirect("/login")

    return render_template(
        "index.html",
        name=session["name"],
        session_id=session["session_id"]
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("Tous les champs sont obligatoires.")
            return render_template("register.html")

        if email in USERS:
            flash("Cette adresse est déjà enregistrée. Connectez-vous.")
            return redirect("/login")

        # Hachage du mot de passe avant de le stocker
        USERS[email] = {
            "name": name,
            "password_hash": generate_password_hash(password),
        }
        flash("Inscription réussie ! Vous pouvez vous connecter.")
        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = USERS.get(email)

        # Utilisateur inconnu : on l'envoie vers l'inscription
        if user is None:
            flash("Aucun compte avec cette adresse. Veuillez vous inscrire.")
            return redirect("/register")

        # Mot de passe incorrect : on reste sur la page de connexion
        if not check_password_hash(user["password_hash"], password):
            flash("Mot de passe incorrect.")
            return render_template("login.html")

        # Connexion réussie : on repart d'une session propre
        session.clear()
        session["name"] = user["name"]
        session["email"] = email
        session["session_id"] = str(uuid.uuid4())
        return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)