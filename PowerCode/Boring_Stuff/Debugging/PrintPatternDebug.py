import traceback,os
def boxprint(symbol,width,hight):
    if len(symbol)!=1:
        raise Exception("'SYMBOL' Need to be a string of length 1.")
    if (width<2 or hight<2):
        raise Exception("'Width and HIght' mustr be greater then 2.")
    print(symbol*width)
    for i in range(hight-2):
        print(symbol+' '*(width-2)+symbol)
    print(symbol*width)
    # write error on log file
    try:
        raise Exception("'SYMBOL' Need to be a string of length 1.")
    except:
        errorLogFile=open('error_log.log','a')
        errorLogFile.write(traceback.format_exc())
        errorLogFile.close()
        print('The Traceback is written at '+os.getcwd())
boxprint('*',3,3)