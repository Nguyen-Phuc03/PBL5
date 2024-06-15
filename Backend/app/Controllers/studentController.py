from app import app
import json
import os
import cv2
import face_recognition
from flask import jsonify, request
from app.Services.studentServices import studentServices
from app.Services.userServices import userServices

@app.route('/get_all_students',methods=['POST'])
def get_all_students():
    data = json.loads(request.data.decode('utf8'))
    filters = data['filters']
    projection = data['projection']
    filters = None if not filters else filters 
    projection = None if  not projection else projection
    
    print("***********************")
    print(filters)
    
    try:
        filters['_id'] = filters.pop('username')
    except: pass    
    
    curser = studentServices.get_all_students(filters, projection)
    
    allStudents = []
    for student in curser:
        student['username'] = student.pop('_id')
        allStudents.append(student)
        
    return jsonify({
        "allStudents" : allStudents
    })
    
    
@app.route('/update_student',methods=['POST'])
def update_sudent():
    updateData = json.loads(request.data.decode('utf8'))
    whatToUpdate = updateData['whatToUpdate']
    whomToUpdate = updateData['whomToUpdate']
    
    return studentServices.update_student(whomToUpdate,whatToUpdate)



@app.route('/enroll_student', methods=['POST'])
def enroll_student():
    # Lấy dữ liệu từ form data
    courseData = request.form.get('courseData')
    student_roll = request.form.get('roll_no')
    image_file = request.files['file']

    # Lưu ảnh vào thư mục
    image_path = os.path.join(app.config["IMAGE_UPLOAD_PATH"], student_roll)
    image_file.save(image_path) 
    
    # Đọc ảnh và tạo mã hóa khuôn mặt của sinh viên
    image_loaded = cv2.imread(image_path)
    student_image_encoding = face_recognition.face_encodings(image_loaded)[0]
    
    # Mảng chứa các đối tượng phản hồi
    response_array = []
    
    # Duyệt qua tất cả các khóa học để đăng ký
    for course, condition in courseData.items():
        if condition:    
            # Tạo dữ liệu sinh viên
            student_data = {
                "roll_no": student_roll,
                "encoding": list(student_image_encoding)
            }
            
            # Đăng ký sinh viên vào khóa học và cập nhật thông tin khóa học của người dùng
            course_response = studentServices.enroll_student(course, student_data)
            userServices.updateCourseInfoOfUser(course, {"roll_no": student_roll}, 'student')
            response_array.append(course_response)
    
    return jsonify(response_array)