SELECT
      *
FROM
     {MAIN_REPO}.{SUB-STREAM}_USSD_SUMM@{DEVISON}_{MAIN_REPO}.LINK WHERE MSISDN='6745588086' AND   er_DATE >= to_date('06/12/2018','dd/mm/yyyy')
      and er_DATE < to_date('08/12/2018','dd/mm/yyyy')
      
OWNER||'.'||OBJECT_NAME              |
-------------------------------------|
STAGETCB9.CTRL_{SUB-STREAM}                 |
STAGETCB9.CTRL_{SUB-STREAM}_BCK             |
{MAIN_REPO}.DIM_CHURN_TRANSACTION_BCK2802    |
{MAIN_REPO}.{SUB-STREAM}USSD                        |
STAGETCB9.{SUB-STREAM}                     |
{MAIN_REPO}.{SUB-STREAM}_383                       |
STAGE.{SUB-STREAM}_HIST                    |
STAGE.{SUB-STREAM}_TEST                    |
{MAIN_REPO}.{SUB-STREAM}_USSD                      |
{MAIN_REPO}.{SUB-STREAM}_USSD_SUMM                 |
FINANCE.ICNT_CDR_DETAIL_FCT_WS_090802|
STAGE.TEST_{SUB-STREAM}                     |      
      
      
      WHERE 
      
      FILENAME LIKE '%PP.20181207.35743%'


SELECT
      *
FROM
      {MAIN_REPO}.{SUB-STREAM}_USSD_FS
      
      SELECT * FROM STAGETCB9.CTRL_{SUB-STREAM}@{DEVISON}_{MAIN_REPO}.link WHERE FILE_NAME_RAW  LIKE '%20181207%35743%'
      
      PP.20181207.35743
      
PRIMARYKEY|FK_{ORG}_COUNTRY|NODE|FILE_NAME_RAW    |FTP_RECORDS|FTP_CREATEDATE     |NUMBER_OF_RECORDS|LOADDATE           |
----------|------------------|----|-----------------|-----------|-------------------|-----------------|-------------------|
   7641694|                 3|   1|PP.20181207.35743|      22566|2018-12-07 06:31:30|            22566|2018-12-07 07:24:35|
   
   
   
   

SELECT
      owner||'.'||OBJECT_NAME
FROM
      all_objects@{DEVISON}_{MAIN_REPO}.LINK
WHERE OBJECT_type LIKE '%TABLE' AND 
      OBJECT_NAME LIKE '%802%' ORDER BY OBJECT_NAME; 





SELECT
      *
FROM
     {MAIN_REPO}.{SUB-STREAM}_USSD_SUMM@{DEVISON}_{MAIN_REPO}.LINK WHERE MSISDN='6745588086' AND   er_DATE >='2018/12/06' and er_DATE < '2018/12/08' 