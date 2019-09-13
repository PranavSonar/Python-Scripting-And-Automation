
s='12:45:54AM'
def timeConversion(s):
    hh=str(s).split(':',)
    if 'PM' in hh[2] and int(hh[0])!=12:
        print('Hi')
        HH=12+int(hh[0])
        if HH>=24:
            HH=HH-24
        MM=hh[1]
        SS=hh[2][:2]
        hh='%s:%s:%s' %(HH,MM,SS)
    else:
        HH=int(hh[0])
        if HH>=12 and 'AM' in hh[2]:
            HH=HH-12
        if HH==12 and 'PM' in hh[2]:
            HH=HH
        if HH<10:
            HH='0'+str(HH)
        MM=hh[1]
        SS=hh[2][:2]
        hh='%s:%s:%s' %(HH,MM,SS)
    print(hh)
timeConversion(s)