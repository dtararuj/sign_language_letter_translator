import numpy as np
from tensorflow.keras import models
import cv2
import os
from flask import Flask, render_template, request, redirect, flash, url_for, Response
from werkzeug.utils import secure_filename



#define our paths
path_parent =os.getcwd()
#from preprocessing.dane import *
model_path = os.path.join(path_parent,'model_dt/model_dt.h5')
UPLOAD_FOLDER = os.path.join(path_parent, 'static/images')

#define our dictionary
#slownik zwracajacy nam przypisanie klasy do litery
slownik = {0: "A",
           1: "B",
           2: "C",
           3: "D",
           4: "E",
           5: "F",
           6: "G",
           7: "H",
           8: "I",
           9: "K",
           10: "L",
           11: "M",
           12: "N",
           13: "O",
           14: "P",
           15: "Q",
           16: "R",
           17: "S",
           18: "T",
           19: "U",
           20: "V",
           21: "W",
           22: "X",
           23: "Y"
          } 


# load our defined model
model = models.load_model(model_path)

# Instatiate flask app  
app = Flask(__name__, template_folder='./templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

# render out template
@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# upload image used in prediction and push forward to predict section
@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect('/predict')

# create our predictions 
@app.route('/predict', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        # here we'r loading uploaded photo from temporary folder
        file1 = request.files['file']
        filename1 = file1.filename
        file_path = (os.path.join(app.config['UPLOAD_FOLDER'], filename1))
        file1.save(file_path)
        
        new_photo =cv2.imread(file_path,cv2.IMREAD_UNCHANGED)

        # due to model definition we need to save photo in grayscale
        gray = cv2.cvtColor(new_photo, cv2.COLOR_BGR2GRAY)

        # our photo need to be scaled to format 28 x 28
        dim = (28, 28)

        resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)

        # last step is to resize your photo to specific shape, which is specific for model input layer
        resized1 = resized.reshape(-1,28,28,1)

        # prediction our uploaded photo
        prediction  = model.predict(resized1).argmax(axis = 1)

        output = slownik[prediction[0]]
        return render_template('index.html', prediction_text="This letter is {}".format(output),user_image = os.path.join("static\images",filename1))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False)