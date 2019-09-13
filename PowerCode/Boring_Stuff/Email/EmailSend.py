import smtplib
conn=smtplib.SMTP('smtp.gmail.com',587)
print(type(conn))
conn.ehlo()
conn.starttls()
conn.login('xxx@gmail.com','password')
conn.sendmail('from@gmail.com','to@gmail.com','Subject:So long subject...\n\nIt a long body part')
conn.quit()
