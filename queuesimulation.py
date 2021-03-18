import numpy
import tkinter as tk
import time
import datetime
import pandas as pd

def gen_int_arr():
    return -numpy.log(1 - (numpy.random.uniform(low=0.0, high=1.0))) * 3


def gen_service_time_teller1():
    return -numpy.log(1 - (numpy.random.uniform(low=0.0, high=1.0))) * 10


def gen_service_time_teller2():
    return -numpy.log(1 - (numpy.random.uniform(low=0.0, high=1.0))) * 10


class Queue:
    def __init__(self):
        self.clock = 0.0  # keeps track of time
        self.no_of_arrivals = 0  # gives the total no of arrivals till now
        self.time_arrival = gen_int_arr()  # time for next arrival
        self.time_leaving_count1 = float('inf')  # time when a customer leaves counter 1,float('inf') denotes infinity,
        # initially a departure event is scheduled at infinity to ensure first event is arrival'''
        self.time_leaving_count2 = float('inf')  # time when a customer leaves counter 2
        self.dep_sum_time1 = 0  # Sum of service times by teller 1
        self.dep_sum_time2 = 0  # Sum of service times by teller 2
        self.state_count1 = 0  # current state of counter 1(binary)
        self.state_count2 = 0  # current state of counter 2(binary)
        self.total_wait_time = 0.0
        self.num_in_q = 0  # current no of customers in queue
        self.total_cust_in_q = 0  # no of customers who stood in queue
        self.num_of_departures1 = 0  # number of customers served in counter 1
        self.num_of_departures2 = 0  # number of customers served in counter 2
        self.lost_customers = 0  # customers who left without service

    def time_routines(self):
        next_event_time = min(self.time_leaving_count1, self.time_leaving_count2,
                              self.time_arrival)  # the time at which the next event occurs
        self.total_wait_time += (self.num_in_q * (next_event_time - self.clock))  # calculating the total wait time
        self.clock = next_event_time  # Clock is set to time of the next event taking place

        if self.time_arrival < self.time_leaving_count1 and self.time_arrival < self.time_leaving_count2:
            self.arrival()  # if arrival time is less than departure from both the counters
        elif self.time_leaving_count1 < self.time_arrival and self.time_leaving_count1 < self.time_leaving_count2:
            self.counter1dep()  # if departure time of counter 1 is less than arrival and departure time of counter 2
        else:
            self.counter2dep()  # if departure time of counter 2 is less than arrival and departure time of counter 1

    def arrival(self):
        self.no_of_arrivals += 1
        if self.num_in_q == 0:
            if self.state_count1 == 1 and self.state_count2 == 1:  # waits if both tellers are busy
                self.num_in_q += 1
                self.total_cust_in_q += 1
                self.time_arrival = self.clock + gen_int_arr()  # generates arrival time
            elif self.state_count1 == 0 and self.state_count2 == 0:
                if numpy.random.choice([0,1]) == 0:  # choice takes a random number from given list if num is 0 he will go to teller 1 otherwise teller 2
                    self.state_count1 = 1  # 1 implies occupied
                    self.dep_1_service = gen_service_time_teller1()  # generates service time for the customer
                    self.dep_sum_time1 += self.dep_1_service  # total service time provided by teller 1 increases by dep_1_service
                    self.time_leaving_count1 = self.clock + self.dep_1_service
                    self.time_arrival = self.clock + gen_int_arr()  # deciding next arrival
                else:
                    self.state_count2 = 1  # 1 implies occupied1
                    self.dep_2_service = gen_service_time_teller2()  # generates service time for the customer
                    self.dep_sum_time2 += self.dep_2_service  # total service time provided by teller 1 increases by dep_1_service
                    self.time_leaving_count2 = self.clock + self.dep_2_service
                    self.time_arrival = self.clock + gen_int_arr()  # deciding next arrival
            elif self.state_count1 == 0 and self.state_count2 == 1:
                self.dep_1_service = gen_service_time_teller1()
                self.dep_sum_time1 += self.dep_1_service
                self.time_leaving_count1 = self.clock + self.dep_1_service
                self.time_arrival = self.clock + gen_int_arr()
                self.state_count1 = 1
            else:
                self.dep_2_service = gen_service_time_teller2()
                self.dep_sum_time2 += self.dep_2_service
                self.time_leaving_count2 = self.clock + self.dep_2_service
                self.time_arrival = self.clock + gen_int_arr()
                self.state_count2 = 1


        elif self.num_in_q < 4 and self.num_in_q >= 1:  # if queue length is less than 4,then the customer is added to queue
            self.num_in_q += 1
            self.total_cust_in_q += 1
            self.time_arrival = self.clock + gen_int_arr()

        elif self.num_in_q == 4:  # since queue length is 4...there's equal probability of customer leaving or staying
            if numpy.random.choice([0, 1]) == 0:
                self.num_in_q += 1
                self.total_cust_in_q += 1
                self.time_arrival = self.clock + gen_int_arr()
            else:
                self.lost_customers += 1  # customer leaves :(


        elif self.num_in_q >= 5:  # since queue length is greater than 5..there 60 percent probability of customer leaving
            if numpy.random.choice([0, 1], p=[0.4, 0.6]) == 0:
                self.time_arrival = self.clock + gen_int_arr()
                self.num_in_q += 1
                self.total_cust_in_q += 1
            else:
                self.lost_customers += 1

    def counter1dep(self):
        self.num_of_departures1 += 1
        if self.num_in_q > 0:
            self.dep_1_service = gen_service_time_teller1()
            self.dep_sum_time1 += self.dep_1_service
            self.time_leaving_count1 = self.clock + self.dep_1_service
            self.num_in_q -= 1
        else:
            self.time_leaving_count1 = float('inf')
            self.state_count1 = 0

    def counter2dep(self):
        self.num_of_departures2 += 1
        if self.num_in_q > 0:
            self.dep_2_service = gen_service_time_teller2()
            self.dep_sum_time2 += self.dep_2_service
            self.time_leaving_count2 = self.clock + self.dep_2_service
            self.num_in_q -= 1
        else:
            self.time_leaving_count2 = float('inf')
            self.state_count2 = 0

    def user_time_routines(self):
        self.time_arrival = self.clock + self.user_arrival_time()
        next_event_time = min(self.time_leaving_count1, self.time_leaving_count2,
                              self.time_arrival)  # the time at which the next event occurs
        self.total_wait_time += (self.num_in_q * (next_event_time - self.clock))  # calculating the total wait time
        self.clock = next_event_time  # Clock is set to time of the next event taking place

        if self.time_arrival < self.time_leaving_count1 and self.time_arrival < self.time_leaving_count2:
            self.user_arrival()  # if arrival time is less than departure from both the counters
        elif self.time_leaving_count1 < self.time_arrival and self.time_leaving_count1 < self.time_leaving_count2:
            self.user_counter1dep()  # if departure time of counter 1 is less than arrival and departure time of counter 2
        else:
            self.user_counter2dep()  # if departure time of counter 2 is less than arrival and departure time of counter 1

    def user_arrival(self):
        self.no_of_arrivals += 1
        if self.num_in_q == 0:
            if self.state_count1 == 1 and self.state_count2 == 1:  # waits if both tellers are busy
                self.num_in_q += 1
                self.total_cust_in_q += 1
                self.time_arrival = self.clock + self.user_arrival_time()  # generates arrival time
            elif self.state_count1 == 0 and self.state_count2 == 0:
                if numpy.random.choice([0,
                                        1]) == 0:  # choice takes a random number from given list if num is 0 he will go to teller 1 otherwise teller 2
                    self.state_count1 = 1  # 1 implies occupied
                    self.dep_1_service = gen_service_time_teller1()  # generates service time for the customer
                    self.dep_sum_time1 += self.dep_1_service  # total service time provided by teller 1 increases by dep_1_service
                    self.time_leaving_count1 = self.clock + self.dep_1_service
                    self.time_arrival = self.clock + self.user_arrival_time()  # deciding next arrival
                else:
                    self.state_count2 = 1  # 1 implies occupied1
                    self.dep_2_service = gen_service_time_teller2()  # generates service time for the customer
                    self.dep_sum_time2 += self.dep_2_service  # total service time provided by teller 1 increases by dep_1_service
                    self.time_leaving_count2 = self.clock + self.dep_2_service
                    self.time_arrival = self.clock + self.user_arrival_time()  # deciding next arrival
            elif self.state_count1 == 0 and self.state_count2 == 1:
                self.dep_1_service = gen_service_time_teller1()
                self.dep_sum_time1 += self.dep_1_service
                self.time_leaving_count1 = self.clock + self.dep_1_service
                self.time_arrival = self.clock + self.user_arrival_time()
                self.state_count1 = 1
            else:
                self.dep_2_service = gen_service_time_teller2()
                self.dep_sum_time2 += self.dep_2_service
                self.time_leaving_count2 = self.clock + self.dep_2_service
                self.time_arrival = self.clock + self.user_arrival_time()
                self.state_count2 = 1


        elif self.num_in_q >= 1:  # user is added to queue
            self.num_in_q += 1
            self.total_cust_in_q += 1
            self.time_arrival = self.clock + self.user_arrival_time()


    def user_counter1dep(self):
        self.num_of_departures1 += 1
        if self.num_in_q > 0:
            self.dep_1_service = gen_service_time_teller1()
            self.dep_sum_time1 += self.dep_1_service
            self.time_leaving_count1 = self.clock + self.dep_1_service
            self.num_in_q -= 1
        else:
            self.time_leaving_count1 = float('inf')
            self.state_count1 = 0

    def user_counter2dep(self):
        self.num_of_departures2 += 1
        if self.num_in_q > 0:
            self.dep_2_service = gen_service_time_teller2()
            self.dep_sum_time2 += self.dep_2_service
            self.time_leaving_count2 = self.clock + self.dep_2_service
            self.num_in_q -= 1
        else:
            self.time_leaving_count2 = float('inf')
            self.state_count2 = 0

    def user_arrival_time(self):
        return datetime.datetime.now().minute - self.clock


# making a pandas dataframe to store simulated data
df = pd.DataFrame(columns=['Average interarrival time','People who had to wait in line',
                           'Total average wait time', 'Lost Customers'])


numpy.random.seed(2)
s = Queue()
 # we initialize the object after we have a random seed

while s.clock < (200) : # we are running simulations for 10 customers
    s.time_routines() # calling time_routines() each time to decide the next event and run the simulation accordingly
   # print(s.num_in_q)


window=tk.Tk()
window.title("IIITB BANK")
window.geometry("500x500")

def newwindow():
      
      nw=tk.Toplevel(window)
      
      
      s.user_time_routines()

      l4=tk.Label(nw,text="\nuser entered").pack()
      l5=tk.Label(nw,text="number of customers currently in queue = "+str(s.num_in_q)).pack()
      b2=tk.Button(nw,text="OK",bg="blue",fg="white",command=nw.destroy).pack()


l2=tk.Label(window,text="expected  time =" + str(s.total_wait_time)).place(x=100,y=100)
l3=tk.Label(window,text="\nnumber of customers currently in queue = "+str(s.num_in_q)).place(x=100,y=130)
b=tk.Button(text="JOIN THE QUEUE",fg="white",bg="black",command=newwindow).place(x=200,y=220)
l1=tk.Label(window,text=" WELCOME",font="helvetica,400").pack()




window.mainloop()

a = pd.Series(
            [s.clock / s.no_of_arrivals,
             s.total_cust_in_q, s.total_wait_time, s.lost_customers],
             index=df.columns)

# writing the obtained simulated data in a pandas dataframe
df = df.append(a, ignore_index=True)

df.to_csv('statistics.csv') # exporting the pandas data workbook to a csv file

