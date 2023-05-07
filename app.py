from flask import (
    Flask,
    Response,
    render_template,
    session,
    request,
    redirect,
    url_for,
)
import os

import werkzeug


# インスタンスの作成
app = Flask(__name__)

key: bytes = os.urandom(21)
app.secret_key = key
id_pwd: dict[str, str] = {"hoge": "hogehoge"}


@app.route("/")
def index() -> str | werkzeug.Response:
    if not session.get("login"):
        return redirect(url_for("login"))
    else:
        return render_template("index.html")


@app.route("/login")
def login() -> str:
    return render_template("login.html")


@app.route("/logincheck", methods=["POST"])
def logincheck() -> werkzeug.Response:
    user_id: str = request.form["user_id"]
    password: str = request.form["password"]

    if (user_id in id_pwd) and (password == id_pwd[user_id]):
        session["login"] = True
    else:
        session["login"] = False

    if session["login"]:
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout() -> werkzeug.Response:
    session.pop("login", None)
    return redirect(url_for("index"))
