import os, shutil, re
from glob import glob

# get the file location
log_dir_path = '/{root}/{DEVISON}/VLR/log'.strip()
stage_dir_path = '/{root}/{DEVISON}/VLR/stage'.strip()
archive_dir_path = '/{root}/{DEVISON}/VLR/archive'.strip()
# Go to files directory and read the file
os.chdir(log_dir_path)
for filename in glob('{ORG} {Devison}oa MSC VLR*.log'):
    # Delete empty files
    if os.path.getsize(filename) == 0:
        os.remove(filename)
        continue  # Skip to other file
    new_filename = filename.replace('.log', '.txt').replace(' ','_')
    fp = open(filename, 'r')
    nfp = open(new_filename, "w")
    # setting initially all variable value false or null
    part_1_flag = False
    part_2_flag = False
    part_3_flag = False
    imsi = ''
    msisdn = ''
    state = ''
    date = ''
    time = ''
    cgi = ''
    imei = ''
    current_record = ''
    complete_record = ''
    # Start reading the complete file
    for line in fp.readlines():
        # remove extra space from begging and ending place of line
        line = line.strip()
        # if next read line true for any
        if part_1_flag:
            # split the current line and store the length
            part_1 = line.split()
            part_length = part_1.__len__()
            # check if required field are available
            # if available then put each of them in respective variable
            if part_length >= 3:
                imsi = str(part_1[0].strip())
                msisdn = str(part_1[1].strip())
                state = str(part_1[2].strip())
            elif part_length == 2:
                imsi = str(part_1[0].strip())
                msisdn = str(part_1[1].strip())
            elif part_length == 1:
                imsi = str(part_1[0].strip())
            # after reading line it set flag to false for next all line
            part_1_flag = False

        if part_2_flag:
            part_2 = line.split()
            part_length = part_2.__len__()
            if part_length >= 3:
                date = str(part_2[0].strip())
                time = str(part_2[1].strip())
                cgi = str(part_2[2].strip())
            elif part_length == 2:
                date = str(part_2[0].strip())
                time = str(part_2[1].strip())
            elif part_length == 1:
                date = str(part_2[0].strip())
            part_2_flag = False

        if part_3_flag:
            part_3 = line.strip()
            part_length = part_3.__len__()
            # checking if part_3 having some value
            if part_length:
                imei = str(part_3.strip())
            part_3_flag = False

        # check if current_record starting pointer found set all variable value false or null
        if '<MGSSP:IMSI' in line:
            # print 'start found : ' + line
            imsi = ''
            msisdn = ''
            state = ''
            date = ''
            time = ''
            cgi = ''
            imei = ''
            current_record = ''
            part_1_flag = False
            part_2_flag = False
            part_3_flag = False
        # check if required field found in line then set read next line true
        if 'IMSI             MSISDN           STATE' in line:
            part_1_flag = True
        elif 'DATE             TIME             CGI' in line:
            part_2_flag = True
        elif 'IMEISV' in line:
            part_3_flag = True
        # checking if current_record ending pointer meet
        elif 'END' in line:
            # print 'END found : ' + line
            # it will form current complete record and add it to complete_record
            current_record = str(
                imsi + ',' + msisdn + ',' + state + ',' + date + ',' + time + ',' + cgi + ',' + imei + '\n')
            complete_record += current_record

        # other then start,end or required line it will skip line
        else:
            # print 'Current processing : ' + line
            pass

    # print current_record
    # print complete_record
    nfp.write(complete_record)

    nfp.close()
    fp.close()
  
    # Delete the original file replace with new file
    os.chdir(log_dir_path)
    # print filename
    os.system("chmod 777 " +new_filename)
    # os.remove(filename)
    shutil.move(new_filename,stage_dir_path)
    shutil.move(filename,archive_dir_path)
