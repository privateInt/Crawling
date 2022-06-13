import shutil
import math
import glob
import random

def split( img_list, test_count, train_path, test_path):
  
    test_files=[]
    for i in random.sample( img_list, test_count ):
      test_files.append(i)

    # 차집합으로 train/test 리스트 생성하기
    train_files = [x for x in img_list if x not in test_files]

    for k in train_files:
      shutil.copy(k, train_path)
  
    for c in test_files:
      shutil.copy(c, test_path)

    print('train 폴더 이미지 개수 : {}\ntest 폴더 이미지 개수 : {}'.format(len(glob.glob(train_path+'/*')),len(glob.glob(test_path+'/*'))))

path = "/Imageclassification/data"
cat = sorted(glob.glob(path+"/cat" + '/*'))
dog = sorted(glob.glob(path+"/dog"+'/*'))

cat_test_count = round(len(cat)*0.2)
dog_test_count = round(len(dog)*0.2)

cat_train_path='/Imageclassification/train/cat'
cat_test_path='/Imageclassification/test/cat'

dog_train_path='/Imageclassification/train/dog'
dog_test_path='/Imageclassification/test/dog'

split(cat, cat_test_count, cat_train_path, cat_test_path)
split(dog, dog_test_count, dog_train_path, dog_test_path)