import os
import face_recognition
import cv2
import numpy as np
from flask import Flask, render_template, Response, request, session, redirect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

params = {"local_server": "True",
          "admin_user": "face_recognition",
          "admin_password": "abp",
          "upload_location":"ImageBasics"
         }

app.config['UPLOAD_FOLDER']=params['upload_location']
app.secret_key = 'super-secret-key'

cam = cv2.VideoCapture(0)

@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/dashboard",methods=['GET','POST'])
def dashboard():
    if ('user' in session and session['user']==params['admin_user']):
         return render_template('dashboard.html',params=params)

    if request.method=='POST':
        username=request.form.get('uname')
        userpass=request.form.get('pass')
        if username==params['admin_user'] and userpass==params['admin_password']:
            session['user']=username
            return render_template('dashboard.html',params=params)
        else:
            return render_template('login.html',params=params)
    return render_template('login.html',params=params)

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/uploader",methods=['GET','POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if(request.method=='POST'):
            first=request.form.get('fname')
            last=request.form.get('lname')
            f=request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(first+" "+last+".png")))
            return render_template('uploader.html')
        else:
            return render_template('dashboard.html')

path = 'ImageBasics'
image_names = []
known_images = []
known_encodings = []
listknown=[]
mylist = os.listdir(path)

for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    known_images.append(curImg)
    image_names.append(os.path.splitext(cl)[0])

for img in known_images:
    encode = face_recognition.face_encodings(img)[0]
    known_encodings.append(encode)
    listknown.append(encode)

def creating():
    while True:
        s, frame = cam.read()
        if not s:
            break
        else:
            current_frame = face_recognition.face_locations(frame)
            encode_frame = face_recognition.face_encodings(frame, current_frame)

            for encoded, face_location in zip(encode_frame, current_frame):
                m = face_recognition.compare_faces(listknown, encoded)
                distance = face_recognition.face_distance(listknown, encoded)

                i = np.argmin(distance)
                x = np.min(distance)
                if m[i]:
                    if x < 0.5:
                        name = image_names[i].upper()
                    else:
                        name = "Unknown"

                    y1, x2, y2, x1 = face_location
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield(b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recognition',methods = ['POST'])
def recognition():
    return render_template("recognition.html")

@app.route('/normal_recognition')
def video_feed():
    return Response(creating(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)