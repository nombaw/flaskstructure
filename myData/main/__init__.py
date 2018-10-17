from flask import Blueprint

bp = Blueprint('main', __name__)
from myData.main import routes, forms