import os

input_path = 'rename_img/'
# input_path = 'rename_txt/'


def rename(image_path, start_number=0):
    image_list = os.listdir(image_path)

    count = start_number

    for picture_name in image_list:
        src = os.path.join(image_path, picture_name)
        dst = str(count).zfill(4) + '.jpg'
        dst = os.path.join(image_path, dst)
        os.rename(src, dst)
        count += 1

if __name__ == "__main__":
    if not os.path.isdir(input_path):
        os.makedirs(input_path)

    file_list = os.listdir(input_path) #경로 입력

    for i in file_list:
        rename(input_path + i, start_number=0)