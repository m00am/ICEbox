# -*- coding: utf-8 -*-
"""This module contains all software-related classes, including programs and program options.

Common Programs:
  Analyze
  Browse
  Command
  Edit
  Encrypt
  Reality Filter
  Scan

Hacking Programs:
  Armor
  Attack
  Biofeedback Filter
  Black Hammer
  Blackout
  Corrupt
  Data Bomb
  Decrypt
  Defuse
  Disarm
  ECCM
  Exploit
  Medic
  Nuke
  Purge
  Sniffer
  Spoof
  Stealth
  Track

Agent Autosofts:
  Adaptability (1-3)
  ... TODO Unwired: p112

Drone Autosofts:
  ... TODO Unwired: p113

Other:
  Sensorsofts
  Simsense
  Skillsofts

Common Program Options:
  Biofeedback(Rating; Stun)
  Biofeedback(Rating; Physical)
  Copy Protection(Rating)
  Crashguard
  Ergonomic
  Limitation
  Mute
  Optimization(Rating)
  Psychotropic(Rating)
  Registration
  Timer
  Viral Resistence

Hacking Program Options:
  Area(Rating)
  Armor Piercing(Rating 1-3)
  Pavlov
  Rust
  Shredder
  Targeting

Simsense Options:
  Adaptive Scale
  Addictive(Rating 1-2)
  DIMAP
  Lifeline
  Overdrive(Rating 1-3)
  Personalized
  Pluscode

Glitches:
  TODO
"""
import copy
import random

PROG_TYPE_MAPPING = {
    "Edit": ["Common"],
    }

TYPE_NAME_MAPPING = {
    "Common": ["Edit"],
    }


class Program(object):
    """A software that can be used by an agent, ice or user."""

    def __init__(self, name, rating, effective_rating=None, prog_types=None, options=None, glitches=None):
        """"""
        self.name = name
        self.rating = rating
        self.effective_rating = effective_rating
        if prog_types is not None:
            self.prog_types = []
        else:
            self.prog_types = prog_types
        if options is not None:
            self.options = []
        else:
            self.options = options
        if glitches is not None:
            self.glitches = []
        else:
            self.glitches = glitches

    @classmethod
    def copy(cls, prog):
        return cls.__init__(name=prog.name, rating=prog.rating, effective_rating=prog.effective_rating,
                            prog_types=copy.deepcopy(prog.prog_types), options=copy.deepcopy(prog.options),
                            glitches=copy.deepcopy(prog.glitches))

    @classmethod
    def random(cls, prog_type=None, max_rating=None):
        # select random program name
        name = self.get_random_name(prog_type)
        rating = random.randint(1, max_rating+1)
        prog_types = PROG_TYPE_MAPPING[name]
        return cls.__init__(name=name, rating=rating, effective_rating=rating, prog_types=prog_types)

    def __repr__(self):
        effective_rating = f"[{self.effective_rating}]" if self.effective_rating else ""
        return f"{self.name}({self.rating}{effective_rating})"

    @staticmethod
    def get_random_name(prog_type):
        if prog_type is None:
            ...
            # select from all
        else:
            ...
            # filter names
            # select from kept


class ProgOption(object):
    """An option for a program.
    """

    def __init__(self, args):
        "docstring"
        ...



if __name__ == "__main__":
    p = Program("Edit", 6)
    print(p)
