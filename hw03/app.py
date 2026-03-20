# 纯 Python 人脸检测（无网页、无 Streamlit）
import cv2

# 加载人脸检测器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 读取图片（把这里换成你的图片路径，比如 "test.jpg"）
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测人脸
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# 画出人脸框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 显示结果
cv2.imshow("人脸检测结果", img)
cv2.waitKey(0)
cv2.destroyAllWindows()