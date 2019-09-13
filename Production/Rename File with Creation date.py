
from os import chdir,path
import shutil,glob
from datetime import datetime

# return today datecode
get_today_datecode= datetime.today().strftime('%Y%m%d')
# To get modified date of any file
def get_m_datecode(filename):
    return datetime.fromtimestamp(path.getmtime(filename)).strftime('%Y%m%d')

# To get create date of any file
def get_c_datecode(filename):
    return datetime.fromtimestamp(path.getctime(filename)).strftime('%Y%m%d')

# To get create date of any file
def get_a_datecode(filename):
    return datetime.fromtimestamp(path.getatime(filename)).strftime('%Y%m%d')

work_dir='C:/Users/vk041/Desktop/test'
print work_dir
chdir(work_dir)


for filename in glob.glob('*'):
    new_filename= filename+' '+get_m_datecode(filename)
    print filename
    print new_filename
    shutil.move(filename,new_filename)
    
