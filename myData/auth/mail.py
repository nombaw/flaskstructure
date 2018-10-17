from flask import render_template, current_app
from myData.mail import send_email


def send_password_reset_email(user):
    token = user.get_reset_password()
    send_email('[Myblog] Reset Your Password',
               sender=current_app.config['ADMINS'][1],
               recipients=[user.email],
               text_body=render_template('email/reset_password_request.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
