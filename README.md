# Face-Recognition
This project is made using face-recognition library with opencv and frontend is developed using Bootstrap framework with some personal customizations and backened is developed using flask framework. 

## Requirements 
* This model requires latest version of python.
* It requires dlib library which is coded in c++ and requires installation of visual studio with developer tools in c++.
* All other libraries have to be imported from text file requirements.txt 

## Files Description
* Templates - This folder has html files for the hosting of this model.
  * Index.html - It is the first page which contains START button which redirect to recognition.html. On the top it has a navigation bar which has admin controls.
  * recognition.html - This webpage has a window to show webcam with your name and also has a END button which redirects the user to index.html.
  * login.html - This webpage has a signin option for the admin to add more images in the ImageBasics folder which our model can recognize. 
  * dashboard.html - This webpage allows the admin to upload images by renaming it.
  * uploader.html - This webpage shows the message that image is uploaded successfully and has a BACK button.
* app.py - It is a python file which has all the code related to face-recognition model.
* ImageBasics - This folder contains all the images which the model can recognise.
* static - It contains homepage photo and css files which is used in designing.

## Refrences 
* https://pypi.org/project/face-recognition/
* https://flask.palletsprojects.com/en/2.0.x/
* https://getbootstrap.com/docs/5.0/getting-started/introduction/

## Team Members
* Amit Kumar Makkad 
* Bhavya Contractor
* Priyansh Jaseja

## Mentors
* Miten Shah
* Bharat Gupta
* Anjali Singhal

## Screenshots of our model
* Homepage

![Homepage](https://user-images.githubusercontent.com/79632719/127176176-ee445419-a24c-4a6a-b786-51f22f20c595.png)

* recognition page

![recognition](https://user-images.githubusercontent.com/79632719/127176259-3843bb81-7a4b-4c12-a2ef-7b28066c6e51.png)

* login page

![login](https://user-images.githubusercontent.com/79632719/127176452-0e4b4966-05f2-40e0-8b51-73c016ead6dc.png)

* dashboard page

![dashboard](https://user-images.githubusercontent.com/79632719/127176599-867c12b5-ef10-4dc6-bb59-bbce21dda2ad.png)

* uploader page

![uploader](https://user-images.githubusercontent.com/79632719/127176672-ecaf89ba-246f-4a31-8927-116795b81520.png)





