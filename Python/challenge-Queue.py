
#change programe to copmuter input customer not user and dustrubution randomly in each ofice with customer less time 

# change the code to  computer process to get the customer random from the system 
import random
import time
class Queue:
    def __init__(self):
        self.customers = []

    def push(self, item):
        self.customers.append(item)

    def pop(self):
        if not self.is_empty():
            self.customers.pop(0)

    def is_empty(self):
        return len(self.customers) == 0

    def is_full(self):
        return False

class Office:
    def __init__(self, num_office):
        self.num_office = num_office
        self.q = Queue()

    def serve_customer(self, customer):
        self.q.push(customer)

    def process_customers(self):
        while not self.q.is_empty():
            customer = self.q.customers[0]
            print("Serving customer:", customer)
            self.q.pop()


num_office = 3
o = Office(num_office)

while True:
    cus = input("Customer: ")
    if cus == '':
        break
    d = {cus: round(random.random() * 10, 2)}
    o.serve_customer(d)
    time.sleep(2)
    
processing to the cutomer with the computer threds process in labriry to get new process if office is empty or full
o.process_customers()
