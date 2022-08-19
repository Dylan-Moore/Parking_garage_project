from datetime import timedelta


class parking_garage():
    def __init__(self):
        self.ticket = []
        self.parking_spaces = []
        self.ticket_paid = {}

    def take_ticket(self):
        if sum(self.parking_spaces) >= 3:
            print("There are no more parking spaces available sorry! ")
        else:
            response = input("Would you like a ticket?")
            if response.lower() == "yes":
                money_request = input("How would you like to pay, cash or card? ")
                if money_request.lower() == "cash" or "card":   
                    self.ticket_paid["ticket"] = "paid"                 
                    print(self.ticket_paid)
                    print(f"you have {timedelta(minutes =15)} minutes!")
                    self.parking_spaces.append(1)
                    self.ticket.append(1)
                else:
                    self.ticket_paid["ticket2"] = "not paid"
                    print("Please select a valid option.")
            else:
                print("Please select a valid option")
  
    def leave_garage(self):
        q2 = input("Would you like to leave? ")
        if q2 == "yes" and self.ticket_paid["ticket"] == "paid":
            self.parking_spaces.pop()
            self.ticket.pop()
            print("Have a nice day!")
        else:
            print("Okay")

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


            