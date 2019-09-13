
# Alise implientation in production system
# alias xdelf='python /{root}/bin/tools/CODE_FOR_QUICK_DELETE_FILES.py $1' 
# alias gtools='cd /{root}/bin/tools'
# python
import shutil,os,sys
from glob import glob
# get current working dir
path=os.getcwd()
# open in python to current working dir
os.chdir(path)
# get search pattern as 1st external parameter 
pattern=str(sys.argv[1])
print path 
print "Current working Dir: "+path
print "Pattern Finding: "+pattern
print "Searching File..."
file_count=0
for filename in glob(pattern):    
    file_count=file_count+1
    print "Total file found : "+str(file_count)
    print "Files are Following:"
    print filename
    print "Deleting files ..."
    os.(filename)
# exit()
