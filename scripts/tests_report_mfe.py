import time
[time.strptime(t, '%H:%M:%S') > time.strptime('14:40:00', '%H:%M:%S') for t in ["14:41:32+08:00"]]
