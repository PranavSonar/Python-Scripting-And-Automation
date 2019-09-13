# import all required lib
import os, shutil
from glob import glob
# Import the email modules we'll need
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Import smtplib for the actual sending function
import smtplib

# from java.sql  import SQLException

# open database connection
# src_conn = odiRef.getJDBCConnection("SRC")
# sql_stmt = src_conn.createStatement()

# Global variables
# set email variables value based on mode of exectution of program
program_mode = 'TEST'.strip().upper()

if program_mode == 'TEST':
    mail_to = "vivek.kumar@{OrgMain}.com"
    mail_from = "ETLTestTeam"
# check if program in production mode
elif program_mode == 'PROD':
    mail_to = "{emailuser}{OrgMain}.com"
    mail_from = "ETLSupportTeam"
mail_subject = None
mail_body = None

# All Dir of Used by PKG
current_pkg = 'Test Mode PKG'
dir_log = '/{root}/{DEVISON}/VLR/log'.strip()
dir_stage = '/{root}/{DEVISON}/VLR/stage'.strip()
dir_build = '/{root}/{DEVISON}/VLR/build'.strip()
dir_arch = '/{root}/{DEVISON}/VLR/archive'.strip()
dir_darchive = '/{root}/{DEVISON}/VLR/darchive'.strip()
dir_badfiles = '/{root}/{DEVISON}/VLR/badfiles'.strip()

# ODI variable -- we set it
current_file_name = '{SUB-STREAM}_FILENAME_TEST.txt'.strip()

# ODI Variables -default
current_session_id = 534343
current_session_name = 'S_PKG_611_TEST'.strip()
current_step_name = 'Mapping_stage_611_test'.strip()
current_message = 'HI, This is a current error test message'.strip()

# Extra Variable
col_pos = 19

table_audit = 'AUDIT_TABLE_NAME_TEST'.strip()
table_status = 'STATUS_TABLE_NAME_TEST'.strip()
table_postload = 'POSTload_TABLE_NAME_TEST'.strip()
table_postmast = 'POSTMASTER_TABLE_NAME_TEST'.strip()
table_staging='Staging_TABLE_NAME_TEST'.strip()
column_name_staging_table_datefield='date_code_dt'.strip()
date_format = 'YYYYMMDD'.strip()
file_pattern = '*.txt'.strip()
badfile_pattern = '*.bad*'.strip()
errfile_pattern = '*.current*'.strip()
field_sep = ','.strip()


# ----------------------------user defiened function which will used in main program---------------------

# Database opertaion
# to perfrom select statement on database
def db_select(query):
    try:
        print "Insert  statement called"
        print query
        # sql_stmt.executeQuery(query)
    except Exception, e:
        raise 'Exception with query : %s - %s' % (query, e)


# function to perfrom insert, update, delete and drop operation on database
def db_insert_update_delete(query):
    try:
        print "Insert  statement called"
        print query
        # sql_stmt.executeUpdate(query)
    except Exception, e:
        raise 'Exception with query : %s - %s' % (query, e)


# function to send mail only need to pass mail subject and body content
# send_mail(mail_subject,mail_body)
def send_alert_mail(mail_subject, mail_body):
    # formation of proper mail content
    final_subject = ' ODI issue in '+current_pkg+' is '+mail_subject+' on Master Procedure'
    final_body="Hi {MAIN_REPO}.Team,\n \nLook like ODI facing Some issue following are the issue details.\n \n"+mail_body+"\n \nThanks,\nODI/ETL Team"
    # Create a text/plain message
    MSG = MIMEMultipart()
    # Email Details
    MSG['From'] = mail_from
    MSG['To'] = mail_to
    MSG['Subject'] = final_subject
    MSG.attach(MIMEText(final_body, 'plain'))
    # Send the message via our own SMTP server, but don't include the envelope header.
    server = smtplib.SMTP(host="X.X.X.244", port=25)
    server.sendmail(MSG['From'], MSG['To'], MSG.as_string())

# ------------------------------------------------------------------------------------------------------
print 'Greetings Master Program Started - ' +current_pkg.upper()+ ' with '+program_mode.upper()+ ' Mode All Alert will send from :'+mail_from.upper()+' TO: '+mail_to.upper()
task = (raw_input('Enater Task: ')).upper().strip()
print  "YOU HAVE ENTERED : " + task

all_task = True
while all_task:
    if task == 'T1':
        print 'Block File Started'
        del_query = "DELETE %s WHERE filename = '%s' AND session_no <> %s AND status IN ('BLOCKED','ERROR')" % (
        table_status, current_file_name, current_session_id)
        print "calling insert statement"
        db_insert_update_delete(del_query)

        # block procedure code came here

        break
    elif task == 'T2':
        print 'File Process Started Audit'
        updt_query="Update %s set status =  'PICKED',start_date = SYSDATE   WHERE filename = '%s' AND session_no = %s" % (table_status, current_file_name, current_session_id)
        db_insert_update_delete(updt_query)
        # -- Update_File_Start_{DEVISON}
        # Update <%=odiRef.getOption("TABLE_NAME")%> set status =  'PICKED',start_date = SYSDATE   WHERE filename = '<%=odiRef.getOption("FILENAME")%>' AND session_no = <%=odiRef.getOption("SESS_NO")%>

        break
    elif task == 'T3':
        print 'File Load Stage Sucess'
        updt_query = "Update %s set status = 'PROCESSED',end_date = SYSDATE   WHERE filename = '%s' AND session_no = %s" % (table_status, current_file_name, current_session_id)
        db_insert_update_delete(updt_query)
        #         -- UpdateFileSuccess_{DEVISON}
        #         -- UpdateFileStatus
        #         Update <%=odiRef.getOption("TABLE_NAME")%>  set status = 'PROCESSED',end_date =SYSDATE WHERE session_no = <%=odiRef.getOption("SESS_NO")%>  AND filename ='<%=odiRef.getOption("FILENAME")%>'
        inst_query="INSERT INTO %s (SELECT '%s',TO_CHAR('%s','%s'),COUNT(1) FROM %s WHERE file_name = '%s' and session_no = %s GROUP BY '%s',TO_CHAR('%s','%s'))"% (table_postload, current_file_name,column_name_staging_table_datefield,date_format,table_staging,current_file_name,current_session_id,current_file_name,column_name_staging_table_datefield,date_format )
        db_insert_update_delete(inst_query)
        #         -- InsertPostLoadAudit
        #         INSERT INTO <%=odiRef.getOption("POST_LOAD_AUDIT_TABLE")%>
        # (
        # SELECT '<%=odiRef.getOption("FILENAME")%>'
        #      ,TO_CHAR(<%=odiRef.getOption("STAGING_TABLE_COLUMN_NAME")%>,'YYYYMMDD')
        #      ,COUNT(1)
        # FROM <%=odiRef.getOption("STAGING_TABLE_NAME")%>
        # WHERE file_name = '<%=odiRef.getOption("FILENAME")%>' AND session_no = <%=odiRef.getOption("SESS_NO")%>
        # GROUP BY  '<%=odiRef.getOption("FILENAME")%>'
        #      ,TO_CHAR(<%=odiRef.getOption("STAGING_TABLE_COLUMN_NAME")%>,'YYYYMMDD')
        #      )

        break

    elif task == 'T3':
        print 'File Load Master  Sucess'
        inst_query="INSERT INTO %s (SELECT '%s',date_code,count(1),'MASTER' FROM %s group by '%s',date_code,'MASTER')"% (table_postmast, current_file_name, table_staging, current_file_name)
        db_insert_update_delete(inst_query)
        # -- UpdateFileMaster_New_{DEVISON}
        # INSERT INTO <%=odiRef.getOption("POST_LOAD_AUDITMASTER_TABLE")%>
        # (
        # SELECT '<%=odiRef.getOption("FILENAME")%>'
        #      ,date_code
        #      ,COUNT(1)
        #      ,'MASTER'
        # FROM <%=odiRef.getOption("STAGE_TABLE_NAME")%>
        # group by
        # '<%=odiRef.getOption("FILENAME")%>'
        #      ,date_code
        #      ,'MASTER'
        # )

        break

    # file zip and move to archive dir after processing
    elif task == 'T4':
        print "File Archive called"
        # OdiOSCommand "-CAPTURE_OUT_STREAM=ON_ERROR,10,50" "-CAPTURE_ERR_STREAM=ON_ERROR,10,50"
        # # gzip /{root}/{DEVISION}/ER/{SUBSTREAM}/build/#PNG.v_filename_{SUBSTREAM}_{DEVISON}
        # mv /{root}/{DEVISION}/ER/{SUBSTREAM}/build/#PNG.v_filename_{SUBSTREAM}_{DEVISON}.gz /{root}/{DEVISION}/ER/{SUBSTREAM}/archive/

        # After archiving done it will update the status table 'Archive'
        # -- UpdateFileArchive_{DEVISON}
        print 'Archived Sucess'
        updt_query="Update %s set status = 'ARCHIVED',archive_date = SYSDATE   WHERE filename = '%s' AND session_no = %s" % (table_status, current_file_name, current_session_id)
        db_insert_update_delete(updt_query)
        # Update <%=odiRef.getOption("TABLE_NAME")%> set status = 'ARCHIVED',archive_date =SYSDATE WHERE session_no = <%=odiRef.getOption("SESS_NO")%> AND filename ='<%=odiRef.getOption("FILENAME")%>'

        break
    else:  # default, could also just omit condition or 'if True'
        print "You Have selected wrong Option!"
        break

# Close the connection with database
# sql_stmt.close()
# src_conn.close()
