import time
import uiautomator2 as u2
import onnxruntime as ort
import cv2

ort.set_default_logger_severity(3)
# ocr = ddddocr.DdddOcr()

d = u2.connect("127.0.0.1:16384")
screen = d.screenshot(format="opencv")
# screen = cv2.imread("x.png")

print(screen.shape)

print(screen[1264, 300])

cropped_image = screen[961:1034, 578:651]
cv2.imwrite("cut" + str(time.time()) + ".png", cropped_image)

# text_recognizer = TextRecognizer(cropped_image, ocr)
# x = text_recognizer.find_text_from_image()
# print(x)
