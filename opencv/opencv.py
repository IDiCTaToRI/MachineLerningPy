import cv2

path = 'test_pic.jpg'
image = cv2.imread(path)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

print(f'Найдено лиц: {len(faces)}')

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

status = cv2.imwrite(f'faces_detected_{path[:-4]}.jpg', image)

print(f'Результат сохранён в избражении faces_detected_{path[:-4]}.jpg: {status}')
