#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request
from mongoengine import connect

app = Flask(__name__, template_folder='../templates', static_folder='../templates/layui')
conf_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "config.py")
app.config.from_pyfile(conf_path)
# mongo
connect('test', host=app.config.get('MONGO_CONF'))


def register_blueprint():
    from sites.user.views import user
    from sites.role.views import role
    from sites.person.views import person
    from sites.access.views import access
    app.register_blueprint(user)
    app.register_blueprint(role)
    app.register_blueprint(person)
    app.register_blueprint(access)


@app.route("/")
def index_view():
    return render_template('index.html')


@app.route("/home")
def home_view():
    return render_template('home.html')


@app.route("/role")
def role_view():
    return render_template('role.html')


@app.route("/role_edit")
def role_edit_view():
    role_id = request.args.get('id')
    return render_template('role_edit.html', id=role_id)


@app.route("/person")
def person_view():
    return render_template('person.html')


@app.route("/person_edit")
def person_edit_view():
    role_id = request.args.get('id')
    return render_template('person_edit.html', id=role_id)


@app.route("/access")
def access_view():
    return render_template('access.html')


@app.route("/access_edit")
def access_edit_view():
    role_id = request.args.get('id')
    return render_template('access_edit.html', id=role_id)


register_blueprint()
