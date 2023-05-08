# Standard Library
import os
from typing import Any

# Third Party Library
import werkzeug
from flask import Flask, redirect, render_template, request, session, url_for

# First Party Library
from pref_question import pref_location

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


@app.route("/pref_quiz", methods=["POST"])
def pref_quiz() -> str:
    random_perf: str
    city_name: str
    perf_url: str
    random_perf, city_name, perf_url = pref_location()
    session["prefecture"] = random_perf
    session["city"] = city_name
    session["url"] = perf_url
    return render_template("quiz.html", prefecture=random_perf)


@app.route("/answercheck", methods=["POST"])
def answercheck() -> str:
    user_answer: str = request.form["city"]
    prefecture: Any = session.get("prefecture")
    city: Any = session.get("city")
    url: Any = session.get("url")

    if user_answer == city:
        result = "正解!!"
    else:
        result = "残念‼"

    return render_template(
        "result.html", result=result, prefecture=prefecture, city=city, url=url
    )
