from flask import Blueprint

bp = Blueprint('errors', __name__)

from myData.errors import handlers
