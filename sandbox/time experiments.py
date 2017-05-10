import time

localTime = time.localtime(time.time())

year = localTime.tm_year
month = localTime.tm_mon
day = localTime.tm_mday
hour = localTime.tm_hour
minute = localTime.tm_min
second = localTime.tm_sec


"""The date / time string has to be escaped so that it can be put into a URL.
So, for instance,

  2001-01-01 10:32:35

   becomes

  2000-01-01+10%3A32%3A35

  See http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol

"""
dateTimeString = "%d-%02d-%02d+%02d%s%02d%s%02d" % (year, month, day, hour,
                                                    "%3A", minute, "%3A", second)

print("The date-time string is", dateTimeString)
