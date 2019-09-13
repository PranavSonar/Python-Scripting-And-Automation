import os, shutil, re
from glob import glob

# get the file location
log_dir_path = 'C:/Users/Vivek Kumar/Google Drive/shared_with_me/Implementation/src/odi/{DEVISON}_file_development/vlr/{DEVISON}_hub/'.strip()
stage_dir_path = 'C:/Users/Vivek Kumar/Google Drive/shared_with_me/Implementation/src/odi/{DEVISON}_file_development/vlr/{DEVISON}_hub/test/'.strip()
os.chdir(log_dir_path)
for filename in glob('*.txt'):
    new_filename = filename.replace(' ','_').replace('-','_')
    shutil.move(filename,new_filename)
    shutil.move(new_filename,stage_dir_path)
