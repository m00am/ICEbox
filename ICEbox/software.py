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
import sys

PROG_TYPE_MAPPING = {
    "Analyze": ["Common", "Detection"],
    "Browse": ["Common", "Detection"],
    "Command": ["Common"],
    "Edit": ["Common"],
    "Encrypt": ["Common", "Intrusion Defense", "Electronic Warfare"],
    "Reality Filter": ["Common", "User", "f"],
    "Scan": ["Common", "Detection", "Electronic Warfare"],

    "Armor": ["Cybercombat Defensive"],
    "Attack": ["Cybercombat Offensive"],
    "Biofeedback Filter": ["Cybercombat Defensive", "User"],
    "Black Hammer": ["Cybercombat Offensive"],
    "Blackout": ["Cybercombat Offensive"],
    "Corrupt": ["Electronic Warfare"],
    "Data Bomb": ["Intrusion Defense"],
    "Decrypt": ["Intrusion Offensive", "Electronic Warfare"],
    "Defuse": ["Intrusion Offensive"],
    "Disarm": ["Intrusion Offensive"],
    "ECCM": ["Electronic Warfare"],
    "Exploit": ["Intrusion Offensive"],
    "Medic": ["Cybercombat Defensive"],  # also user?
    "Nuke": ["Cybercombat Offensive"],
    "Purge": ["Intrusion Offensive", "Intrusion Defense"],
    "Sniffer": ["Electronic Warfare"],
    "Spoof": ["Intrusion Offensive", "Electronic Warfare"],
    "Stealth": ["Intrusion Offensive"],
    "Track": ["Detection", "Electronic Warfare"],
    }

TYPE_NAME_MAPPING = {
    "Common": [
        "Analyze",
        "Browse",
        "Command",
        "Edit",
        "Encrypt",
        "Reality Filter",
        "Scan",
    ],
    "Cybercombat Offensive": [
        "Attack",
        "Black Hammer",
        "Blackout",
        "Nuke"
    ],
    "Cybercombat Defensive": [
        "Armor",
        "Biofeedback Filter",
        "Medic",
    ],
    "Detection": [
        "Analyze",
        "Browse",
        "Scan",
        "Track",
    ],
    "Electronic Warfare": [
        "Encrypt",
        "Scan",
        "Corrupt",
        "Decrypt",
        "ECCM",
        "Sniffer",
        "Spoof",
        "Track",
    ],
    "Intrusion Offensive": [
        "Decrypt",
        "Defuse",
        "Disarm",
        "Exploit",
        "Spoof",
        "Stealth",
        "Purge",
    ],
    "Intrusion Defense": [
        "Encrypt",
        "Data Bomb",
        "Purge"
    ],
    "User": [
        "Biofeedback Filter",
        "Reality Filter"
    ],
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



def validate_program_dicts():
    """ Check that the dictionaries are bijective.

    This means, that all types 
    """
    valid = True
    try:
        for name, types in PROG_TYPE_MAPPING.items():
            for t in types:
                if name not in TYPE_NAME_MAPPING[t]:
                    print(f"Found invalid mapping: {name}({types}), program name was not found in {t}")
                    valid = False
    except KeyError:
        print("Could not find program name in TYPE_NAME_MAPPING. Terminating.")
        raise

    try:
        for prog_type, names in TYPE_NAME_MAPPING.items():
            for name in names:
                if prog_type not in PROG_TYPE_MAPPING[name]:
                    print(f"Found invalid mapping: {prog_type}({names}), type was not found in {name}")
                    valid = False
    except KeyError:
        print("Could not find program type in PROG_TYPE_MAPPING. Terminating.")
        raise
        
    if not valid:
        print("Errors in the type mapping dicts were found. Terminating.")
        sys.exit(1)


if __name__ == "__main__":
    p = Program("Edit", 6)
    print(p)
    validate_program_dicts()
