# -*- coding: utf-8 -*-
"""This file contains all classes and functions concerning all actors acting in nodes.

This includes:
  - Agents
  - ICE
  - Users
  - Sprites
"""

class Actor(object):
    """Abstract base class for Agents, ICE, etc."""
    def __init__(self, rating):
        """Create a new agent with given rating and no programs."""
        self.rating = rating
        self.programs = []
        self.restricting_node = None
        self.current_node = None

    def move(self, node):
        """Move the agent to another node."""
        old_node = self.current_node
        self.current_node = node
        # TODO: Check which node restricts the agent. Owners comlink? Running node?

    def __repr__(self):
        return f"({self.rating}) running on {self.current_node}"


class Agent(Actor):
    """This class models agents as described in SRBB p.TODO"""

    def __init__(self, name, rating):
        """
        """
        self.name = name
        super(Agent, self).__init__(rating)

    def __repr__(self):
        return f"Agent '{self.name}' {super(Agent, self).__repr__()}"


class ICE(Actor):
    """This class models agents as described in SRBB p.TODO"""
    def __init__(self, name, rating, payload):
        """
        """
        self.name = name
        self.payload = payload
        super(ICE, self).__init__(rating)

    def __repr__(self):
        return f"ICE '{self.name}' {super(ICE, self).__repr__()}"



if __name__ == "__main__":
    a = Agent("Sentinel", 4)
    print(a)
