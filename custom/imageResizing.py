import os
from PIL import Image

data_dir = '/data/YoloTrainSet'
print('data_dir : \n', os.listdir(data_dir))

category = [c for c in os.listdir(data_dir) if c != '.DS_Store']
print('Category : \n', category)

directory_list = [os.path.join(data_dir, c) for c in category]
print('Directory List : \n', directory_list)

new_path = '/data/NewYoloTrainSet'
new_path_list = [os.path.join(new_path, c) for c in category]
print('New Path List : \n', new_path_list)

img_list = []
for i in range(len(category)):
  temp = os.listdir(directory_list[i])
  temp = [file for file in temp if file.split('.')[1] == 'jpg']
  img_list.append(temp)

for i in range(len(category)):
  dir = directory_list[i]
  for j in range(len(img_list[i])):
    img_dir = os.path.join(dir, img_list[i][j])
    save_img_dir = os.path.join(new_path_list[i], img_list[i][j])

    image = Image.open(img_dir)
    if image.mode != 'RGB':
      image = image.convert('RGB')
    resize_image = image.resize((int(image.width / 3), int(image.height / 3)))
    resize_image.save(save_img_dir)
