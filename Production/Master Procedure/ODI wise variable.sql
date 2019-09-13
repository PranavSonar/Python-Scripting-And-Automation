# All Dir of Used by PKG
log_dir='<%=odiRef.getOption("LOG_DIR")%>'.strip()
stage_dir='<%=odiRef.getOption("STAGE_DIR")%>'.strip()
build_dir='<%=odiRef.getOption("BUILD_DIR")%>'.strip()
arch_dir='<%=odiRef.getOption("ARCH_DIR")%>'.strip()
darchive_dir='<%=odiRef.getOption("DARCHIVE_DIR")%>'.strip()
badfiles_dir='<%=odiRef.getOption("BADFILES_DIR")%>'.strip()



# ODI variable -- we set it
# current_file_name= #PNG.v_filename_{SUBSTREAM}_{DEVISON}

# ODI Variables -default
# session_num = <%=odiRef.getSession("SESS_NO")%>
# current_session_id= <%=odiRef.getSession("SESS_NO")%>
# current_session_name =<%=odiRef.getSession("SESS_NAME")%>
# current_step_name = <%=odiRef.getPrevStepLog("STEP_NAME")%>
# current_message=<%=odiRef.getPrevStepLog("MESSAGE")%>

# Extra Variable
# col_pos = int('<%=odiRef.getOption("COLUMN_POSITION")%>') - 1
# date_format = '<%=odiRef.getOption("DATE_FORMAT")%>'
# audit_tablename = '<%=odiRef.getOption("AUDIT_TABLE")%>'.strip()
# status_table = '<%=odiRef.getOption("STATUS_TABLE")%>'.strip()
# postmast_table = '<%=odiRef.getOption("POSTMAST_TABLE")%>'.strip()
# file_pattern = os.path.join(build_dir,'<%=odiRef.getOption("PATTERN")%>')
# badfile_pattern = os.path.join(build_dir,'*.bad*')
# errfile_pattern = os.path.join(build_dir,'*.current*')
# fs = '<%=odiRef.getOption("FIELD_SEP")%>'.strip()
