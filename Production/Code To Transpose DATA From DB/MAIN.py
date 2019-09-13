import cx_Oracle 

query=(u'''SELECT
            date_Code,
            master_agent,
            transaction_count
        FROM
            TELEPIN.ACTIVE_RETAIL_AGENT_DAY_A
        WHERE
            date_Code BETWEEN '20190401' AND '20190430' and rownum<10
        ORDER BY
            date_code''')

def db_data(sqlquery):
    conn_str = u'username/password@x.x.x.139:1522/{MAIN_REPO}.xxxxx.local'
    conn = cx_Oracle.connect(conn_str)
    result = conn.cursor()
    result.execute(sqlquery)    
    return result
    conn.close()

result=db_data(query)
for row in result:
    date_Code=row[0]
    master_agent=row[1]
    transaction_count=row[2]    



