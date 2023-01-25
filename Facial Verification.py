import face_recognition
import os
import cv2
source_img = face_recognition.load_image_file("Path to Source Image")
source_face_encoding = face_recognition.face_encodings(source_img)[0]
for filename in os.listdir("Path to Directory"):
    img = face_recognition.load_image_file(f"Path to Directory{filename}")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img_face_encoding = face_recognition.face_encodings(img)[0]
    results = face_recognition.compare_faces([source_face_encoding], img_face_encoding)
    if results[0]:
        cv2.imshow("Matching Image "+filename, img)
        cv2.waitKey(0)
cv2.destroyAllWindows() 
