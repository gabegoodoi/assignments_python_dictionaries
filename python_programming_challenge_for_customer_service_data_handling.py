'''
Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:

Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.

Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
'''

import datetime
ticket_timecode = "".join("".join("".join("".join(str(datetime.datetime.now()).split()).split("-")).split(":")).split("."))


service_tickets = {
    "Ticket1" : {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

ticket_button = 3

print("Welcome to the customer ticket app!")

def open_new_ticket(main_ticket_dictionary, new_ticket):
    print("In order to add your ticket, we'll need a bit more information.")
    name = input("What is your name? ")
    issue = input("What is your issue? ")
    main_ticket_dictionary.update({new_ticket : {"Customer": name, "Issue": issue, "Status": "open"}})
    print(f"New Ticket # {new_ticket} added.")

def update_ticket_status(main_ticket_dictionary, ticket):
    if main_ticket_dictionary[ticket]["Status"] == "open":
        main_ticket_dictionary[ticket].update({"Status" : "closed"})
        print(f"{ticket} status updated to 'closed'.")
    else:
        main_ticket_dictionary[ticket].update({"Status" : "open"})
        print(f"{ticket} status updated to 'open'.")

def display_tickets_or_filter_by_status(main_ticket_dictionary):
    while True:
        display_or_filter = input("Choose from the following options\n\n[D]isplay all tickets\n[F]ilter by status\n").lower()
        if display_or_filter == "d":
            for ticket_name, ticket_info in main_ticket_dictionary.items():
                print(ticket_name)
                for key, value in ticket_info.items():
                    print(f"{key} : {value}")
                print()
            break
        elif display_or_filter == "f":
            choose_status = input("By which status would you like to filter?\n\n1. Open\n2. Closed\n")
            if choose_status == "1":
                for ticket_name, ticket_info in main_ticket_dictionary.items():
                    if ticket_info["Status"] == "open":
                        print(ticket_name)
                        for key, value in ticket_info.items():
                            print(f"{key} : {value}")
                        print()
                break
            elif choose_status == "2":
                for ticket_name, ticket_info in main_ticket_dictionary.items():
                    if ticket_info["Status"] == "closed":
                        print(ticket_name)
                        for key, value in ticket_info.items():
                            print(f"{key} : {value}")
                    print()
                break
            else:
                print("Option not available.")
        else:
            print("Must choose from options 'D' or 'F'. Try again.")

while True:
    new_ticket = "Ticket" + str(ticket_button)

    choice = input("What would you like to do?\n1. Open new ticket\n2. Update ticket status\n3. Display tickets or filter by status\n4. Quit\n")
    if choice not in ["1", "2", "3", "4"]:
        print("Choice must be 1-4")
    else:
        if choice == "1":
            ticket_button += 1
            open_new_ticket(service_tickets, new_ticket)
        elif choice == "2":
            requested_ticket = input("What ticket's status would you like to update? ")
            ticket_in_dict = service_tickets.get(requested_ticket, "Ticket not found")
            if ticket_in_dict != "Ticket not found":
                update_ticket_status(service_tickets, requested_ticket)
            else:
                print("Ticket not found.")
        elif choice == "3":
            display_tickets_or_filter_by_status(service_tickets)
        else:
            break