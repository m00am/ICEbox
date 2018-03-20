# -*- coding: utf-8 -*-
"""This module contains all clases modeling hardware like comliks, clusters, nexi, etc.


System <= Response
If System > Response -> System = Response
Programs <= System
#(Loaded programs) >= System -> Response loss


Processor Limit:
- Nodes: System
- Nexi: System * 3


"""

class Node(object):
    """This class models a node, for example a comlink."""

    def __init__(self, name, response, signal, system, firewall):
        self.name = name
        self.response = response
        self.effective_response = response
        self.signal = signal
        self.system = None
        self.firewall = None
        self.loaded_programs = []
        self.neighbours = []

        self.set_system(system)
        self.set_firewall(firewall)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.effective_response != self.response:
            reduced_response = "({})".format(self.effective_response)
        else:
            reduced_response = ""
        return f"Name: (Response: {self.response}{reduced_response}, Signal: {self.signal}, System: {self.system}, Firewall: {self.firewall})"

    def set_system(self, system):
        """Set a system value and check if it is complient with the response value.
        """
        if system <= self.response and system > 0:
            self.system = system
        elif system > 0:
            # assume max value
            self.system = self.response
        else:
            raise ValueError(f"System value has to be a positive integer. Got {system}")

    def set_firewall(self, firewall):
        """Set a firewall value and check if it is complient with the response value.
        """
        if firewall <= self.response and firewall > 0:
            self.firewall = firewall
        elif firewall > 0:
            # assume max value
            self.firewall = self.response
        else:
            raise ValueError(f"Firewall value has to be a positive integer. Got {firewall}")

    def recalculate_response_loss(self):
        """Manage response loss due to high program load.
        """
        # TODO: Does a reduced response also affect the system rating?
        response_modifier = len(self.loaded_programs) // self.response
        self.effective_response = self.response - response_modifier

    def add_program(self, program):
        """Add a new program and recalculate response value
        """
        self.loaded_programs.append(program)
        self.recalculate_response_loss()

    def remove_program(self, program):
        """Remove the program from the node and recalculate response loss.
        """
        try:
            self.loaded_programs.remove(program)
            self.recalculate_response_loss()
        except ValueError:
            print(f"Error: Tried to remove program {program} which is not in the list of the current node.")
            raise

    def add_neighbour(self, node):
        """Add a new neigbbouring node."""
        self.neighbours.append(node)

    def remove_neighbour(self, node):
        """Remove a neighbouring node."""
        try:
            self.neighbours.remove(node)
        except ValueError:
            print(f"Error: Tried to remove neighbour {node} which is not in the list of the current node.")
            raise

if __name__ == "__main__":
    n = Node("Comlink", 2, 3, 4, 5)
    print(n)
    n.add_program("foo")
    n.remove_program("foo")
    # n.remove_program("foo")
