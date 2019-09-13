

FILENAME |LOG_DATE |STATUS |SESSION_NO |START_DATE |END_DATE |ARCHIVE_DATE  |FILENAME |DATE_CODE |NUMBER_OF_RECORDS |FILENAME |DATE_CODE |NUMBER_OF_RECORDS |FILENAME |DATE_CODE |NO_OF_RECORDS |CURRENT_STATUS |
---------|---------|-------|-----------|-----------|---------|------------- |---------|----------|------------------|---------|----------|------------------|---------|----------|--------------|---------------|
SELECT *
FROM {ODI_WORK_REPO}.FILENAME_STATUS_VLR_{DEVISON} , {ODI_WORK_REPO}.FILEAUDIT_PRELOAD_VLR_{DEVISON}, {ODI_WORK_REPO}.FILEAUDIT_POSTLOAD_VLR_{DEVISON}, {ODI_WORK_REPO}.FILEAUDIT_POSTMAST_VLR_{DEVISON};




# Method to check if File was already archived
def check_archive_file():
    # Check if file is already Archived earlier
    l_query = "SELECT 'Y' status FROM %s WHERE status = 'ARCHIVED' AND filename = '%s'" % (status_table, filename)
    l_status = "N"
    try:
        result_arc = sql_stmt.executeQuery(l_query) 
        try:
            while result_arc.next():
                l_status=result_arc.getString(1)
            result_arc.close()
            
        except SQLException, se:
            print se
        return l_status
    except Exception, e:
        raise 'Exception with query : %s - %s' %(l_query,e)
       
# Check the entries stuck in PICKED status 
def check_picked_file():
    l_query = "DELETE %s WHERE status = 'PICKED' AND filename = '%s' AND log_date < (SYSDATE - 4/24)" % (status_table, filename)
    try:
        sql_stmt.executeUpdate(l_query)
    except Exception, e:
        raise 'Exception with query : %s - %s' %(l_query,e)
      
# Check the entries stuck in PICKED status       
def check_processed_file():
    # Check if file is already Processed earlier but was not entered in PostMast and PostLoad
    l_query = "SELECT filename FROM %s WHERE status = 'PROCESSED' AND filename = '%s' AND log_date < (SYSDATE - 4/24)" % (status_table, filename)
    try:
        result_proc = sql_stmt.executeQuery(l_query)
        try:
            while result_proc.next():
                # Check in PostMast for the file
                l_query = "SELECT 'Y' FROM %s WHERE filename = '%s'" %(postmast_table,filename)
                filename_result=sql_stmt.executeQuery(l_query)
                l_status = ""
            
                try:
                    while filename_result.next():
                        l_status = filename_result.getString(1)
                except SQLException, se:
                    print se
                filename_result.close()
                    
                if (l_status == ""):
                    # No entry in PostMast, Session got interrupted while inserting into FS table. No entry made in FS table
                    l_query = "DELETE %s WHERE status = 'PROCESSED' AND filename = '%s'" %(status_table,filename)
                    sql_stmt.executeUpdate(l_query)
                if (l_status == "Y"):
                    # Session got interrupted while archiving file, Update status to Archive and move
                    l_query = "UPDATE %s SET status = 'ARCHIVED' , archive_date = SYSDATE WHERE filename = '%s'" %(status_table,filename)
                    sql_stmt.executeUpdate(l_query)
                    shutil.move(file,arch_dir)
                result_proc.close()
        except SQLException, se:
            print se
    except Exception, e:
        raise 'Exception with query : %s - %s' %(l_query,e)
    
def insert_preaudit(p_date_code):
    # Check if file is already Archived earlier
    l_query = """INSERT INTO %s
                 SELECT '%s','%s','%s' FROM DUAL
                  WHERE NOT EXISTS 
                    (SELECT 1 
                       FROM %s 
                      WHERE filename = '%s' AND date_code = '%s')""" % (audit_tablename, filename, p_date_code, rec_count, audit_tablename, filename, p_date_code)
    try:
        sql_stmt.executeUpdate(l_query)
    except Exception, e:
        raise 'Exception with query : %s - %s' %(l_query,e)
    
# Insert the file name in status table    
def insert_status():
    # Delete any previous entry of the file if already BLOCKED
    l_query = "DELETE %s WHERE filename = '%s' AND session_no <> %s AND status IN ('BLOCKED','ERROR')" % (status_table, filename, session_num );
    try:
        sql_stmt.executeUpdate(l_query)
    except Exception, e:
        raise 'Exception with query : %s - %s' %(l_query,e)
    
    # Insert new entry
    l_query = """INSERT INTO %s a ( filename, log_date, status, session_no )
                SELECT '%s'
                     , SYSDATE
                     , 'BLOCKED'
                     , %s
                  FROM DUAL
                 WHERE NOT EXISTS
                           (SELECT 1
                              FROM %s b
                             WHERE     b.filename = '%s'
                                   AND b.session_no <> %s
                                   AND b.status IN ('PICKED', 'PROCESSED', 'ARCHIVED'))""" % (status_table, filename, session_num, status_table, filename, session_num)
    
    try:
        sql_stmt.executeUpdate(l_query)
    except Exception, e:
        raise 'Exception with query : %s - %s' %(l_query,e)
    
# Main Flow        
os.chdir(build_dir)

# Check the bad files present in the folder
files = glob(badfile_pattern)
files.extend(glob(errfile_pattern))
for file in files:
    # Move bad files
    filename = os.path.basename(file)
    # if re.match(r".*\.bad.*", filename):
    shutil.move(file, bad_dir)
    
# Form the DB connection
src_conn = odiRef.getJDBCConnection("SRC")
sql_stmt = src_conn.createStatement()

# Goto files directory to get the file List
files = glob(file_pattern)
print 'Build : %s - File %s - Bad File : %s - Error File : %s' % (build_dir, file_pattern,badfile_pattern,errfile_pattern)
for file in files:
    filename = os.path.basename(file)
    print 'File %s  -  File name : %s' % (file,filename)
    # Delete empty files
    if os.path.getsize(file) == 0:
        os.remove(file)
        continue  # Skip to other file
        
    status = check_archive_file()
    # Move the file to Archive folder if file was processed earlier
    if status == "Y":
        shutil.move(file, arch_dir)
        continue  # Skip to other file
        
    check_picked_file()
    check_processed_file()
    
    fp=None
    try:
        fp = open(file, 'r')
        result = []
        for lines in fp.readlines():

            coldet = lines.split(fs)[col_pos]
            # If no Datecode then continue to next line
            if  coldet == "":
                continue
            
            year_str = date_str = month_str = day_str = ""
            coldet = coldet[0:10].replace("-", "/")  # New for SGSN
            if (date_format.upper() == "YYYY/MM/DD"):
                year_str = coldet.split("/")[0]
                month_str = coldet.split("/")[1]
                if (len(month_str) == 1):
                    month_str = '0' + month_str
                day_str = coldet.split("/")[2]
                if (len(day_str) == 1):
                    day_str = '0' + day_str
            elif (date_format.upper() == "YYYY/DD/MM"):
                year_str = coldet.split("/")[0]
                month_str = coldet.split("/")[2]
                if (len(month_str) == 1):
                    month_str = '0' + month_str
                day_str = coldet.split("/")[1]
                if (len(day_str) == 1):
                    day_str = '0' + day_str
            elif (date_format.upper() == "MM/DD/YYYY"):
                year_str = coldet.split("/")[2]
                month_str = coldet.split("/")[0]
                if (len(month_str) == 1):
                    month_str = '0' + month_str
                day_str = coldet.split("/")[1]
                if (len(day_str) == 1):
                    day_str = '0' + day_str
            elif (date_format.upper() == "DD/MM/YYYY"):
                year_str = coldet.split("/")[2]
                month_str = coldet.split("/")[1]
                if (len(month_str) == 1):
                    month_str = '0' + month_str
                day_str = coldet.split("/")[0]
                if (len(day_str) == 1):
                    day_str = '0' + day_str
            date_str = year_str + month_str + day_str
            result.append(date_str)
            prev_value = curr_value = ""
            actual_count = []

        # Sort the Result and save in Audit table
        for i in sorted(result):
            curr_value = i;
            if (curr_value != prev_value):
                if (prev_value != ""):
                    rec_count = result.count(prev_value)
                    # Preaudit entry
                    insert_preaudit(prev_value)
                prev_value = curr_value

        # Insert data into table
        rec_count = result.count(curr_value)
        # Preaudit entry
        insert_preaudit(curr_value)
        # Status Table entry
        insert_status()
        
        fp.close()
    except IOError:
        print "File Not Found : %s" % (file)
    except OSError:
        print "File Not Found : %s" % (file)
    except IndexError:
        print "Index out of range for file : %s" % (file)
    except Exception, e:
        raise e
    
# Close the connection
sql_stmt.close()
src_conn.close()


