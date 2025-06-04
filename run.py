# run.py

import os
from flask import Flask
from app.routes import main

# Tell Flask where to find the templates folder inside app/
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'app', 'templates'))
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
