#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    memory = dict()
    for ticket in tickets:
        memory[ticket.source] = ticket.destination
    
    source = "NONE"
    route = []
    destination = ""
    while destination != "NONE":
        destination = memory[source]
        route.append(destination)
        source = destination

    return route


# if __name__ == "__main__":
    
