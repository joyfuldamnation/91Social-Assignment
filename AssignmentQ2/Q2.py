# Write a Python program to calculate the number of days between two dates.
from datetime import date
def daysbwdates(date1,date2):
    y1=date1//10000
    m1=(date1-y1*10000)//100
    d1=date1%100
    y2=date2//10000
    m2=(date2-y2*10000)//100
    d2=date2%100
    ini_date = date(y1, m1, d1)
    fin_date = date(y2, m2, d2)
    diff = fin_date - ini_date
    return diff.days
print(daysbwdates(20200702,20200711)