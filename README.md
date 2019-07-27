# CSOC-2.0
### Link for demo video (https://drive.google.com/open?id=1MF980HOWH1yjsLt6NJB-35uwSrHHLlGV)
    - This video doesn't show all funtionalities like Voice Search which we discuss below
# Requirements
Any python 3 version. However pythnon 3.7 is recommended.
Once you have successfully installed python  then in your cmd write following commands to install various modules 
- pip install django==2.2.2
- pip install bcrypt
- pip install django[argon2]
- pip install django-bootstrap3
- pip install django-braces
- pip install misaka
- pip install pillow
- pip install pyttsx3
- pip install SpeechRecognition
- pip install PyAudio. If you are using windows then refer (https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-my-python-how-to-do-it)
- ### Sometimes you may get pywin error. So you need to install that from github. Follow the instructions below:
     1. Open (https://github.com/mhammond/pywin32/releases/tag/b224).
     2. Scroll down you see 'Assets' dropdown. Click on it.
     3. Now based on your python version install correct .exe
# Working using cmd
### Follow the steps below
- Download the zip.
- Extract all files and folders in single directory.
- Open cmd and change directory where uinote(extracted folder) is present.
- Activate your virtual environment if you are using it. It is not mandatory.
- Then in your cmd type  python manage.py runserver. Do not close cmd; just minimise it.
- Now in your browser open (http://127.0.0.1:8000/)
- Here you can use this website

# Various functionalities of website
- # Voice Search
As in every normal website user can manually click on links and fill the forms to get notes and papers which we discuss later.
But this website has functionality by which user can ask anything in english language and it will automatically takes you 
to the asked page if possible.
### How to use
- Click on 'Just Ask' option in the navbar
- It will wish you and after waiting for a second you can ask your question in english language regarding to the website.
- It will automatically takes you to your destination.
#### for eg. if user asked ,"show digital circiut pdfs of 3rd semester ECE department"; then it will display that pdfs. No need to 
#### fill any form as we discuss later.

### Note:
- After it wishes you, wait for about 1 second and then ask your question
- #### Some features of this voice search like opening pdfs occur in chrome only. So chrome is recommended for this.However it is not mandatory to use chrome only. If you use some other browser and you ask for notes or papers it will automatically open that one in chrome .


- # Get free Notes 
### Here user can get the notes of various subjects in a very simple way by following the steps below
- Click on Notes in navbar. It will takes you to the page where various departments are present.
- Choose your department and a dropdown to that particular department will appaer.
- Click on 'get notes' option and a form will pop up to you screen.
- Fill the form and then it will ask you to choose subject.
- Finally you see pdfs present regarding the given details.


- # Get free previous year question papers
### Here user can get previous year question papers by following the steps below
- Click on Papers in navbar.It will take you to the page which displays various departments.
- Choose your department and click on 'Click Here' button and a form will pop up.
- Form will ask for your semester and click on 'submit' button.
- Now choose your desired subject and click 'submit'.
- Now you will see Pdfs with required details.

- # Discussion Form
It is a community where a user can discuss his/her doubts with other users. Here user can
- create a new group.
- ask doubts
- add comment to someone's question

- ## Create new  group

- This functionality can be accessed by selecting Discussions option in navbar.
- User has to sign in if he/she wants to create one.
- After signing in choose 'Create Group' option on Discussions page.
- Enter the name and description for your desired group and click on 'create' button.
- After this it will display option to join/leave group.

- ## View Groups

- On Discussions page click on 'Groups' option to view all the groups with relevant details like number of members and posts in each group.

- ## Ask Questions and Add Comments.

- Click on 'Ask question' to ask doubts and resolve queries.
- Put your message in message box.
- Select the desired group from select menu below.
- Click on Post button.
- Now You can see your username and message on screen along with day/date/time of the post.
- It will also give you option to delete post.
- any other user can also comment on your post by clicking on 'Add Comment'.
- After clicking on 'Add Comment' button any other user can leave a message with his/her username on your post.

# Upload notes
  Every users will not have permissions to upload notes. Only some users like CR's of every class will be given rights to upload notes. 
  Users with superuser rights can see 'upload' option in the navbar. But for security purposes we have used OTP confirming method.
  
  # OTP SMS
   - When CR(or any user with superuser rights) click on 'upload' option a form open with some warnings.
   - Now user input his/her phone number and click on generate OTP.
   - OTP is sent to the number provided.
   - Now if the OTP is confirmed only then user will see form to upload notes.
   - There is also a resend otp button.
   
  # Authentication for copyright notes
     When user input number for OTP, his personal number is stored from which we get the information that copyright pdf is uploaded by        which user.
