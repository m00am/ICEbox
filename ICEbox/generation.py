# -*- coding: utf-8 -*-
"""Put everything that generates a system structure here.
"""
import nodes
import actors
import software
import random

CON_NAMES = [
    # The big 10
    "Ares",
    "Aztechnology",
    "Evo",
    "Horizon",
    "Mitsuhama",
    "Renraku",
    "Saeder-Krupp",
    "Shiawaze",
    "Spinrad",
    "Wuxing",

    "Cross",
    "Yakashima",
]



class Name:
    def __init__(self, name, connotations):
        self.name = name
        self.connotations = connotations

ICE_NAMES = [
    Name("Rottweiler", ["offensive", "defensive"]),
    Name("Knight",  ["offensive", "defensive"]),
    Name("Bloodhound", ["defensive", "tracking"]),
]




## patterns
# honeypot  (looks interesting, is veeery dangerous)
# camera node  (has lots of cameras subscribed)
# security nexus  (launches all the ICE for the system)
# drone control  (cleaning and maintenance drones)
# security done control  (combat drones)
# environment control  (climate controls, lights, etc)
# public UI  (Bank login or similar)
# private/ internal UI  (For users of the system, dev suites, )
# API  ()
# data vault  (big ass storage facility, inherent high level browse)
# paydata vault  (contains money!)
# compute server  (high response machines)
# sysadmin node  (periheral data for all computer systems)
# spider node  (control over all active users, inherent search)
# terminal  (runs some programs, thats it)
# uplink node  (allows connection to other subnet)
# satelite  (as the name suggests)
# log node  (keeps the datalog)




## variants
# distributed
# deprecated
# 




## Tree by escalating privacy value
# public, private, restricted, secret


## minimal nodes and example nodes
def get_tiny_nodes():
    tiny_nodes = dict()

    # a level 3 camera with an autonomous agent looking for stuff.
    n = nodes.Node("Camera", 3, 3, 3, 3)
    a = actor.Agent("Argus", 3, [programs.Program("Command", 3), programs.Program("Autosoft(Security)")], independent=False)
    n.add_program(a)
    tiny_nodes["Camera"] = n

    # a vending machine
    n = nodes.Node("Coffee Vending Machine", 2, 1, 2, 2)
    tiny_nodes["Coffee Vending Machine"] = n
    
    # a terminal in a public library
    n = nodes.Node("Library Terminal", 3, 2, 3, 2)
    n.add_program(programs.Program("Browse", 3))
    n.add_program(programs.Program("Edit", 3))
    tiny_nodes[n.name] = n

    # Cheap comlink
    n = nodes.Node("Cheap Comlink", 2, 3, 2, 1)
    n.add_program(programs.Program("Analyze", 2))
    tiny_nodes[n.name] = n

    # Average comlink
    n = nodes.Node("Average Comlink", 3, 3, 3, 3)
    n.add_program(programs.Program("Analyze", 2))
    a = actor.ICE("Rottweiler", 3, [programs.Program("Attack", 3)])
    tiny_nodes[n.name] = n
    
    return tiny_nodes



## ICE

def random_ICE(rating=None, role=None):
    if role is None:
        role = random.choice(("offensive", "defensive", "tracker"))
    if rating is None:
        rating = random.randint(1,6)
    name = f"{random.choice(CON_NAMES)} {random.choice(ICE_NAMES).name}"
    if role == "offensive":
        payload = ["Attack"]
    elif role == "defensive":
        payload = ["Analyze"]
    elif role == "tracker":
        payload = ["Analyze", "Trace"]
    else:
        raise ValueError(f"Invalid role {role}")
    return actors.ICE(name, rating, payload)


if __name__ == "__main__":
    print(random_ICE())
