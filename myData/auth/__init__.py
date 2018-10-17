from flask import Blueprint

bp = Blueprint('auth', __name__)

from myData.auth import routes
