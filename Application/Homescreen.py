from random import randint

tickets = {}
payment_received = False
def generate_tickets():
    for x in range(100):
        tickets[x] = 0
    random_ticket = randint(0,99)
    print(random_ticket)
    tickets[random_ticket] = 1
    print(tickets)

def send_ticket():
    newitem = tickets.popitem()
    #print(newitem)
    #print(tickets)
    receive_ticket(newitem)

def receive_ticket(item):
    if(item[1] == 1):
        print("Time to get paid")
        payment_received = True
        print(payment_received)
    # else:
    #     print("No luck")


generate_tickets()
for j in range(100):
    send_ticket()





