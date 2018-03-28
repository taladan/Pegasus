
# -*- coding: utf_8 -*-
"""
jobs_defaults.py

This file holds the defaults for the jobs systems.
You should not be changing anything in here.
instead you should look in:

    <GAME>/world/jobs/jobs_settings.py

"""
# Table Settings
DEFAULT_CORNER_TOP_LEFT_CHAR = "|y╔|n"
DEFAULT_CORNER_TOP_RIGHT_CHAR = "|y╗|n"
DEFAULT_CORNER_BOTTOM_LEFT_CHAR = "|y╚|n"
DEFAULT_CORNER_BOTTOM_RIGHT_CHAR = "|y╝|n"
DEFAULT_BORDER_LEFT_CHAR = "|b║|n"
DEFAULT_BORDER_RIGHT_CHAR = "|b║|n"
DEFAULT_BORDER_TOP_CHAR = "|b═|n"
DEFAULT_BORDER_BOTTOM_CHAR = "|b═|n"
DEFAULT_HEADER_BOTTOM_LEFT_CHAR = "|b╠|n"
DEFAULT_HEADER_BOTTOM_RIGHT_CHAR = "|b╣|n"
DEFAULT_HEADER_LINE_CHAR = "|y╼|n"
DEFAULT_SORT_METHOD = "date"
DEFAULT_SORT_DIRECTION = "des" # asc for ascending, des for descending
DEFAULT_TABLE_WIDTH = 102
DEFAULT_TEXT_COLOR = "|w"

# Prefixes
DEFAULT_ERROR_PRE = "|w|[200Game:|n "
DEFAULT_SUCC_PRE = "|w|[001Game:|n "
DEFAULT_TEST_PRE = "|000|[021TESTING>>>|n"

# Actions
DEFAULT_VALID_BUCKET_ACTIONS = ("bucket_access", "bucket_check", "bucket_create", "bucket_delete",
                                 "bucket_info", "bucket_monitor", "bucket_rename", "bucket_sort",
                                 "job_approve", "job_reply" "job_complete", "job_create", "job_edit",
                                 "job_log","job_mail", "job_reports",)
DEFAULT_VALID_JOB_ACTIONS = ("act", "add", "all", "approve", "assign", "catchup", "checkin", "checkout",
                              "claim", "clean", "clone", "complete", "compress", "create", "credits", "delete",
                              "deny", "due", "edit", "esc", "help", "last", "list", "lock", "log", "mail", "merge",
                              "mine", "name", "new", "overdue", "publish", "query", "reports", "search", "select",
                              "set", "sort", "source", "summary", "sumset", "tag", "trans", "unlock", "untag", "who",)

# Sortby
DEFAULT_VALID_SORT_METHODS = ("alpha", "date", "priorty",)

# Settings
DEFAULT_VALID_BUCKET_SETTINGS =  {"desc": "desc",
                                   "completion" : "completion_board",
                                   "approval" : "approval_board",
                                   "denial": "denial_board",
                                   "timeout" : "due_timeout", }
DEFAULT_VALID_TIMEOUT_INTERVALS = ("hours", "days", "months", "years",)
DEFAULT_VALID_JOB_SETTINGS = ()

