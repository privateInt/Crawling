# 이미지 넘버링
import os
import glob

def rename(files):
    if 'cat' in files[0]:
        for i,f in enumerate(files):
            os.rename(f, os.path.join(path+"/cat", 'cat_' + '{0:03d}.jpg'.format(i)))  
        print("cat {}번째 이미지까지 성공".format(i+1))

    elif 'dog' in files[0]:
        for i,f in enumerate(files):
            os.rename(f, os.path.join(path+"/dog", 'dog_' + '{0:03d}.jpg'.format(i)))
        print("dog {}번째 이미지까지 성공".format(i+1))

#path = "C:\Imageclassification\data"
#path = "/Imageclassification/train"
path = "/Imageclassification/test"

cat = glob.glob(path+"/cat" + '/*')
dog = glob.glob(path+"/dog" + '/*')

rename(cat)
rename(dog)

# 이미지 정렬
cat = sorted(cat)
dog = sorted(dog)

whole_sum = len(cat)+len(dog)
print('cat 이미지 개수: {}\ndog 이미지 개수: {}'.format(len(cat), len(dog)))
print('전체 이미지 개수 : {}\ncat 이미지 비율 : {:.2f}%\ndog 이미지 비율 : {:.2f}%'.format( whole_sum, 100*len(cat)/whole_sum, 100*len(dog)/whole_sum))