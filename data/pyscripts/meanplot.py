import fortumdata as fortum
import matplotlib.pyplot as plt

# Switch median parameter to True for median instead of mean
timewatts = fortum.get_avg('../raw.data', median=False)
times = [x[0] for x in timewatts]
watts = [x[1] for x in timewatts]
plt.plot(times, watts)

