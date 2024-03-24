from flask import Flask, render_template, request, redirect, session, flash, jsonify, url_for
from flask_session import Session  # Import für die Session-Erweiterung

app = Flask(__name__)

# Konfigurationen für automatisches Template-Reload, Sessions und Datenbank
app.config["TEMPLATES_AUTO_RELOAD"] = True
# festgelegt, dass Session nicht dauerhaft ist
app.config["SESSION_PERMANENT"] = False
# Sitzungsinformationen auf dem Dateisystem gespeichert
app.config["SESSION_TYPE"] = "filesystem"
# Geheimer Schlüssel für die Session-Sicherheit (notwendig für die Session-Verwaltung)
Session(app)  # Initialisiert die Session mit der App

@app.route('/')
def home():
    return "Legal Prompt"

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Startet den Server auf Port 5001 mit aktiviertem Debug-Modus
