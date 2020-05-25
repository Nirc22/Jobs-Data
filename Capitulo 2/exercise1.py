from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = "exercise1"
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
data = []
@app.route("/", methods=["POST"])
def optener_documento():
    file = request.files['file']
    if file.filename == '':
            return 'No selected file'
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        return 'file uploaded successfully'
    else:
        return 'No allowed extension'

@app.route('/options', methods=["GET"])
def show_form_data():
    data 
    return jsonify(data)

if __name__ == '__main__':
    app.run()