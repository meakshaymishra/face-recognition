import cv2
import numpy as np
import sqlite3

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)


def insertOrUpdate(Id, Name):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM People WHERE ID=" + str(Id)
    print(str(Name))
    cursor = conn.execute(cmd)
    isRecordExist = cursor.fetchone()
    print(isRecordExist)
    # for row in cursor:

    if isRecordExist is None:
        cmd = "INSERT INTO People(ID,Name,Age,Gender,Semester) Values(" + \
            str(Id)+",'"+str(Name)+"','"+str(age) + \
            "','"+str(sex)+"','"+str(sem)+"')"

    else:
        cmd = "UPDATE People SET Name='"+str(Name)+"' WHERE ID=" + str(Id)

    conn.execute(cmd)
    conn.commit()
    conn.close()


sampleNum = 0
id = raw_input('Enter user id: ')
name = raw_input('Enter the name: ')
age = raw_input('Enter the age: ')
sex = raw_input('Enter your Gender (M/F) ')
sem = raw_input('Enter which semseter you are in... ')

insertOrUpdate(id, name)
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        sampleNum = sampleNum+1
        cv2.imwrite("dataSet/User."+str(id)+"." +
                    str(sampleNum)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.waitKey(100)
    cv2.imshow("Face", img)
    cv2.waitKey(1)
    if(sampleNum > 20):
        break
cam.release()
cv2.destroyAllWindows()
