# -*- coding: utf-8 -*-
"""This file contains all classes and functions concerning all kinds of actors acting in nodes.

This includes:
  - Agents
  - ICE
  - Sprites
  - Users
"""

class Actor(object):
    """Abstract base class for Agents, ICE, etc."""
    def __init__(self, rating):
        """Create a new agent with given rating and no programs."""
        self.rating = rating
        self.programs = []
        self.restricting_node = None
        self.current_node = None
        self.max_dmg_boxes = 8 + (rating // 2)
        self.current_dmg_boxes = self.max_dmg_boxes
        self.response = None

    def move_home_node(self, node):
        """Move the agent to another node."""
        self.current_node = node
        self.calculate_attributes()

    def calculate_attributes(self):
        """(Re-) calculate all node-depending attributes. I.e. Response"""
        if self.current_node:
            self.response = self.current_node.response
        else:
            self.response = None

    def __repr__(self):
        return f"({self.rating}) running on {self.current_node}"


class Agent(Actor):
    """This class models agents as described in SRBB(anniversary ed.) p.234

    Attribute: Agent rating
    Derived Attributes and Skills:

        - Pilot Rating = Agent Rating
        - System = Pilot
        - Firewall = Pilot
        - No Signal
        - Response = Response of Node it is running on (not the one it )
        - Computer, Hacking, Data Search, Cyber Combat all equal to its pilot rating

    An agent must be run on a node, but can be send to other nodes.
    If run independently, the Agent counts against the subscription limit (and not the processor limit).
    If run on the same node, the agent counts against the processor limit (and not the subscription limit).

    All software run by an agent is limited by its Pilot Rating.
    """

    def __init__(self, name, rating, payload, *, independent):
        """Create an agent using a name, its rating and the independent flag."""
        self.name = name
        self.payload = payload
        self.independent = independent
        super(Agent, self).__init__(rating)

    def __repr__(self):
        return f"Agent '{self.name}' {super(Agent, self).__repr__()}"


class ICE(Actor):
    """This class models agents as described in SRBB AE p.235

    Work just as Agents.
    Only differences:

        - ICE always runs independently (has its own icon)
        - The ICE as well as its programs count against the processor limit
    """
    def __init__(self, name, rating, payload):
        """Create a new ICE using a name, rating and list of programs (payload)."""
        self.name = name
        self.payload = payload
        self.independent = True
        super(ICE, self).__init__(rating)

    def __repr__(self):
        return f"ICE '{self.name}' {super(ICE, self).__repr__()}"

if __name__ == "__main__":
    a = Agent("Sentinel", 4, [], independent=True)
    print(a)
