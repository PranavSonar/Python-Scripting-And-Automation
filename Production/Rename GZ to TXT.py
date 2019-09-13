python

import os,shutil
from glob import glob
print os.getcwd()
for file in glob("*.gz.txt"):
    words = file.split(".")
    # print file
    new_file = ""
    for i in range(0, len(words) - 1):
        if new_file:
            new_file = new_file + "." + words[i]
        else:
            new_file = words[i]
    print "old %s renamed to %s"%(file,new_file)
    shutil.move(file,new_file)

exit()