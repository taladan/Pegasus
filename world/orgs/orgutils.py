#!/usr/bin/python
# -*- coding utf-8 -*-


import evennia as ev
from org import Org
# imports go here

def assign_org(group_string):
    """assign a group if it exists

    :return: group query object
    """
    return ev.search_script(group_string)
