#
#
#
#
#
#
#
import datetime
from itertools import groupby
from collections import defaultdict
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib.dates import date2num, num2date


f = open('/Users/anvika/Downloads/perch_data_output (1).txt', 'r')
# file_contents = "2016-11-28 21:11:53.798749,2016-11-28 23:26:45.436094,2016-11-28 23:27:01.278436,2016-11-28 23:27:02.073281,2016-11-28 23:27:44.244016,2016-11-28 23:27:44.245053,2016-11-28 23:27:54.346078,2016-11-28 23:27:56.590600,2016-11-28 23:27:59.505157,2016-11-28 23:28:07.110551,2016-11-28 23:28:07.111789,2016-11-28 23:28:09.202434,2016-11-28 23:28:11.173718,2016-11-29 00:16:59.826652,2016-11-29 00:17:01.244385,2016-11-29 00:17:12.355762,2016-11-29 00:17:12.356526,2016-11-29 00:17:13.741113,2016-11-29 00:17:13.741916,2016-11-29 00:17:58.176260,2016-11-29 00:18:04.744747,2016-11-29 00:18:04.745527"
# f.readlines()
# f = file_contents.split(",")
count = 0
total = 0
count1 = 0
res = []
for i in range(len(f)):
    for j in range(i + 1, len(f)):
        print "I am printing i", i
        print "I am printing j", j
        sep = '.'
        rest = f[i].split(sep)[0]
        rest1 = f[j].split(sep)[0]
        a = datetime.datetime.strptime(rest, '%Y-%m-%d %H:%M:%S')
        b = datetime.datetime.strptime(rest1, '%Y-%m-%d %H:%M:%S')
        if (a.date() == b.date()):
            # difference = relativedelta.relativedelta(b, a)
            diff = (b - a).seconds
            print "Subtracting", diff
            if (diff > 60):
                count = count + 1
                i = i + 1
            res.append((str(a.date()), count))
            print "final count after each iteration", count
        else:
            print "Hello", i
            count = 0
        print "I am trying", count
key1 = []
value = []
print count
print res
for key, group in groupby(res, key=lambda x: x[0][:10]):
    c = sum(j for i, j in group)
    print c, "I am printing c"
    key1.append(datetime.datetime.strptime(key, "%Y-%m-%d").date())
    value.append(c)


num_dates = [date2num(d) for d in key1]
print num_dates
plt.plot(num_dates, value)

# Average for all customers:
count = 0
total = 0
res = []
for i in range(len(f)-1):
        sep = '.'
        rest = f[i].split(sep)[0]
        rest1 = f[i+1].split(sep)[0]
        a = datetime.datetime.strptime(rest, '%Y-%m-%d %H:%M:%S')
        b = datetime.datetime.strptime(rest1, '%Y-%m-%d %H:%M:%S')
        if(a.date() == b.date() and (i+1)<len(f)):
            diff = (b - a).seconds
            if (diff < 60):
                count = count + 1
                print count, "I am printing count"
                total = total + diff
        else:
            avg = total/count
            total = 0
            count = 0
            print "I am printing average",avg

avg = total/count
print "I am printing average",avg



