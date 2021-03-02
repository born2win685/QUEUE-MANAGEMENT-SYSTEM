import numpy
import pandas
import self as self
import tkinter


def gen_int_arr():
    return -numpy.log(1 - (numpy.random.uniform(low=0.0, high=1.0))) * 3


def gen_service_time_teller1():
    return -numpy.log(1 - (numpy.random.uniform(low=0.0, high=1.0))) * 1.2


def gen_service_time_teller2():
    return -numpy.log(1 - (numpy.random.uniform(low=0.0, high=1.0))) * 1.5

class Simulation:
    def __init__(self):
        self.clock = 0.0  # keeps track of time
        self.no_of_arrivals = 0  # gives the total no of arrivals till now
        self.time_arrival = gen_int_arr() #time for next arrival
        self.time_leaving_count1 = float('inf')  # time when a customer leaves counter 1
        self.time_leaving_count2 = float('inf')  # time when a customer leaves counter 2
        '''float('inf') is used while assigning to a variable when we have to find the lowest value,intialising it to 0 
        may cause errors,so initially we assume the lowest value as an positive infinite value'''
        '''similarly,if we wnt to get a max value ,we initialize to to -infinite by float('-inf')'''
        self.state_count1 = 0  # current state of counter 1
        self.state_count2 = 0  # current state of counter 2
        self.total_wait_time = 0.0
        self.num_in_q = 0  # current no of customers in queue
        self.totat_cust_in_q = 0  # no of customers who stood in queue
        self.num_of_departures1 = 0  # number of customers served in counter 1
        self.num_of_departures2 = 0  # number of customers served in counter 2
        self.lost_customers = 0  # customers who left without service

    def time_routines(self):
        next_event_time=min(self.time_leaving_count1, self.time_leaving_count2, self.time_arrival) #calculating the time for the next event
        self.total_wait_time+=(self.num_in_q*(next_event_time-self.clock)) #calculating the total time
        self.clock=next_event_time #Clock is set to time of the next event taking place 

        if self.time_arrival<self.time_leaving_count1 and self.time_arrival<self.time_leaving_count2:
            self.arrival() #if arrival time is less than departure from both the counters
        elif self.time_leaving_count1<self.time_arrival and self.time_leaving_count1<self.time_leaving_count2:
            self.counter1() #if departure time of counter 1 is less than arrival and departure time of counter 2
        else:
            self.counter2() #if departure time of counter 2 is less than arrival and departure time of counter 1
