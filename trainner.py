import os
import cv2
import numpy as np
from PIL import Image

recoginizer = cv2.createLBPHFaceRecognizer()
path = 'dataSet'


def getImagesWithID(path):
    imagePaths = [os.path.join(path, f)for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print(ID)
        IDs.append(ID)
        cv2.imshow("trainning", faceNp)
        cv2.waitKey(10)
    return np.array(IDs), faces


Ids, faces = getImagesWithID(path)
recoginizer.train(faces, Ids)
recoginizer.save('recoginizer/trainningData.yml')
cv2.destroyAllWindows()