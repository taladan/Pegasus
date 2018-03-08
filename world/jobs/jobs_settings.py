
# -*- coding: utf-8 -*-
"""
################################################################################
#  JOBS - Skin output:
#           To change the skin of the tables output to the user, uncomment and
#           change the defaults below.
#
#           Please note: Unicode characters /may/ not work correctly on all
#                        mu* clients.  Use at your own risk.
################################################################################
# _CORNER_TOP_LEFT_CHAR = "╔"
# _CORNER_TOP_RIGHT_CHAR = "╗"
# _CORNER_BOTTOM_LEFT_CHAR = "╚"
# _CORNER_BOTTOM_RIGHT_CHAR = "╝"
# _BORDER_LEFT_CHAR = "║"
# _BORDER_RIGHT_CHAR = "║"
# _BORDER_TOP_CHAR = "═"
# _BORDER_BOTTOM_CHAR = "═"
# _HEADER_BOTTOM_LEFT_CHAR = "╠"
# _HEADER_BOTTOM_RIGHT_CHAR = "╣"
# _HEADER_LINE_CHAR = "╼"

################################################################################
#  JOBS - Message prefixes
#           Use the variables below to change how your messages are prefixed
#           when they are sent to the player.
#
#           Please note: Unicode characters /may/ not work correctly on all
#                        mu* clients.  Use at your own risk.
################################################################################
# _ERROR_PRE = "|w|[200Game:|n "
# _SUCC_PRE = "|w|[001Game:|n "
# _TEST_PRE = "|000|[021TESTING>>>|n"

################################################################################
#  JOBS - Bucket actions & Job actions
#           DO NOT MAKE CHANGES HERE.
#
#           With that said.  If you ignore the above, note that you /must/ know
#           what you are doing here.  If you want to add actions to a bucket
#           or job, this is the place to set what is counted as a 'default'
#           valid action.  You must add your own code in if you wish to add
#           any actions as to what those actions actually /do/
#
#           If you add or change the actions, you may choose to concat your
#           actions alongside the default actions - this will keep system functionality
#           from breaking
################################################################################
# _DEFAULT_VALID_BUCKET_ACTIONS = ("access", "check", "create",
#                                  "delete", "info", "rename", "sort")
# _DEFAULT_VALID_JOB_ACTIONS = ("add", "approve", "complete",
#                               "create", "deny", "edit", "give",
#                               "log", "mail", "sort", "stats")
# _VALID_BUCKET_ACTIONS = _DEFAULT_VALID_BUCKET_ACTIONS
# _VALID_JOB_ACTIONS = _DEFAULT_VALID_JOB_ACTIONS
"""

import jobs_defaults

_CORNER_TOP_LEFT_CHAR = jobs_defaults._CORNER_TOP_LEFT_CHAR
_CORNER_TOP_RIGHT_CHAR = jobs_defaults._CORNER_TOP_RIGHT_CHAR
_CORNER_BOTTOM_LEFT_CHAR = jobs_defaults._CORNER_BOTTOM_LEFT_CHAR
_CORNER_BOTTOM_RIGHT_CHAR = jobs_defaults._CORNER_BOTTOM_RIGHT_CHAR
_BORDER_LEFT_CHAR = jobs_defaults._BORDER_LEFT_CHAR
_BORDER_RIGHT_CHAR = jobs_defaults._BORDER_RIGHT_CHAR
_BORDER_TOP_CHAR = jobs_defaults._BORDER_TOP_CHAR
_BORDER_BOTTOM_CHAR = jobs_defaults._BORDER_BOTTOM_CHAR
_HEADER_BOTTOM_LEFT_CHAR = jobs_defaults._HEADER_BOTTOM_LEFT_CHAR
_HEADER_BOTTOM_RIGHT_CHAR = jobs_defaults._HEADER_BOTTOM_RIGHT_CHAR
_HEADER_LINE_CHAR = jobs_defaults._HEADER_LINE_CHAR
_ERROR_PRE = jobs_defaults._ERROR_PRE
_SUCC_PRE = jobs_defaults._SUCC_PRE
_TEST_PRE = jobs_defaults._TEST_PRE
_VALID_BUCKET_ACTIONS = jobs_defaults._VALID_BUCKET_ACTIONS
_VALID_JOB_ACTIONS = jobs_defaults._VALID_JOB_ACTIONS
_VALID_BUCKET_SETTINGS = jobs_defaults._VALID_BUCKET_SETTINGS
_VALID_JOB_SETTINGS = jobs_defaults._VALID_JOB_SETTINGS
