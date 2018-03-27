
# -*- coding: utf-8 -*-
"""
This module holds settings that can be customized by the game admin.
"""
import jobs_defaults as defaults

################################################################################
#  JOBS - Skin output:
#           To change the skin of the tables output to the user, uncomment and
#           change the defaults below. Only a single character may be used for
#           these.
#
#           Please note: Unicode characters /may/ not work correctly on all
#                        mu* clients.  Use at your own risk.
################################################################################
CORNER_TOP_LEFT_CHAR = defaults.DEFAULT_CORNER_TOP_LEFT_CHAR
CORNER_TOP_RIGHT_CHAR = defaults.DEFAULT_CORNER_TOP_RIGHT_CHAR
CORNER_BOTTOM_LEFT_CHAR = defaults.DEFAULT_CORNER_BOTTOM_LEFT_CHAR
CORNER_BOTTOM_RIGHT_CHAR = defaults.DEFAULT_CORNER_BOTTOM_RIGHT_CHAR
BORDER_LEFT_CHAR = defaults.DEFAULT_BORDER_LEFT_CHAR
BORDER_RIGHT_CHAR = defaults.DEFAULT_BORDER_RIGHT_CHAR
BORDER_TOP_CHAR = defaults.DEFAULT_BORDER_TOP_CHAR
BORDER_BOTTOM_CHAR = defaults.DEFAULT_BORDER_BOTTOM_CHAR
HEADER_BOTTOM_LEFT_CHAR = defaults.DEFAULT_HEADER_BOTTOM_LEFT_CHAR
HEADER_BOTTOM_RIGHT_CHAR = defaults.DEFAULT_HEADER_BOTTOM_RIGHT_CHAR
HEADER_LINE_CHAR = defaults.DEFAULT_HEADER_LINE_CHAR
TABLE_WIDTH = defaults.DEFAULT_TABLE_WIDTH

################################################################################
#  JOBS - UI Message prefixes
#           Use the variables below to change how your messages are prefixed
#           when they are sent to the player. Must contain string.
#
#           Please note: Unicode characters /may/ not work correctly on all
#                        mu* clients.  Use at your own risk.
################################################################################
ERROR_PRE = defaults.DEFAULT_ERROR_PRE
SUCC_PRE = defaults.DEFAULT_SUCC_PRE
TEST_PRE = defaults.DEFAULT_TEST_PRE
TEXT_COLOR = defaults.DEFAULT_TEXT_COLOR


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
# sort settings
SORT_METHOD = defaults.DEFAULT_SORT_METHOD
SORT_DIRECTION = defaults.DEFAULT_SORT_DIRECTION
VALID_SORT_METHODS = defaults.DEFAULT_VALID_SORT_METHODS

# Bucket settings
VALID_BUCKET_ACTIONS = defaults.DEFAULT_VALID_BUCKET_ACTIONS
VALID_BUCKET_SETTINGS = defaults.DEFAULT_VALID_BUCKET_SETTINGS

# Job settings
VALID_JOB_ACTIONS = defaults.DEFAULT_VALID_JOB_ACTIONS
VALID_JOB_SETTINGS = defaults.DEFAULT_VALID_JOB_SETTINGS
VALID_TIMEOUT_INTERVALS = defaults.DEFAULT_VALID_TIMEOUT_INTERVALS
