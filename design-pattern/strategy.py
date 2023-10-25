import random
from dataclasses import dataclass, field
import string
from typing import List, Callable


def generate_id(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class SupportTicket:
    id: str = field(init=False, default_factory=generate_id)
    customer: str
    issue: str

SupportTickets = List[SupportTicket]

Ordering = Callable[[SupportTickets], SupportTickets]


class CustomerSupport:
    def __init__(self):
        self.tickets: SupportTickets = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processng ticket id:{ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")

    def process_tickets(self, ordering: Ordering):
        ticket_list = ordering(self.tickets)

        if len(ticket_list) == 0:
            print("There are no tickets to process!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)


# Strategies for ticket processing
def fifo_ordering(tickets: SupportTickets) -> SupportTickets:
    return tickets.copy()


def filo_ordering(tickets: SupportTickets) -> SupportTickets:
    tickets_copy = tickets.copy()
    tickets_copy.reverse()
    return tickets_copy


def random_ordering(tickets: SupportTickets) -> SupportTickets:
    tickets_copy = tickets.copy()
    random.shuffle(tickets_copy)
    return tickets_copy


def blackhole_ordering(_: SupportTickets) -> SupportTickets:
    return []


def main():
    # Initialise Customer Support application
    app = CustomerSupport()

    app.create_ticket("Madhav", "Hey my camera is not working")
    app.create_ticket("Pranav", "Hey my iphone is not working")
    app.create_ticket("Rahul", "Hey my android is not working")
    app.create_ticket("Unni", "Hey my bike is not working")
    app.create_ticket("Rony", "Hey my airpods are not working")

    # Here you can use any of the following strategies defined or create a new strategy
    """
    1. fifo_ordering
    2. filo_ordering
    3. random_ordering
    4. blackhole_ordering
    """
    app.process_tickets(random_ordering)


if __name__ == "__main__":
    main()
