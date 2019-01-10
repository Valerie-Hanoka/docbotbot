#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
crap_ner.py is part of the project docbotbot
Author: Valérie Hanoka

"""
import re



PATIENT = [
    re.compile('(?P<sex>J?[HF])\s*(?P<age>[0-9][/0-9]*)(an?)', flags=re.IGNORECASE),
    re.compile('(?P<sex>J?(HF))(omme|emme)*', flags=re.IGNORECASE),
    re.compile('(?!(depuis|pour|pendant))\s*(?P<age>([0-9][0-9]*))\s* an?', flags=re.IGNORECASE),
    re.compile('(?P<sex>patiente?|gar[çc]on|fille(tte)?)\s', flags=re.IGNORECASE),
    re.compile('(?P<sex>une? enfant)', flags=re.IGNORECASE),
]

POSOLOGIE = [
    re.compile('(?P<prec>(\w*[ :]*){,5})\s(?P<Qte>[0-9][,\/0-9]*)\s*(?P<unit>[a-z\-/]+)', flags=re.IGNORECASE),
    re.compile('(sous)(?<molecule>)')
]



def get_ners(token):

    info = {}

    NE = PATIENT + POSOLOGIE
    for RE in NE:

        match = re.search(RE, token)
        if match:
            info.update(match.groupdict())

    if info:
        print(token)
        print(info)
