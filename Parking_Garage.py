from datetime import timedelta
from random import randint


class parking_garage():
    def __init__(self):
        self.ticket = []
        self.parking_spaces = []
        self.ticket_paid = {}
        self.base_time = 15
        self.time_parked = 0
        self.tickets = 0
    def take_ticket(self):
        if sum(self.parking_spaces) >= 3:
            print("There are no more parking spaces available sorry! ")
        else:
            response = input("Would you like a ticket?")
            if response.lower() == "yes":
                self.time_parked = randint(1,3200) 
                money_request = input("How would you like to pay, cash or card? ")
                if money_request.lower() == "cash" or "card":
                    self.ticket_paid[self.tickets] = self.time_parked               
                    print(self.tickets)
                    print(f"you have {self.base_time} minutes!")
                    self.tickets += 1
                    self.parking_spaces.append(1)
                    self.ticket.append(1)
                else:
                    self.ticket_paid["ticket2"] = "not paid"
                    print("Please select a valid option.")
            elif response.lower() == "no":
                print("Have a nice day! Please stop loitering!")
            else:
                print("Please select a valid option")
  
    def leave_garage(self):
        q2 = input("What is your ticket number? ")
        print(self.time_parked)
        print(self.base_time)
        if self.ticket:
            if int(q2) in self.ticket_paid.keys()  and self.time_parked <= 15:
                del self.ticket_paid[q2]
                self.parking_spaces.pop()
                self.ticket.pop()
                print("Have a nice day!")
            elif int(q2) in self.ticket_paid.keys() and self.time_parked > self.base_time:
                self.ticket_paid["ticket"] = "unpaid"
                extra_owed = (self.time_parked - self.base_time) * .20
                self.parking_spaces.pop()
                self.ticket.pop()
                print(f"You owe {extra_owed} dollars for time over 15 minutes!")
                payment_over = input("Please insert cash or card. ")
                if payment_over == "cash" or payment_over == "card":
                    self.ticket_paid["ticket"] = ["paid"]
                    print("Thank you have a nice day!")
                else:
                    print("If you don't pay we will call the cops")
            
            else:
                print("Please select a valid option")
        else:
            print("How did you get in here without a ticket?")
            self.take_ticket()

car = parking_garage()
def run():
    enter_garage = input("Would you like to enter the garage? ")
    if enter_garage.lower() == "yes":
        while True:
            question = input("Do you have a ticket? ")
            if question.lower() == "yes":
                car.leave_garage()
            elif question.lower() == "no":
                car.take_ticket()
            else:
                print("Please enter a valid response.")
                run()
    elif enter_garage.lower() == "no":
        print("Have a nice day!")
    else:
        print("Please enter a valid response")
        run()
run()


            