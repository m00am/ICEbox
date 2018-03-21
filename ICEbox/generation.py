# -*- coding: utf-8 -*-
"""Put everything that generates a system structure here.
"""
import .nodes
import .actors
import .software




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
# compute server  (high response machines)
# sysadmin node  (periheral data for all computer systems)
# spider node  (control over all active users, inherent search)
# 



## variants
# distributed
# deprecated
# 




## Tree by escalating privacy value



## minimal nodes and example nodes


def get_tiny_nodes():
    tiny_nodes = dict()

    # a level 3 camera with an autonomous agent looking for stuff.
    n = nodes.Node("Camera", 3, 3, 3, 3)
    a = actor.Agent("Argus", 3, [programs.Program("Command", 3), programs.Program("Autosoft(Security)")], independent=False)
    n.add_program(a)
    tiny_nodes["Camera"] = n

    # a vending machine
    n = nodes.Node("Coffe Vending Machine", 2, 1, 2, 2)
    
    
