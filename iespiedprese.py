import os
from flask import Flask, send_from_directory
from flask_bcrypt import Bcrypt
from flask_htmlmin import HTMLMIN
from lib.config import SECRET_KEY
from lib.login_manager import init_login_manager
from lib.blueprints import register_blueprints
from lib.helpers import str_to_bool
from dotenv import load_dotenv
from flask_squeeze import Squeeze
from datetime import datetime, timedelta

squeeze = Squeeze()
load_dotenv()
PORT = int(os.getenv('PORT'))
DEBUG = str_to_bool(os.getenv('DEBUG', 'False'))
CACHE_AGE = int(os.getenv('CACHE_AGE'))

def create_app():
    app = Flask(__name__)
    squeeze.init_app(app)
    app.secret_key = SECRET_KEY
    app.config['MINIFY_HTML'] = True
    HTMLMIN(app)
    Bcrypt(app)
    init_login_manager(app)
    register_blueprints(app)

    @app.after_request
    def add_header(response):
        if 'Cache-Control' not in response.headers:
            expires = datetime.utcnow() + timedelta(days=365)
            response.headers['Expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
            response.headers['Cache-Control'] = f'public, max-age={CACHE_AGE}'
        return response

    @app.route('/static/<path:filename>')
    def custom_static(filename):
        response = send_from_directory(app.static_folder, filename)
        expires = datetime.utcnow() + timedelta(days=365)
        response.headers['Expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
        response.headers['Cache-Control'] = f'public, max-age={CACHE_AGE}'
        return response

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)