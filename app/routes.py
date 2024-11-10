from app import app

from flask import render_template, request, redirect


@app.route("/", methods=['GET'])
@app.route("/login", methods=['GET'])
def index():
    return render_template('login.html')


@app.route("/auth", methods=['POST'])
def login():
    form = request.form
    print(form)
    return redirect(request.referrer or request.host_url)
