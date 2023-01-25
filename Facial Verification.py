import face_recognition
import os
import cv2
source_img = face_recognition.load_image_file("//home//rajesh//Desktop//week3//TASK 4//Images//295999c1c9187d059a31dfaf4a02828b.jpg")
source_face_encoding = face_recognition.face_encodings(source_img)[0]
for filename in os.listdir("//home//rajesh//Desktop//week3//TASK 4//Images"):
    img = face_recognition.load_image_file(f"//home//rajesh//Desktop//week3//TASK 4//Images//{filename}")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img_face_encoding = face_recognition.face_encodings(img)[0]
    results = face_recognition.compare_faces([source_face_encoding], img_face_encoding)
    if results[0]:
        cv2.imshow("Matching Image "+filename, img)
        cv2.waitKey(0)
cv2.destroyAllWindows() 