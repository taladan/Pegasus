#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
+bucket:

    Bucket creation beginning...
    Pick a task:


    1. Enter a bucket name
    2. Enter a bucket description
    3. Bulletin board for approval
    4. Bulletin board for completion
    5. Bulletin board for denial
    6. Grab createdby from self.caller
    7. Set the default timeout
    8. Set the group that this bucket belongs to (default is Admin)
    9. Should this bucket be locked? <Y/N>
    10. Should we override the default notification method? <SUCC_PRE + "A new job has been posted to {0}".format(ju.decorate(self.db.key))>



    Groups:
        A group is a string, groups should separate the buckets so that if it's a player controlled group any that have group access can access
        that subset of buckets.  This way it should allow faction/group controlled jobs that can be monitored by staff when there's a need to but
        otherwise runs without staff intervetion.

        # this is the way, uh huh, I like it.

        if self.player_inputs in self.groups:
            self.bucket_settings[group]  = self.player_input
        else:
            msg = "{0}  is not in the current list of bucket groups, should I create this group? [y]es\[n]o: ".format(self.player_input)
            submenu(msg)



        groups = ["admin", "twilight guild", "the artificer's guild"]
        tag player with group...maybe not a tag, an attribute on a player that's named whatever the bucket hash is with access settings


    # cruft
        ## old imports:

        from datetime import datetime
        import evennia as ev
        from evennia.utils import evtable
        import jobutils as ju
        import jobs_settings as settings
        from world.jobs.bucket import Bucket


    Todo: Keep and rework


    def _bucket_table(self, buckets):
        ret = evtable.EvTable("Bucket", "Description", "# Jobs", "Pct", "C", "A", "D", "Due", "ARTS",
                              header=True,
                              border="table",
                              header_line_char=HEADER_LINE_CHAR,
                              width=110,
                              corner_top_left_char=CORNER_TOP_LEFT_CHAR,
                              corner_top_right_char=CORNER_TOP_RIGHT_CHAR,
                              corner_bottom_left_char=CORNER_BOTTOM_LEFT_CHAR,
                              corner_bottom_right_char=CORNER_BOTTOM_RIGHT_CHAR,
                              border_left_char=BORDER_LEFT_CHAR,
                              border_right_char=BORDER_RIGHT_CHAR,
                              border_top_char=BORDER_TOP_CHAR,
                              border_bottom_char=BORDER_BOTTOM_CHAR)

        # layout the column widths
        ret.reformat_column(0, width=12, align="l")  # Bucket
        ret.reformat_column(1, width=45, align="l")  # Description
        ret.reformat_column(2, width=8, align="r")   # Number of Jobs
        ret.reformat_column(3, width=5, align="r")   # Percent completed
        ret.reformat_column(4, width=4, align="r")   # Completion Board
        ret.reformat_column(5, width=4, align="r")   # Approval Board
        ret.reformat_column(6, width=4, align="r")   # Denial Board
        ret.reformat_column(7, width=10, align="l")   # Due
        ret.reformat_column(8, width=10, align="r")   # Average Resolution Times

        # fix header corners
        ret.table[0][0].reformat(corner_bottom_left_char=HEADER_BOTTOM_LEFT_CHAR)
        ret.table[8][0].reformat(corner_bottom_right_char=HEADER_BOTTOM_RIGHT_CHAR)

        # populate the table.
        if isinstance(buckets, list):
            for bucket in buckets:
                if self.caller in bucket.db.per_player_actions or self._pass_lock(self.caller):
                    info = bucket.info()
                    ret.add_row(*info)
            self.caller.msg(ret)
        else:
            info = buckets.info()
            ret.add_row(*info)
            self.caller.msg(ret)


"""

from evennia.utils.evmenu import EvMenu
from evennia.commands.default import MuxCommand
from bucket import Bucket
from jobs_settings import SUCC_PRE, ERROR_PRE, INFO_PRE


class CmdBucket(MuxCommand):
    """
    This holds all the commands for the bucket system.  Manipulating bucket creation through a menu driven system allows the user
    to be able to more efficiently create and use the buckets system.

    We may re-implement the old command structure after this is written for completion, however the menu driven system will be the
    advised way to manipulate and create buckets.
    # TODO: Rework these
    def _check(self, obj):
        # Todo: Fix bucket check not displaying properly
        buckets = []
        actions = []
        if self._pass_lock(self.caller):
            for bucket in self.buckets:
                actions = self._check_actions(bucket, obj)
                if actions:
                    buckets.append(bucket)

            if actions:
                ret = self._check_table(buckets)
            else:
                ret = SUCC_PRE + "%s can not perform any actions on any bucket." % self.character
        else:
            ret = ERROR_PRE + "You do not have administrator access to the bucket system."

        self.caller.msg(ret)

    #  Todo: Table template??
    def _check_table(self, bucket):
        ret = evtable.EvTable("Buckets %s has access to:" % self.character, "Actions available to: %s" % self.character,
                              header=True,
                              border="table",
                              header_line_char="-",
                              width=95,
                              corner_top_left_char=CORNER_TOP_LEFT_CHAR,
                              corner_top_right_char=CORNER_TOP_RIGHT_CHAR,
                              corner_bottom_left_char=CORNER_BOTTOM_LEFT_CHAR,
                              corner_bottom_right_char=CORNER_BOTTOM_RIGHT_CHAR,
                              border_left_char=BORDER_LEFT_CHAR,
                              border_right_char=BORDER_RIGHT_CHAR,
                              border_top_char=BORDER_TOP_CHAR,
                              border_bottom_char=BORDER_BOTTOM_CHAR, )
        # layout the column widths
        ret.reformat_column(0, width=40, align="l")   # Buckets target can access
        ret.reformat_column(1, width=55, align="c")   # Actions available to target
        # fix header corners
        ret.table[0][0].reformat(corner_bottom_left_char=HEADER_BOTTOM_LEFT_CHAR)
        ret.table[1][0].reformat(corner_bottom_right_char=HEADER_BOTTOM_RIGHT_CHAR)
        # populate the table.
        if isinstance(bucket, list):
            for buck in bucket:
                ret.add_row(buck.key, ', '.join(str(x) for x in buck.db.per_player_actions[self.character]))
        else:
            ret.add_row(', '.join(str(x) for x in bucket.info()))
        return ret

        ## Do I need this?
        _set_timeout


    # This is the node template for the EvMenu system
    def node_template(self):
        # Todo: delete me when you're done jackass
        error = ERROR_PRE + "Error message goes here"
        opt = "nodename"
        text = ("display goes here", "help goes here")
        options =(
            {
                "key": "option0",
                "desc": "The description that's shown to players", # Todo: fix
                "exec": "_set_timeout",
                "goto": "group"},
            {
                "key": "option1",
                "desc": "The description that's shown to players", # Todo: fix
                "exec": "_set_timeout",
                "goto": "group"
            },
            {
                "key": "_default",
                "desc": "This is the default option - also used for catching input from a player", # Todo: fix
                "exec": "_set_timeout",
                "goto": "group"
            }
        )
        return text, options

     """

    key = "bucket"
    aliases = ["+bucket", "+buckets", "buckets"]
    lock = "cmd:all()"
    help_category = "Jobs"


    def func(self):
        """This handles the actual functionality of the buckets command"""
        self.bucket_settings= {"approve":0,
                               "complete":0,
                               "deny":0,
                               "name": None,
                               "desc": None,
                               "timeout": None,
                               "group": "admin",
                               "locked": False,
                               "notify": SUCC_PRE + "A message has been added to the {0} bucket.".format(self.bucket.key), }

        nodes = {"name":self.name,
                 "desc":self.desc,
                 "group":self.group,
                 "timeout":self.timeout,
                 "boards":self.board,
                 "locked":self.locked,
                 "notify":self.notify,}

        # Reference: Evennia menu call model: https://github.com/evennia/evennia/wiki/EvMenu
        EvMenu(self.caller,
               nodes,
               startnode="name",
               cmdset_mergetype="Union",
               cmdset_priority=1,
               auto_help=True,
               auto_look=True,
               auto_quit=True,
               cmd_on_exit="look",
               nodetext_formatter = "", # Todo: Fix
               options_formatter= "", # Todo: Fix
               node_formatter="", # Todo: fix
               input_parser="", # Todo: fix
               persistent=True,
               **kwargs)


    # Todo: Finished, untested
    def _get_input(self, caller, raw_string):
        """get input from the user"""
        inp = raw_string.strip()
        if not inp:
            self.player_input = None
        else:
            self.player_input = inp

    def _assign_boards(self, caller):
        """loop throught the bboard settings and grab them from player input"""
        from world.utilities.pegasus_utilities import isbboard
        # errors
        no_input_error = ERROR_PRE + "You must enter a bulletin board"
        wrong_board_error = ERROR_PRE + "That is not a valid bulletin board"

        # which boards
        boards = "approve", "complete", "deny"
        for i, board in enumerate(boards):
            caller.msg(INFO_PRE + "Please enter a bulletin board for the {0} action for this bucket".format(boards[i]))
            _get_input()
            if self.player_input is None:
                caller.msg(no_input_error)
                self.desc(caller, raw_string)
            elif not isbboard(board):
                caller.msg(wrong_board_error)
                self.desc(caller, raw_string)
            else:
                self.bucket_settings[boards[i]] =  self.player_input

    def timeout(self, caller, raw_string):
        error = ERROR_PRE + "The timeout must be a number"
        opt = "timeout"
        text = ("Please enter a timeout period :>",
                "The timeout period should be an integer followed by string:\r\tex: 30 days 6 months 2 years"
                )
        options = (
            {
                "key": "_default",
                "desc": "This is the default option - also used for catching input from a player", # Todo: fix
                "exec": "self._get_input",
                "goto": "self.board"
            }
        )
        ret = text, options

        if self.player_input is None:
            self.board_settings[timeout] = 30
            return ret
        elif not self.player_input.isdigit():
            caller.msg(error)
            # Todo: add sleep
            timeout(caller, raw_string)
        else:
            timeout = self.player_input
            return ret

    def name(self, caller):
        """first node of the menu, takes the bucket name to be created"""
        exists_error = ERROR_PRE + "That bucket already exists"
        no_input_error = ERROR_PRE + "You must enter a name for the bucket"
        ii = Bucket().objects.all()
        bucket_list = []
        for bucket in ii:
            bucket_list.append(bucket.key.lower())

        opt = "name"
        text = ("Please enter a Bucket name :>",
                "A bucket name should be a single word, not more than 12 characters."
                )
        options = (
            {
                "key": "_default",
                "desc": "Default option",
                "exec": "self._get_input",
                "goto": "self.desc"
            }
        )
        ret = text, options

        if self.player_input is None:
            caller.msg(no_input_error)
            self.name(caller)
        elif self.player_input.lower() in bucket_list:
            caller.msg(exists_error)
            # Todo: add sleep
            self.name(caller)
        else:
            self.bucket_settings[opt] = self.player_input
            return ret

    def desc(self, caller, raw_string):
        """"Input the bucket description - Blocking"""
        too_long_error = ERROR_PRE + "A description may only be 45 characters in length"
        no_input_error = ERROR_PRE + "You must enter a description for the bucket"
        opt = "desc"
        text = ("Please enter a description for the bucket :>",
                "A description should be no more than 45 characters in length."
                )
        options = (
            {
                "key": "_default",
                "desc": "Default option",
                "exec": "self._get_input",
                "goto": "self.group"
            }
        )
        ret = text, options

        if self.player_input is None:
            caller.msg(no_input_error)
            self.desc(caller, raw_string)
        elif len(self.player_input) < 45:
            caller.msg(too_long_error)
            self.desc(caller, raw_string)
        else:
            self.bucket_settings[opt] = self.player_input
            return ret

    def board(self, caller, raw_string):
        """Input the bulletin board for approvals, completions, denials to go to"""
        # Todo: After bbsys creation must test for board existing before assigning - get board input from user
        text = ("Setting bulletin boards:>",
                """If a bulletin board system is available we need to set which boards Approved,\
                Completed, and Denied jobs go to."""
                )
        options = (
            {
                "key": "_default",
                "desc": "Default option",
                "exec": "self._assign_boards",
                "goto": "self.locked"
            }
        )
        ret = text, options
        return ret

    # Todo: Fix these - unfinished, untested

    def group(self, caller, raw_string):
        """Set the group that this bucket belongs to"""
        opt = "group"
        text = ("Setting the bucket group ('admin' is the default group) :>",
                """A board group determines who can access the bucket.  Typically you shouldn't need to set this for\
                 anything but faction/group buckets that you want players to be able to manage."""
                )
        options = (
            {
                "key": "_default",
                "desc": "Default option",
                "exec": "self._assign_boards",
                "goto": "self.timeout"
            }
        )
        ret = text, options

        if self.player_input == None:
            pass
        else:
            self.bucket_settings[opt]=self.player_input
        if not group:
            create group? y/n
        if y:
            create new group and assign (string)
        else:
            restart group session

    def locked(self, caller, raw_string):
        """lock the bucket"""
        # Locked node should traverse to Notify
        opt = "locked"
        if self.player_input.lower() in "yes":
            self.bucket_settings[opt] = True
        else:
            self.bucket_settings[opt] = False
        ret = SUCC_PRE + "{0} bucket has been {1}.".format(self.bucket.db.key, "locked" if self.player_input in "yes" else "unlocked")
        return ret

    def notify(self, caller, raw_string):
        """Default notification message for bucket"""
        # Todo: fix
        notify: Should we override the default notification method?(y/n)
        if y:
            input new notify
        else:
            use default notify
        }

        # Broken
        # Todo: fix

        def create(self, options):
            self.bucket = Bucket().create(options)

        def delete(self):
            pass

        def info(self):
            pass

        def monitor(self):

        def rename(self):
            pass

        def set(self):
            pass
