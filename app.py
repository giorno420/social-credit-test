import os
import json
from flask import Flask, render_template, redirect, url_for
from flask_discord import DiscordOAuth2Session, requires_authorization

config = json.load(open("config.json", "r"))

app = Flask(__name__)

app.secret_key = os.urandom(24)
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = config['insecuretransport']
app.config["DISCORD_CLIENT_ID"] = config['id']
app.config["DISCORD_CLIENT_SECRET"] = config['secret']
app.config["DISCORD_REDIRECT_URI"] = config['redirect_uri']
discord = DiscordOAuth2Session(app)

@app.route('/login')
def login():
    return discord.create_session()


@app.route('/callback')
def callback():
    discord.callback()
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    discord.revoke()
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/socialcredittest')
def socialcredittest():
    return "to be continued"

app.run(debug=True)