import time
import cv2
#from main import main_v1
def snapShotCt(camera_idx=1):  # camera_idx的作用是选择摄像头。如果为0则使用内置摄像头，比如笔记本的摄像头，用1或其他的就是切换摄像头。
    cap = cv2.VideoCapture(camera_idx)
    ret, frame = cap.read()  # cao.read()返回两个值，第一个存储一个bool值，表示拍摄成功与否。第二个是当前截取的图片帧。
    while ret:
        cv2.imwrite(".\\photo\\2.jpg", frame)  # 写入图片
        time.sleep(1)  # 休眠一秒 可通过这个设置拍摄间隔，类似帧。
        ret, frame = cap.read()  # 下一个帧图片
    cap.release()

snapShotCt(0)
