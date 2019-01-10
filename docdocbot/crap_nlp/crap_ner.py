#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Heuristic Named Entity recognition in French medical Tweets
addressed to DocTocToc.
crap_ner.py is part of the project docbotbot
Author: Valérie Hanoka

"""
import re
from docdocbot.utils.merge_dict import merge_two_dicts_in_sets

NE_NUM_UNIT = re.compile('(?P<num>[0-9/,\.]+)\s*(?P<unit>[^0-9]*)')

NE_REGEX = {
    'PATIENT': [
        re.compile('(?P<gender>[HF])[de ]*(?P<age>([0-9][/0-9]*)\s*(an?s?))+', flags=re.IGNORECASE),
        re.compile('(?P<gender>(HF))(omme|emme)?', flags=re.IGNORECASE),
        re.compile('(?!((il\sy\s*a)|en|depuis|pour|pendant))\s*(?P<age>([0-9][/0-9]*)\s*(an?s?))+',
                   flags=re.IGNORECASE),
        re.compile('(?P<gender>patiente?|gar[çc]on|fille(tte)?)\s', flags=re.IGNORECASE),
        re.compile('(?P<gender>une? enfant)', flags=re.IGNORECASE),
        re.compile('(?P<gender>une? ado)', flags=re.IGNORECASE),

    ],
    'POSOLOGIE': [
        re.compile('sous (?P<molecule>[^ ]{3,})\s(?P<qantity_unit>[0-9][,\/0-9]*\s*[a-z\-/]+)', flags=re.IGNORECASE),
        re.compile('(?P<molecule>[^ ]{3,})\s(?P<qantity_unit>[0-9][,\/0-9]*\s*(m?g)+) ', flags=re.IGNORECASE)
    ],
}

########################
# NE Normalization
########################

#--- Age ---#

def get_normalized_age(string_age):
    num, unit = re.match(NE_NUM_UNIT, string_age).groups()
    num = num.rpartition('/')[0] if '/' in num else num
    num = float(num.replace(',', '.'))
    map_age_units = {
        'a': 'y',
        'm': 'm',
        'j': 'd'
    }
    unit = map_age_units.get(unit[0].lower(), 'unknown')
    return (num, unit)

def normalize_age(raw_ages):
    raw_ages_list = []
    if isinstance(raw_ages, set):
        for raw_age in raw_ages:
            norm_age = get_normalized_age(raw_age)
            raw_ages_list.append(norm_age)
    else:
        raw_ages_list.append(get_normalized_age(raw_ages))

    # Only the greatest age is returned
    return sorted(raw_ages_list).pop()

#--- Gender ---#

def get_normalized_gender(raw_gender):
    raw_gender = raw_gender.lower()
    map_genders = {
        'd': 'f', # dame
        'g': 'm', # garçon
        'm': 'm', # monsieur
        'h': 'm', # homme
        'f': 'f'  # femme
    }
    gender_initial = map_genders.get(raw_gender[0])
    if gender_initial:
        return gender_initial

    # Patient•e
    if raw_gender.startswith('pat'):
        return 'f' if raw_gender[-1]=='e' else 'm'
    if raw_gender.startswith('une'):
        return 'f'
    if raw_gender.startswith('un'):
        return 'm'

    return 'unknown'

def normalize_gender(raw_genders):

    if isinstance(raw_genders, set):
        raw_genders = raw_genders.pop()
    return get_normalized_gender(raw_genders)

#--- Posology ---#
# TODO: improve
def normalize_molecule(raw_molecules):
    raw_molecule_list = []
    if isinstance(raw_molecules, set):
        for raw_molecule in raw_molecules:
            raw_molecule_list.append(raw_molecule.lower())
    else:
        raw_molecule_list.append(raw_molecules.lower())

    return raw_molecule_list

def get_normalized_quantity_unit(string_quantity_unit):
    num, unit = re.match(NE_NUM_UNIT, string_quantity_unit).groups()
    num = float(num.replace(',', '.'))

    return (num, unit.lower())

def normalize_qantity_unit(raw_quantity_units):
    raw_quantity_unit_list = []
    if isinstance(raw_quantity_units, set):
        for raw_quantity_unit in raw_quantity_units:
            raw_quantity_unit_list.append(
                get_normalized_quantity_unit(raw_quantity_unit)
            )
    else:
        raw_quantity_unit_list.append(
            get_normalized_quantity_unit(raw_quantity_units)
        )

    return raw_quantity_unit_list

####################
# NER Extraction
####################

def normalize_ners(raw_ner_dict):
    ne_normalizing = {
        'gender': normalize_gender,
        'age': normalize_age,
        'molecule': normalize_molecule,
        'qantity_unit': normalize_qantity_unit
    }

    normalized_ners = {}
    for (key, value) in raw_ner_dict.items():
        normalized_ners[key] = ne_normalizing.get(key)(value)
    return normalized_ners



def get_ners(full_text):
    ner_info = {}
    for NE_TYPE, REGEXPS in NE_REGEX.items():
        matched_ners = {}
        for RE in REGEXPS:
            for match in re.finditer(RE, full_text):
                matched_ners = merge_two_dicts_in_sets(matched_ners, match.groupdict())
        if matched_ners:
            ner_info.update({NE_TYPE: normalize_ners(matched_ners)})
    return ner_info


