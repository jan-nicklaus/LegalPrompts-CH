from flask import Flask, render_template, request, redirect, session, flash, jsonify, url_for
from flask_session import Session
import requests
import json
from bs4 import BeautifulSoup
from fetch import *
app = Flask(__name__, template_folder='frontend')  # den template_folder auf den frontend Ordner setzen!
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)  # Initialisiert die Session mit der App
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/GetDecText')
def GetDecText():
    query_term = request.args.get("fundstelle")
    url = query_entscheidsuche(query_term)
    text = fetch_and_parse_html(url) if url else "No results found for your query."
    return text
if __name__ == "__main__":
    app.run(debug=True, port=5001)