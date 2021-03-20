import datetime
from queuesimulation import Queue

# use these variables at appropriate places in gui

t = 0  # assign when join is asserted

s1 = datetime.datetime.now().minute  # assign when join is asserted

s2 = datetime.datetime.now().minute  # assign when join is asserted for the subsequent time

q = Queue()

q.num_in_q # number of customers i queue

