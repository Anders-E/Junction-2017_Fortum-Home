from sys import stdin
from datetime import datetime
import statistics as stats

def tuple_from_line(line):
    timewatts = []
    line = line.split(';')
    t = datetime.strptime(line[0].strip(), '%Y-%m-%d %H:%M:%S')
    w = float(line[1])
    return (t, w)

def get_all(path):
    timewatts = []
    with open(path) as f:
        for line in f:
            if line[0] == '#':
                continue
            timewatts.append(tuple_from_line(line))
    return timewatts

def get_avg(path, median=False):
    timewatts = []
    timedict = {}
    with open(path) as f:
        for line in f:
            if line[0] == '#':
                continue
            timewatt = tuple_from_line(line)
            t = timewatt[0]
            t = datetime(2017, 1, 1, t.hour, t.minute, t.second)
            if t in timedict:
                timedict[t].append(timewatt[1])
            else:
                timedict[t] = [timewatt[1]]
    for key in timedict.keys():
        if median:
            timewatts.append((key, stats.median(timedict[key])))
        else:
            timewatts.append((key, stats.mean(timedict[key])))
    return timewatts

def get_range(path, date1, date2):
    timewatts = []
    with open(path) as f:
        for line in f:
            if line[0] == '#':
                continue
            timewatt = tuple_from_line(line)
            if date1 < timewatt[0] < date2:
                timewatts.append(timewatt)
            if date2 < timewatt[0]:
                break
    return timewatts

def get_day(path, month, day, weekend=True):
    timewatts = []
    with open(path) as f:
        for line in f:
            if line[0] == '#':
                continue
            timewatt = tuple_from_line(line)
            if not weekend and timewatt[0].weekday() > 4:
                continue
            if timewatt[0].day == day and timewatt[0].month == month:
                timewatts.append(timewatt)
            elif timewatt[0].day > day:
                break
    return timewatts
