import cv2
import os
import math

input_path = 'video/'
output_path = 'img/'
file = 'img/0000.jpg'
EXTRACTION = 1000

def video2img(file_name):
    cap = cv2.VideoCapture(file_name)
    total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print('총 프레임 수 :', total_frame)

    ext_num = math.trunc(total_frame / EXTRACTION)
    frame_cnt = 0
    file_cnt = 0

    #     file_name_cnt = 0
    file_name_cnt = int(os.listdir(output_path)[-1].split(".")[0]) + 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_cnt % ext_num == 0:
            img_name = "img/" + str(file_name_cnt).zfill(4) + '.jpg'
            cv2.imwrite(img_name, frame)
            print('파일 생성 완료! :', img_name)
            print("file_cnt :", file_cnt)
            print("file_name_cnt :", file_name_cnt)
            file_name_cnt += 1
            file_cnt += 1

        if file_cnt == EXTRACTION:
            file_cnt = 0
            break

        frame_cnt += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if not os.path.isdir(input_path):
        os.makedirs(input_path)
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    file_list = os.listdir(input_path) #경로 입력
    for i in file_list:
        video2img(input_path + i)