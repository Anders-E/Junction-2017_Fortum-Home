import fortumdata as fortum
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ALL DAYS 2-6 OCTOBER SUPERIMPOSED
for day in range(2, 7):
timewatts = fortum.get_day('../raw.data', 10, day)
times = [x[0] - timedelta(days=day) for x in timewatts]
watts = [x[1] for x in timewatts]
plt.plot(times, watts)


