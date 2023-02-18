import argparse
import cv2
def detectFace(input, output):
    input = cv2.imread(input) # 讀取圖檔
    grayinput = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY) # 透過轉換函式轉為灰階影像
    color = (0, 255, 0)  # 定義框的顏色
    # OpenCV 人臉識別分類器
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # 調用偵測識別人臉函式
    faceRects = face_classifier.detectMultiScale(
        grayinput, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    
    # 大於 0 則檢測到人臉
    if len(faceRects):  
        # 框出每一張人臉
        for faceRect in faceRects: 
            x, y, w, h = faceRect
            cv2.rectangle(input, (x, y), (x + h, y + w), color, 2)
             # 將結果圖片輸出
    cv2.imwrite(output, input)

parser = argparse.ArgumentParser()

parser.add_argument("--input", type=str, help="source image path", required=True)
parser.add_argument("--output", type=str, help="destination image path")
args = parser.parse_args()

if args.output is None:
    args.output = args.input[:-4] + '_new.jpg'

if args.input:
    detectFace(args.input, args.output)

