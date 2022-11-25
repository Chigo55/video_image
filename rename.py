import os
from datetime import datetime

image_path = 'img/'
image_list = os.listdir(image_path)

t = datetime.now()

count = 1
for picture_name in image_list:
    src = os.path.join(image_path, picture_name)
    dst = str(count).zfill(4) + '.jpg'
    dst = os.path.join(image_path, dst)
    os.rename(src, dst)
    count += 1