import os
from datetime import datetime
from flask import Flask, render_template, jsonify, redirect, url_for, request


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = ['txt', 'cvs']

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/defineData', methods = ['GET', 'POST'])
def defineData():
	dirs = os.listdir(app.config['UPLOAD_FOLDER'])
	return render_template('uploadData.html', files = dirs)	

@app.route('/storeData', methods = [ 'GET', 'POST'])
def guardarData():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			now = datetime.now()
			filename = os.path.join(app.config['UPLOAD_FOLDER'], "%s" % (file.filename))
			file.save(filename)
			return jsonify({"success":True})
		return redirect(url_for('defineData'))
	else:
		return redirect(url_for('home'))

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == '__main__':
   app.run( debug = True)