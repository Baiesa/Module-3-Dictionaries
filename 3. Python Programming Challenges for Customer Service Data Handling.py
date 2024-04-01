'''
Task 1: Customer Service Ticket Tracker
Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement:
Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:


'''

class CustomerServiceTicketTracker:
    def __init__(self, initial_tickets):
        self.service_tickets = initial_tickets

    def open_new_ticket(self, ticket_id, customer_name, issue_description):
        if ticket_id not in self.service_tickets:
            self.service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
            print(f"New ticket opened with ID: {ticket_id}")
        else:
            print("Ticket ID already exists. Please choose a unique ID.")

    def update_ticket_status(self, ticket_id, new_status):
        if ticket_id in self.service_tickets:
            self.service_tickets[ticket_id]["Status"] = new_status
            print(f"Status of ticket {ticket_id} updated to {new_status}.")
        else:
            print("Ticket ID not found.")

    def display_tickets(self, status_filter=None):
        if status_filter:
            filtered_tickets = {ticket_id: ticket_info for ticket_id, ticket_info in self.service_tickets.items() if
                                ticket_info["Status"] == status_filter}
            if filtered_tickets:
                print(f"Tickets with status '{status_filter}':")
                for ticket_id, ticket_info in filtered_tickets.items():
                    print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
            else:
                print(f"No tickets found with status '{status_filter}'.")
        else:
            print("All Tickets:")
            for ticket_id, ticket_info in self.service_tickets.items():
                print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")

initial_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

ticket_tracker = CustomerServiceTicketTracker(initial_tickets)
ticket_tracker.open_new_ticket("Ticket003", "Charlie", "Website loading slowly")
ticket_tracker.update_ticket_status("Ticket001", "closed")
ticket_tracker.display_tickets()
ticket_tracker.display_tickets("open")