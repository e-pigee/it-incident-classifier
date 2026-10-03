from ticket import create_ticket

ticket_description = input("Describe your IT issue: ")
ticket_category = input("Enter the ticket category: ")
ticket_priority = input("Enter the ticket priority: ")

ticket = create_ticket(
    ticket_description,
    ticket_category,
    ticket_priority
)

ticket_two_description = input("Describe your second IT issue: ")
ticket_two_category = input("Enter the second ticket category: ")
ticket_two_priority = input("Enter the second ticket priority: ")

ticket_two = create_ticket(
    ticket_two_description,
    ticket_two_category,
    ticket_two_priority
)

ticket_list = [ticket]
ticket_list.append(ticket_two)

for ticket in ticket_list:
    print("Description:", ticket["description"])
    print("Category:", ticket["category"])
    print("Priority:", ticket["priority"])
    print("--------------------")
    
print(ticket_list)