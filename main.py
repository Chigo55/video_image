import cv2
import os

input_path = 'viedo/'
output_path = 'img/'
EXTRACTION = 10

def video2img(file_name):
    cap = cv2.VideoCapture(file_name)
    total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print('총 프레임 수 :', total_frame)

    ext_num = round(total_frame / EXTRACTION)
    frame_cnt = 0

    file_cnt = int(os.listdir(output_path)[-1].split(".")[0]) + 1

    while True:
        key = cv2.waitKey(33)
        if key == ord('q'):
            break
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('video', frame)
        if frame_cnt % ext_num == 0:
            img_name = "img/" + str(file_cnt).zfill(4) + '.jpg'
            cv2.imwrite(img_name, frame)
            print('파일 생성 완료! :', img_name)
            file_cnt += 1
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


