from flask import Flask, request, url_for, render_template, flash, session, g, jsonify
from werkzeug.utils import secure_filename
from viewhelper import *

import config
import os

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    error = None
    if request.method == 'POST':
        g.file = request.files['file']
        if g.file.content_type == 'text/plain':
            filepath = os.path.join(config.Config.UPLOAD_DIR, secure_filename(g.file.filename))
            g.file.save(filepath)
            flash('file upload success')
        else:
            error = 'only text/plain support'
    elif request.method == 'GET':
        g.file = None
    
    return render_template('upload.html', error=error)

@app.route('/view', methods=['GET'])
def view():
    if request.method == 'GET':
        filedir = config.Config.UPLOAD_DIR
        filelist = os.listdir(filedir)
        filename = request.args.get('file')
        cityinfo = None
        if filename is not None:    
            cityinfo = get_cityinfo(filedir, filename)    # cityinfo as tuple
        return render_template('view.html', filelist=filelist, filename=filename, cityinfo=cityinfo)


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == "__main__":
    app.debug = True
    app.config.from_object(config.Config)
    
    app.run(host='0.0.0.0', port=1337)