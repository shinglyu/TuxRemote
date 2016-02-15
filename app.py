#!venv/bin/python
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('web', 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
      # send_static_file will guess the correct MIME type
        return send_from_directory('web', path)

@app.route('/do/open-mozilla')
def openmozilla():
    os.system('firefox https://www.mozilla.org')
    return "Opening mozilla.org in Firefox"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    #app.run(debug=True)
