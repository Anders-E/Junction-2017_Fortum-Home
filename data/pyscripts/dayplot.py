import fortumdata as fortum
import matplotlib.pyplot as plt

timewatts = fortum.get_all('../day.data')
times = [x[0] for x in timewatts]
watts = [x[1] for x in timewatts]
plt.plot(times, watts)
plt.gcf().autofmt_xdate()
plt.show()

