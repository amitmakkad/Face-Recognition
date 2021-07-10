from flask import Flask, render_template, Response, url_for
import cv2
import face_recognition
import numpy as np
import os


app = Flask(__name__, template_folder='template')
cam = cv2.VideoCapture(0)

path = 'ImageBasics'
image_list = []
image_names = []
mlList = os.listdir(path)

for img in mlList:
    current = cv2.imread(f'{path}/{img}')
    image_list.append(current)
    image_names.append(os.path.splitext(img)[0])


def encoding(image_list):
    encoding_list = []
    for img in image_list:
        # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(img)[0]
        encoding_list.append(encoding)
    return encoding_list

listknown = encoding(image_list)



def creating():
    while True:
        s, frame = cam.read()
        if not s:
            break
        else:
            face_names = []
            current_frame = face_recognition.face_locations(frame)
            encode_frame = face_recognition.face_encodings(frame, current_frame)

            for encoded, face_location in zip(encode_frame, current_frame):
                m = face_recognition.compare_faces(listknown, encoded)
                distance = face_recognition.face_distance(listknown, encoded)

                i = np.argmin(distance)
                x = np.min(distance)
                if m[i]:
                    if x < 0.48:
                        name = image_names[i].upper()
                    else:
                        name = "Unknown"

                    y1, x2, y2, x1 = face_location
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.waitKey(17)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield(b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/res',methods = ['POST'])
def res():
    return render_template("finale.html")

@app.route('/results')
def video_feed():
    return Response(creating(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)