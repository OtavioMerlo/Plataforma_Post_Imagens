from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///bancodados.db"
app.config["SECRET_KEY"] = "0570ddb44902c6c863f5322ba0d3cd0884890e021c904061c60d3faacef16c291531c1e0b0cd0b5fac41c673c4b5ff4d9b03"
app.config["UPLOAD_FOLDER"] = "static/fotos_post"
database=SQLAlchemy(app)

bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="homepage"

from app_site import routes