
# -*- coding: utf-8 -*-
"""
################################################################################
#  JOBS - Skin output:
#           To change the skin of the tables output to the user, uncomment and
#           change the defaults below. Only a single character may be used for
#           these.
#
#           Please note: Unicode characters /may/ not work correctly on all
#                        mu* clients.  Use at your own risk.
################################################################################
_CORNER_TOP_LEFT_CHAR = ""
_CORNER_TOP_RIGHT_CHAR = ""
_CORNER_BOTTOM_LEFT_CHAR = ""
_CORNER_BOTTOM_RIGHT_CHAR = ""
_BORDER_LEFT_CHAR = ""
_BORDER_RIGHT_CHAR = ""
_BORDER_TOP_CHAR = ""
_BORDER_BOTTOM_CHAR = ""
_HEADER_BOTTOM_LEFT_CHAR = ""
_HEADER_BOTTOM_RIGHT_CHAR = ""
_HEADER_LINE_CHAR = ""

################################################################################
#  JOBS - Message prefixes
#           Use the variables below to change how your messages are prefixed
#           when they are sent to the player. Must contain string.
#
#           Please note: Unicode characters /may/ not work correctly on all
#                        mu* clients.  Use at your own risk.
################################################################################
_ERROR_PRE = ""
_SUCC_PRE = ""
_TEST_PRE = ""

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
_VALID_BUCKET_ACTIONS = ()      # Must be a set
_VALID_BUCKET_SETTINGS = {}     # Must be a dict
_VALID_JOB_ACTIONS = ()         # Must be a set
_VALID_TIMEOUT_INTERVALS = ()   # Must be a set
"""
import jobs_defaults as defaults

_CORNER_TOP_LEFT_CHAR = defaults._DEFAULT_CORNER_TOP_LEFT_CHAR
_CORNER_TOP_RIGHT_CHAR = defaults._DEFAULT_CORNER_TOP_RIGHT_CHAR
_CORNER_BOTTOM_LEFT_CHAR = defaults._DEFAULT_CORNER_BOTTOM_LEFT_CHAR
_CORNER_BOTTOM_RIGHT_CHAR = defaults._DEFAULT_CORNER_BOTTOM_RIGHT_CHAR
_BORDER_LEFT_CHAR = defaults._DEFAULT_BORDER_LEFT_CHAR
_BORDER_RIGHT_CHAR = defaults._DEFAULT_BORDER_RIGHT_CHAR
_BORDER_TOP_CHAR = defaults._DEFAULT_BORDER_TOP_CHAR
_BORDER_BOTTOM_CHAR = defaults._DEFAULT_BORDER_BOTTOM_CHAR
_HEADER_BOTTOM_LEFT_CHAR = defaults._DEFAULT_HEADER_BOTTOM_LEFT_CHAR
_HEADER_BOTTOM_RIGHT_CHAR = defaults._DEFAULT_HEADER_BOTTOM_RIGHT_CHAR
_HEADER_LINE_CHAR = defaults._DEFAULT_HEADER_LINE_CHAR
_ERROR_PRE = defaults._DEFAULT_ERROR_PRE
_SORT_METHOD = defaults._DEFAULT_SORT_METHOD
_SORT_DIRECTION = defaults._DEFAULT_SORT_DIRECTION
_SUCC_PRE = defaults._DEFAULT_SUCC_PRE
_TEST_PRE = defaults._DEFAULT_TEST_PRE
_TEXT_COLOR = defaults._DEFAULT_TEXT_COLOR
_VALID_BUCKET_ACTIONS = defaults._DEFAULT_VALID_BUCKET_ACTIONS
_VALID_BUCKET_SETTINGS = defaults._DEFAULT_VALID_BUCKET_SETTINGS
_VALID_JOB_ACTIONS = defaults._DEFAULT_VALID_JOB_ACTIONS
_VALID_JOB_SETTINGS = defaults._DEFAULT_VALID_JOB_SETTINGS
_VALID_SORT_METHODS = defaults._DEFAULT_VALID_SORT_METHODS
_VALID_TIMEOUT_INTERVALS = defaults._DEFAULT_VALID_TIMEOUT_INTERVALS
