def date_time():
  import time,datetime
  print(time.time()) #now in timestamp
  print(datetime.datetime.now()) #now in datetime
  print(datetime.date.today()) #today in date
  print(datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time())) #date to datetime
  print(datetime.datetime.now().date()) #datetime to date
  print(datetime.datetime.strptime('202104', '%Y%m')) #string to datetime
  print(datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d')) #datetime to string
  print(datetime.datetime.now().timestamp()) #datetime to timestamp
  print(datetime.datetime.fromtimestamp(time.time())) #timestamp to datetime
  print(datetime.datetime(2021,4,1)) #datetime from year,month,day
  print(datetime.datetime.now() + datetime.timedelta(days=1)) #datetime + timedelta

  print(datetime.datetime.now().replace(day=1,hour=0,minute=0,second=0,microsecond=0)) #start of month
  print((datetime.datetime.now().replace(day=1)+datetime.timedelta(days=40)).replace(day=1,hour=0,minute=0,second=0,microsecond=0)) #start of next month
  print((datetime.date.today().replace(day=1)+datetime.timedelta(days=40)).replace(day=1))
date_time() #first day of next month

def base_encode():
  alpha = '0123456789abcdefghijklmnopqrstuvwxyz'
  n,d = int('abc12',36),''
  while n!=0:
    n,m = divmod(n,36)
    d = alpha[m] + d
  print(d)
base_encode()
