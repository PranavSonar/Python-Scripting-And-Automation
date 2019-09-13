import os, datetime
from datetime import datetime, timedelta
# from java.sql import SQLException

# Local variables

dt = datetime.now() 
date_code_d = int(dt.strftime("%Y%m%d"))
date_code_d_1=date_code_d-1
date_code_d_2=date_code_d-2


# print date_code_d,date_code_d_1,date_code_d_2


file_path = os.path.join('C:\Users\Vivek Kumar\Desktop','LOCAL_FILES.txt')
# Derive the SFTP Files count from path and update the table for the files count
file_count_d=0
file_count_d_1=0
file_count_d_2=0
fp = open(file_path, "r")
for line in fp.readlines():
    columns=line.split(',')
    column=columns[0]
        # print date_code_d,column
    if str(date_code_d) in column:
        file_count_d=file_count_d+1
        
    elif str(date_code_d_1) in column:
        file_count_d_1=file_count_d_1+1

    elif str(date_code_d_2) in column:
        file_count_d_2=file_count_d_2+1
    else:
        pass

print file_count_d,file_count_d_1,file_count_d_2

# count = len([words[0] for words in [line.split(',') for line in fp.readlines()] if date_code_sc in words[0]])
# count_d_1 = len([words[0] for words in [line.split(',') for line in fp.readlines()] if date_code1 in words[0]])
# count_d_2 = len([words[0] for words in [line.split(',') for line in fp.readlines()] if date_code2 in words[0]])
# print count,count_d_1,count_d_2,date_code,date_code1,date_code2
fp.close()













# file_name = '<%=odiRef.getOption("SNAPSHOT_FILENAME")%>'

# Form the DB connection
# src_conn = odiRef.getJDBCConnection("SRC")
# sql_stmt = src_conn.createStatement()

# sel_query = """SELECT file_path path, market_id
#   FROM {MAIN_REPO}.im.{MAIN_REPO}.audit_dirs
#  WHERE     enabled_flag = 'Y'
#        AND sftp_enabled = 'Y'
#        AND path_type = 'LOG'
#        """

# Execute the query and open a cursor
# try:
    # paths_cur = sql_stmt.executeQuery(sel_query)
    # Loop for Paths in the cursor
    # while paths_cur.next():
    #     path = paths_cur.getString("PATH")
        # file_path = os.path.join(path,file_name)
        # file_path = os.path.join('C:\Users\Vivek Kumar\Desktop','LOCAL_FILES.txt')
        # # Derive the SFTP Files count from path and update the table for the files count
        # fp = open(file_path, "r")
        # count = len([words[0] for words in [line.split(',') for line in fp.readlines()] if date_code_sc in words[0]])
        # count_d_1 = len([words[0] for words in [line.split(',') for line in fp.readlines()] if date_code1 in words[0]])
        # count_d_2 = len([words[0] for words in [line.split(',') for line in fp.readlines()] if date_code2 in words[0]])
        # fp.close()

        # update the record count
        # upd_stmt = src_conn.createStatement()
    #     upd_query = """UPDATE {MAIN_REPO}.im.{MAIN_REPO}.audit_dirs
    # SET SFTP_FILES_COUNT = %d
    #   , SFTP_FILES_COUNT_D1 = %d
    #   , SFTP_FILES_COUNT_D2 = %d
    #   , sftp_date_code = '%s'
    #   , last_update_date = SYSDATE
    # WHERE enabled_flag = 'Y' 
    #   AND sftp_enabled = 'Y' 
    #   AND file_path = '%s' 
    #   AND market_id = %d""" % (count,count_d_1,count_d_2,date_code,path,paths_cur.getInt("MARKET_ID"))
            
    #     # Update the table
    #     try:
    #         upd_stmt.executeUpdate(upd_query)
    #         upd_stmt.close()
    #     except SQLException, se:
    #         raise "SQL Exception : %s for query : %s" % (se, upd_query)
         

        
#     # Close the cursor
#     paths_cur.close()
# except SQLException, se:
#     raise "SQL Exception : %s for query : %s" % (se, sel_query)
# except Exception, e:
#     raise "Exception : %s" %(e)
    
# # Close the connection
# sql_stmt.close()
# src_conn.close()
