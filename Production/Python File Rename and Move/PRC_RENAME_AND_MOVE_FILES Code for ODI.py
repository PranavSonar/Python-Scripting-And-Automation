import os, shutil, re
from glob import glob
# get the file location
log_dir_path = '<%=odiRef.getOption("LOG_DIR")%>'.strip()
stage_dir_path = '<%=odiRef.getOption("STAGE_DIR")%>'.strip()
os.chdir(log_dir_path)
for filename in glob('*.txt'):
    new_filename = filename.replace(' ','_').replace('-','_')
    shutil.move(filename,new_filename)
    shutil.move(new_filename,stage_dir_path)
