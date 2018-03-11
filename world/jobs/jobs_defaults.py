
# -*- coding: utf_8 -*-
"""
jobs_defaults.py

This file holds the defaults for the jobs systems.
You should not be changing anything in here.
instead you should look in:

    <GAME>/world/jobs/jobs_settings.py

"""
_DEFAULT_CORNER_TOP_LEFT_CHAR = "|y╔|n"
_DEFAULT_CORNER_TOP_RIGHT_CHAR = "|y╗|n"
_DEFAULT_CORNER_BOTTOM_LEFT_CHAR = "|y╚|n"
_DEFAULT_CORNER_BOTTOM_RIGHT_CHAR = "|y╝|n"
_DEFAULT_BORDER_LEFT_CHAR = "|b║|n"
_DEFAULT_BORDER_RIGHT_CHAR = "|b║|n"
_DEFAULT_BORDER_TOP_CHAR = "|b═|n"
_DEFAULT_BORDER_BOTTOM_CHAR = "|b═|n"
_DEFAULT_HEADER_BOTTOM_LEFT_CHAR = "|b╠|n"
_DEFAULT_HEADER_BOTTOM_RIGHT_CHAR = "|b╣|n"
_DEFAULT_HEADER_LINE_CHAR = "|y╼|n"

# Prefixes
_DEFAULT_ERROR_PRE = "|w|[200Game:|n "
_DEFAULT_SUCC_PRE = "|w|[001Game:|n "
_DEFAULT_TEST_PRE = "|000|[021TESTING>>>|n"

# Actions
_DEFAULT_VALID_BUCKET_ACTIONS = ("access", "check", "create", "delete", "info", "monitor", "rename", "sort")
_DEFAULT_VALID_JOB_ACTIONS = ("add", "approve", "complete", "create", "deny", "edit", "give",
                              "log", "mail", "sort", "stats")
# Settings
_DEFAULT_VALID_BUCKET_SETTINGS =  {"desc": "desc",
                                   "completion" : "completion_board",
                                   "approval" : "approval_board",
                                   "denial": "denial_board",
                                   "timeout" : "due_timeout",}
_DEFAULT_VALID_TIMEOUT_INTERVALS = ("hours", "days", "months", "years")
_DEFAULT_VALID_JOB_SETTINGS = ()
