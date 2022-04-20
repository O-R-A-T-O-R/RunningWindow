from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

"""

Example of command for victim

{
    id : int | str,
    command : str
}

"""

@app.route('/')
def main():
    return '<h1>WELCOME TO THE BOTNET API</h1>'

def export_app():
    return app