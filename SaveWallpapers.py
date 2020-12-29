import os
import shutil
import getpass
from PIL import Image


# desired minimum image width (1920) and windows user
desired_image_width = 1920
windows_user = getpass.getuser()

# location of windows images and destination folder
my_path = 'C:\\Users\\'+windows_user+'\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'
destination = 'C:\\Users\\'+windows_user+'\\Desktop\\Wallpapers\\Provisional\\'

# create list of files in the windows path
source_files = os.listdir(my_path)

# delete (empty) the destination folder and create it again
os.system('cmd /c "rmdir /s/q '+destination+'"')
os.system('cmd /c "mkdir  '+destination+'"')
print("done deleting old files")

# copy files to destination folder
for file in source_files:
    full_path = os.path.join(my_path, file)
    shutil.copy(full_path, destination+file)
print("done copying")

# put .jpg extension to the files
os.system('cmd /c "cd '+destination+' & Ren *.* *.jpg"')
print("done JPG extension")

# create the list of JPG files in the destination folder
renamed_files = os.listdir(destination)

# count total of images processed and deleted
count_deleted=0
count_total=0
# delete files shorter than desired size, mostly small icons
for newfile in renamed_files:
    image = Image.open(destination+newfile)
    width = image.width
    image.close()
    count_total += 1
    if width != desired_image_width:
        path_to_delete = os.path.join(destination, newfile)
        os.system('cmd /c "del /f '+path_to_delete+'"')
        count_deleted += 1
print(f'Done! Total files: {count_total}, Small images deleted: {count_deleted}')