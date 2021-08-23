from datetime import datetime
from time import mktime
import pandas as pd

df = pd.read_csv('smsdb.csv')

cocoatimestamps = df['cocoa']

convertedcocoa=[]

for i in cocoatimestamps:
        startdate = datetime(2001, 1, 1, 0, 0, 0, 0, tzinfo=None)
        starttounix = int(mktime(startdate.timetuple()))
        converted = starttounix + i
        convertedcocoa.append(converted)

print(len(convertedcocoa))

cc = pd.Series(convertedcocoa)
cc.to_csv('test.csv')
