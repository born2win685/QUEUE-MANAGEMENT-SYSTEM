import numpy as np
import pandas as pd
import queuesimulation as qs

s = qs.Queue()
# making a pandas dataframe to store simulated data
df = pd.DataFrame(columns=['Average interarrival time', 'Average service time teller1', 'Average service time teller 2',
                           'Utilization teller 1', 'Utilization teller 2', 'People who had to wait in line',
                           'Total average wait time', 'Lost Customers'])

for i in range(10):
    np.random.seed(i)
    s.__init__() # we initialize the object each time after we have chosen a seed for random numbers
    print(qs.gen_int_arr())
    while s.clock <= 240: # we are running simulations for a total duration of 4 hrs
        s.time_routines() # calling time_routines() each time to decide the next event and run the simulation accordingly

    a = pd.Series(
        [s.clock / s.no_of_arrivals, s.dep_sum_time1 / s.num_of_departures1, s.dep_sum_time2 / s.num_of_departures2,
         s.dep_sum_time1 / s.clock, s.dep_sum_time2 / s.clock, s.total_cust_in_q, s.total_wait_time, s.lost_customers],
        index=df.columns)
    df = df.append(a, ignore_index=True)

df.to_csv('statistics.csv')

