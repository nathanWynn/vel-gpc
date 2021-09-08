import os
import logging
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__) 


UPLOAD_FOLDER = '.'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/') 
def main(): 
        return 'VEL-GPC' 
         
@app.route('/worldmap', methods = ['GET', 'POST'])
def upload_worldmap():
        if request.method == 'POST':
                f = request.files['file']
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return 'Uploading file'
        if request.method == 'GET':
                return 'get file'
    
@app.route('/download', methods = ['GET', 'POST'])    
def download_worldmap():
    if request.method == 'GET':
        return send_file('./worldmap', as_attachment=True)


if __name__ == '__main__': 
    app.run(port=5000, debug=True)  
        
