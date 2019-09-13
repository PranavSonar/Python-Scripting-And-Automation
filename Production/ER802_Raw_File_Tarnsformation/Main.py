import os
import shutil
import re
from glob import glob

file_path = "C:/WorkArea/Python_Home/The_Python_Bible_Everything_You_Need_to_Program_in_Python/20190112/{SUB-STREAM}_RawFile_Tarnsformation/"
filename = "Test.log".strip()
# filename = "PP.20190112.35657".strip()

# creating new file with {Devison}e name .txt on {Devison}e dir
# new_filename = filename+'.txt'
# new_file = os.path.join(file_path, os.path.basename(new_filename))
os.chdir(file_path)
# fp = open(filename, 'r')
# nfp = open(new_filename, "w")
fp = open(filename)

for line_number, line in enumerate(fp):
    line = line.replace('\n', ' ')
    line_content = line.split(',',)
    line_length = line_content.__len__()
    if line_length > 3 and line_content[3] == '800':
        if line_content[2] == '801':
            current_line = line
            # print line
        elif line_content[2] == '804':
            current_line = line

            # print line
        elif line_content[2] == '756':
            current_line = line
            # print line
        elif line_content[2] == '802':
            read_next_line_flag = True
            while read_next_line_flag:
                try:
                    
                    f = open(filename)
                    lines = f.readlines()
                    next_line = lines[line_number+1]
                    next_line_content = next_line.split(',',)
                    next_line_length = next_line_content.__len__()
                    if next_line_length > 3 and next_line_content[3] == '800':
                        current_line = line
                        # line_content = line.split(',',)
                        # line_length = line_content.__len__()
                        # message_merge_length = line_length-4
                        # message = ''                        
                        # for i in range(17, message_merge_length):
                        #     message += line_content[i]
                        # line_content_17 = message
                        # line_content_18 = line_content[message_merge_length+1]
                        # line_content_19 = line_content[message_merge_length+2]
                        # line_content_20 = line_content[message_merge_length+3]
                        # # line_content_21 = line_content[message_merge_length+4]
                        # current_line=line_content_17+','+line_content_18+','+line_content_19+','+line_content_20
                        read_next_line_flag = False
                    else:
                        line = line+' '+next_line
                        line_number = line_number+1
                        read_next_line_flag = True
                except StopIteration:
                    read_next_line_flag = False
                    # print "**********No rows - StopIteration"+line
                except IndexError:
                    current_line = line
                    read_next_line_flag = False
                    # print"************No rows - IndexError"+line
        else:
            # print "*********Records of ER800 Class but not any specified subclass :"+line
            pass
        complete_line= current_line.replace('\n', ' ')
        print complete_line
    else:
        # print "*********Not an Event Records: "+line
        pass

    


    



# nfp.write(complete_record)
# nfp.close()
f.close()
fp.close()
