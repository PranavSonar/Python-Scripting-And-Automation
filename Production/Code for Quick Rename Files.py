python

import os 
from glob import glob
path=os.getcwd()
os.chdir(path)
print "Current working Dir: "+path
print "Searching File..."
for filename in glob('*.bad'):
    path_filename=path+filename
    new_filename=filename+'.txt'
    os.rename(filename,new_filename)
    print 'BAD FILE FOUND : '+filename+' RENAMING TO : '+new_filename

exit()