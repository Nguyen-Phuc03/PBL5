from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS


app = Flask(__name__)
CORS(app=app, support_credentials=True)
app.config['IMAGE_UPLOAD_PATH'] =r"C:\Users\USER\Downloads\PBL5_Demo\PBL5_Demo\Backend\app\static\images"



client = MongoClient(host='localhost',port=27017)
print(client)
db = client.AttendenceSystem1

## INITIATING COLLECTIONS
from app.Collections.Courses import Courses
from app.Collections.Departments import Departments
from app.Collections.Users import Users
Courses.create()
Departments.create()
Users.create()

from app.Controllers import courseController
from app.Controllers import departmentController
from app.Controllers import userController
from app.Controllers import studentController
from app.Controllers import teacherController


