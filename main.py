import os
import shutil
import glob
train='path/to/folder where/you want to put/training images/'
path='path /to/the mai/folder'
test='path/to/folder where/you want to put/testing images/'
i = 1
j=1
x=(sum([len(files) for r, d, files in os.walk(path)]))
print(x)
y=x*0.20
z=x*0.80
print(y)
print(z)
for root,dirs,files in os.walk(path):

     for file in files:
        #print(file)
#copying the 20% of the images and removing the same from the main folder to test folder
        if file.endswith('.jpg') or file.endswith('.JPG'):
            
            if i < y+1:
                #print(file)#testing
                #if os.path.isdir(train):
                shutil.copy(os.path.join(path, file), test)#shutil.copyfile(path, train)#shutil.copy(files, 'test')
                os.remove((os.path.join(path, file)))#remove=os.path.join('C:/Users/user/Pictures/Camera Roll',)#os.remove(os.path.join(path,"*.jpg ","*.JPG")#b=os.path.join(train,os.path.basename(path))
                
            i += 1
            
            #copying the rest 80% of images to train folder
for jpgfile in glob.iglob(os.path.join(path,("*.jpg" or "*.JPG"))):
    #print("%d",src_dir)

    
        shutil.copy(jpgfile,train)
