import os
import shutil
import re
from glob import glob

# get the file location

# stage_dir_path = '/{root}/{DEVISON}/VLR/stage'.strip()
stage_dir_path = 'D:/Programs/WorkArea/Code-Challenge/Python/TABE_SEPERATED_FILE_TRANSFORMATION_{DEVISON}_{DEVISON}_VLR/Stage'.strip()
# build_dir_path = '/{root}/{DEVISON}/VLR/build'.strip()
build_dir_path = 'D:/Programs/WorkArea/Code-Challenge/Python/TABE_SEPERATED_FILE_TRANSFORMATION_{DEVISON}_{DEVISON}_VLR/build'.strip()
# archive_dir_path = '/{root}/{DEVISON}/VLR/archive'.strip()
archive_dir_path = 'D:/Programs/WorkArea/Code-Challenge/Python/TABE_SEPERATED_FILE_TRANSFORMATION_{DEVISON}_{DEVISON}_VLR/archive'.strip()

# Go to files directory and read the file
os.chdir(stage_dir_path)
for filename in glob('*.log'):
    # Delete empty files
    if os.path.getsize(filename) == 0:
        os.remove(filename)
        continue  # Skip to other file
    new_filename = filename.replace('.log', '.txt').replace(' ', '_')
    fp = open(filename, 'r')
    nfp = open(new_filename, "w")
    complete_line = ''
    for line in fp.readlines():
        # remove extra space from begging and ending place of line
        line = line.strip().split()
        if len(line) == 3:
            complete_record = line[0]+','+line[1]+','+line[2]+'\n'
            complete_line += complete_record
        elif len(line) == 2:
            if len(line[0]) > 13 and len(line[1]) < 8:
                complete_record = line[0]+','+'NA'+','+line[1]+'\n'
                complete_line += complete_record
            elif len(line[0]) > 13 and len(line[1]) > 8:
                complete_record = line[0]+','+line[1]+','+'NA'+'\n'
                complete_line += complete_record
            else:
                complete_record = 'NA'+','+line[0]+','+line[1]+'\n'
                complete_line += complete_record
        else:
            raise Exception(line)
    # it will write the content in new file in loop
    nfp.write(complete_line)
    # close both original and splited file
    nfp.close()
    fp.close()
    # Delete the original file replace with new file

    print filename
    print new_filename
    # os.system("chmod 777 " +new_filename)

    shutil.move(new_filename, build_dir_path)
    shutil.move(filename, archive_dir_path)
