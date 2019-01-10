#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
merge_dict is part of the project docbotbot
Author: Valérie Hanoka

"""

import six
from copy import deepcopy

try:
    basestring
except NameError:
    basestring = str


# ----  Exceptions ---- #
class QueryException(Exception):
    pass


class NameSpaceException(QueryException):
    pass

# ---- Data structure identification --- #

def is_listlike(element):
    """Identify objects that acts like lists (list, tuple, set, ...)
    but are *not* strings.
    """

    if isinstance(element, basestring):
        return False
    else:
        try:
            element.__iter__()
            return True
        except AttributeError:
            return False

# ---- Data structures ---- #

def merge_two_dicts_in_lists(x, y):
    """Given two dicts (with string keys),
    merge them into a new dict as a deep copy.
    In cases of duplicate keys, values are appended in lists.

    >>> dic_y = {'both': {'both_y_diff' : 'bar', 'both_same': 'same_y'}, 'only_y': 'only_y'}
    >>> dic_x = {'both': {'both_x_diff' : 'foo', 'both_same': 'same_x'}, 'only_x': {'only_x' : 'baz'}}
    >>> merge_two_dicts(dic_x, dic_y)
    >>> {'both': {
    >>>      'both_same': ['same_x', 'same_y'],
    >>>      'both_x_diff': 'foo',
    >>>      'both_y_diff': 'bar'},
    >>>  'only_x': {'only_x': 'baz'},
    >>>  'only_y': 'only_y'}

    :param x: First dictionary
    :param y: Second dictionary
    :return: The recursive merge of x and y, appending values in list in case of duplicate keys."""
    if not isinstance(y, dict):
        return y
    result = deepcopy(x)
    for k, v in six.iteritems(y):
        if k in result and isinstance(result[k], dict):
                result[k] = merge_two_dicts_in_lists(result[k], v)
        else:
            if isinstance(v, dict):
                result[k] = deepcopy(v)
            else:
                v = deepcopy(v)
                existing_v = deepcopy(result.get(k, []))
                if existing_v:
                    v = v if isinstance(v, list) else [v]
                    existing_v = existing_v if isinstance(existing_v, list) else [existing_v]
                    result[k] = existing_v+v
                else:
                    result[k] = v
    return result


def merge_two_dicts_in_sets(x, y):
    """Given two dicts (with string keys),
    merge them into a new dict as a deep copy.
    In cases of duplicate keys, values are added into a set.

    >>> dic_y = {'both': {'both_y_diff' : 'bar', 'both_same': 'same_y'}, 'only_y': 'only_y'}
    >>> dic_x = {'both': {'both_x_diff' : 'foo', 'both_same': 'same_x'}, 'only_x': {'only_x' : 'baz'}}
    >>> merge_two_dicts(dic_x, dic_y)
    >>> {'both': {
    >>>      'both_same': set(['same_x', 'same_y']),
    >>>      'both_x_diff': 'foo',
    >>>      'both_y_diff': 'bar'},
    >>>  'only_x': {'only_x': 'baz'},
    >>>  'only_y': 'only_y'}

    :param x: First dictionary
    :param y: Second dictionary
    :return: The recursive merge of x and y, appending values in list in case of duplicate keys."""
    if not isinstance(y, dict):
        return y
    result = deepcopy(x)
    for k, v in y.items():
        if k in result and isinstance(result[k], dict):
                result[k] = merge_two_dicts_in_sets(result[k], v)
        else:
            if isinstance(v, dict):
                result[k] = deepcopy(v)
            else:
                v = deepcopy(v)
                existing_v = deepcopy(result.get(k, set([])))
                if existing_v:
                    v = v if isinstance(v, set) else set([v])
                    existing_v = existing_v if isinstance(existing_v, set) else set([existing_v])
                    result[k] = existing_v | v
                else:
                    result[k] = v
    return result