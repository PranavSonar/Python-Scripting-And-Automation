import datetime

t = datetime.time(5, 25, 1)

print(t)
# t.minute=7


print(t.max)
print(t.resolution)

print(datetime.date.today())

print(datetime.datetime.max)

d1=datetime.date(2019,12,3)
print(d1)

print(d1.replace(2018))



d1=datetime.date.today()
d2=datetime.date(1997,11,5)
print(year(d1-d2))