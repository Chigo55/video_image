import cv2
import os
import math

# 영상 파일 경로
input_path = 'video/'

# 추출한 이미지 파일 경로
output_path = 'img/'

# 추출할 이미지 갯수
EXTRACTION = 1000

def video2img(file_name):
    # 영상 파일의 프레임을 분할하여 이미지 형식으로 가져온다
    cap = cv2.VideoCapture(file_name)

    # 영상 길이에 따른 총 프레임을 계산
    total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print('총 프레임 수 :', total_frame)

    # 추출할 개수에 따라 총 프레임에서 나누어 분할할 프레임을 소수점을 이하의 수를 버리고 계산
    ext_num = math.trunc(total_frame / EXTRACTION)

    # 프레임 카운트
    frame_cnt = 0
    
    # 생성될 파일의 갯수 카운트
    file_cnt = 0

    # 지정된 경로에 파일의 없을 경우 0에서 시작
    # 파일 이름 카운트
    # file_name_cnt = 0

    #  지정된 경로에 파일이 있을 경우 파일의 이름에서 번호를 추출하여 사용
    # 파일 이름 카운트
    file_name_cnt = int(os.listdir(output_path)[-1].split(".")[0]) + 1

    # 무한 반복
    while True:
        # 이미지 형식으로 가져온 영상을 ret, frame으로 분할
        ret, frame = cap.read()
        
        # ret가 없을 경우 영상이 끝난것으로 판단후 break
        if not ret:
            break
        
        # 프레임 카운트 수가 분할 프레임 수와 같아질 때
        if frame_cnt % ext_num == 0:
            # 영상의 현재 프레임을 파일 이름 카운트와 함께 
            # 이미지 파일(.jpg)로 추출한 이미지 파일 경로에 저장
            img_name = "img/" + str(file_name_cnt).zfill(4) + '.jpg'
            cv2.imwrite(img_name, frame)
            
            # 확인용 프린트 문
            print('파일 생성 완료! :', img_name)
            print("file_cnt :", file_cnt)
            print("file_name_cnt :", file_name_cnt)
            
            # 저장시 사용할 파일 이름 카운트 1 증가
            file_name_cnt += 1
            # 파일 갯수 카운트 1 증가
            file_cnt += 1

        # 파일 카운트가 추출할 갯수와 같이지면 break
        if file_cnt == EXTRACTION:
            file_cnt = 0
            break
        
        # 프레임 카운트 1증가
        frame_cnt += 1
    
    # 가져오기 종료
    cap.release()

if __name__ == "__main__":
    if not os.path.isdir(input_path):
        os.makedirs(input_path)
    if not os.path.isdir(output_path):
        os.makedirs(output_path)

    file_list = os.listdir(input_path) #경로 입력
    for i in file_list:
        video2img(input_path + i)