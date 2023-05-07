from flask import Flask, render_template, session, request, redirect, url_for
import os

# インスタンスの作成
app = Flask(__name__)

key = os.urandom(21)
app.secret_key = key
id_pwd = {"hoge": "hogehoge"}


@app.route("/")
def index():
    return "Hello Flask"


@app.route("/login")
def login():
    return render_template("login.html")
