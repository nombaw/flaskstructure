from myData import db
from flask import render_template, Blueprint
from myData.errors import bp


@bp.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'),404


@bp.errorhandler(500)
def server_error(error):
    db.session.rollback()
    return render_template('errors/500.html'),500