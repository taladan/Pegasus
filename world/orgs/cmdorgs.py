#!/usr/bin/python
# -*- coding utf-8 -*-

# import goes here
from evennia import default_cmds
from evennia.utils.evmenu import EvMenu
from orgutils import assign_org
from world.utilities.pegasus_utilities import is_org, assign_character, isblank
from org_settings import SUCC_PRE, ERROR_PRE, INFO_PRE, TEST_PRE
# from evennia.utils import logger as log


# Todo: research inheritance
class CmdOrgs(default_cmds.MuxCommand):
    """
    Org should aggregate a list of players that have access to that org's commands.  This should include special segments of systems such as:

    * BBsys
    * Mailing lists
    * Jobs system
    * Events (Org events?)
    * Org inventory/fund storage
    * Org goals?? (possibly tied in with bbsys - see ferex tenebrae's RPP system)
    * Org logging?? - May need to tie in to mailsys.
    """
    key = "org"
    aliases = ["orgs", "faction", "factions", "grp", "fact", "fac"]
    locks = "cmd:perm(Admin)" # Todo: fix lock perms so that members of a org can access the commands as well as the admin

    def func(self):
        """this handles the main functionality of the org command
        # Todo: determine addt'l commands

        |Command|Description|
        |:-----:|:---------:|
        +org/create Org=Description|Creates Org with Description
        +org/add Org=Character|Adds Character to Org
        +org/remove Org=Character|Removes Character from Org
        +org/rename Org=Neworg|Rename the org to Newname
        +org/delete Org|Deletes a specific org and all membership information
        +org/list Org|Display list of members in the org

        # cmd template
        +cmd/switch Noun/Verb=Noun/verb

        we can parse with just self.lhs & self.rhs currently """
        self.org_opts = {"name": None,"board": None,"desc": None,"bucket": None,"vault": None,}
        # Todo: Take this out and put something sane here.
        usage = "This is some usage option, if you've got this, you hit something stupid or the code stopped working.  Tell Taladan to change this message."


        # Todo: cleanup pt()
        pt = self.caller.msg
        pt(TEST_PRE + repr(self.switches))

        # one switch at a time
        if self.switches:
            self.switch = self.switches[0]

            # We bypass self._switch_parser here because create is a special case (creates a menu object)
            if self.switch.lower() == "create":
                if self.can(self.caller, "create"):
                        # Bombs away.  Todo: Clean up switches
                        self._create()

            elif self.lhs:
                # set orgname
                self.org_string = self.lhs
                self.org = assign_org(self.org_string)

                # set our target
                if self.rhs:
                    self.target_string = self.rhs

                try:
                    ret = _switch_parser(self.switch)
                except ValueError as e:
                    ret = ERROR_PRE + "Caught an unhandled exception: " + repr(e)
                    self.caller.msg(ret)
                    raise e
        else:
            #Todo: remove snark
            ret = usage + "Sweetikins"
        self.caller.msg(ret)

    def _create(self):
        """org creation menu"""
        nodes = {
            "name": "self._set_name",
            "desc": "self._set_desc",
            "board": "self._set_board",
            "bucket": "self._set_bucket",
            "inventory": "self._set_vault",
        }

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
               persistent=True,)

        # Todo: test this
        for k,v in self.org_opts:
           self.org.db.k = v

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

    # Todo: Delete
    """

    Create menu tree.


              - name
              - desc
      - start - board
              - bucket
              - vault
    """


    def _start(self, caller, raw_string):
        """Welcome to the Organization creation wizard.

            Oranizations by necessity are unique to the group it's composed of;  However, each organization will be
            given a standardized commandset.  The following things must be set on an organization before it can be created.

            *  Name: A simple descriptive name up to 80 characters in length
            *  Desc: A description of the organization up to 1000 characters in length
            *  Bucket: A simple single name up to 12 characters in length
            *  Board: A name for the bbsys of up to 45 characters in length

        """
        next = None

        text = self._set_name.__doc__
        options = (
            {
                "key": "_set_name",
                "desc": "desc for self._set_name",
                "exec": "self._set_name",
                "goto": next
            },
            {
                "key": "_set_desc",
                "desc": "desc for self._set_desc",
                "exec": "self._set_desc",
                "goto": next
            },
            {
                "key": "_set_board",
                "desc": "desc for self._set_board",
                "exec": "self._set_board",
                "goto": next
            },
            {
                "key": "_set_bucket",
                "desc": "desc for self._set_bucket",
                "exec": "self._set_bucket",
                "goto": next
            },
            {
                "key": "_set_vault",
                "desc": "desc for self._set_vault",
                "exec": "self._set_vault",
                "goto": next
            },
        )
        ret = text, options
        return ret

    def _set_name(self, caller, raw_string):
        """Set your organization's name.

        ### Requirements for the organization name:

        * Your organization's name should be unique to the game
        * It should be no more than 80 characters in length
        * adhere to the language rules of the game

        """
        noname_error = ERROR_PRE + "You must enter a name for the organization"
        exists_error = ERROR_PRE + "That organization exists"
        set_msg = SUCC_PRE + "Organization name set to {0}".format(raw_string.strip()[0:79])

        def do(caller, raw_string):
            """Set the name and gather options"""
            next = "do"
            if isblank(raw_string):
                next = "self._set_name"
                caller.msg(noname_error)
            elif isself._org(raw_string):
                next = "self._set_name"
                caller.msg(exists_error)
            else:
                self.org_opts["name"] = raw_string.strip()[0:79]
                caller.msg(set_msg)
                next = "self._start"

            text = None
            options = (
                {
                    "key": "_default",
                    "desc": None,
                    "goto": next,
                },
            )
            ret = text, options
            return ret

        text = self._set_name.__doc__
        options = (
            {
                "key": "_default",
                "desc": None,
                "goto": "next",
            },
        )

        ret = text, options
        return ret

    def _set_desc(self, caller, raw_string):
        """Set the description for the organization.

        ### The description should contain:

        * Org structure (if appropriate) - Suggested*
        * any org specific aliases/commands/pertinent zone info
        * Org bb # (added by system)
        * org bucket (added by system)

        |wNote|n: the description Truncates at 1000[999] characters.
        """
        next = "do"

        def do(caller, raw_string):
            """this actually sets the desc"""
            blank_error = ERROR_PRE + "You must set a description."
            set_msg = SUCC_PRE + "Description set to {0}".format(raw_string.strip()[999])
            next = "_start"
            if isblank(raw_string):
                caller.msg(blank_error)
                next = _set_desc
            else:
                self.org_opts["desc"] = raw_string.strip()[0:999]
                caller.msg(set_msg)

            text = None
            options = (
                {
                    "key": "_default",
                    "desc": None,
                    "goto": next
                },
            )

            ret = text, options
            return ret

        text = self._set_desc.__doc__
        options =(
            {
                "key": "_default",
                "goto": next,
                "desc": None,
            },
        )

        ret = text, options
        return ret

    def _set_board(self, caller, raw_string):
        """Set the name of the organization bboard

        ### The name should:

        * be no more than 45 characters in length.
        * be descriptive
        * adhere to the language rules of the game
        """
        next = "do"

        def do(caller, raw_string):
            """this sets the bulletin board name"""
            blank_error = ERROR_PRE + "The bulletin board name may not be blank"
            set_msg = SUCC_PRE + "The bulletin board name has been set to {0}".format(raw_string.strip()[0:999])
            try:
                len(raw_string)
                self.org_opts["desc"] = raw_string.strip()[0:999]
                caller.msg(set_msg)
                next = "_start"
            except TypeError:
                caller.msg(blank_error)
                next = "_set_board"

            text = None
            options = (
                {
                    "key": "_default",
                    "desc": None,
                    "goto": next,
                },
            )

            ret = text, options
            return ret

        text = self._set_board.__doc__
        options = (
            {
                "key": "_default",
                "desc": None,
                "goto": next,
            },
        )

        ret = text, options
        return ret

    def _set_bucket(self, caller, raw_string):
        """Set bucket name

        # Todo: write up bucket name documentation

        """
        # Jobs tie in
        next = "do"

        def do(caller, raw_string):
            """this sets the bucket name"""
            if isblank(raw_string):
                caller.msg(blank_error)
                next = "_set_bucket"
            else:
                self.org_opts["bucket"] = raw_string.strip()[0:11]
                caller.msg(set_msg)
                next = "_start"

            text = None
            options = (
                {
                    "key": "_default",
                    "desc": None,
                    "goto": next
                },
            )

            ret = text, options
            return ret

        text = self._set_bucket.__doc__
        options = (
            {
                "key": "_default",
                "desc": None,
                "goto": next,
            },
        )
        ret = text, options
        return ret

    def _set_vault(self, caller, raw_string):
        """Set inventory options

        # Todo: write up bucket name documentation


        """
        next = "do"

        def do(caller, raw_string):
            """This actually sets the inventory system values.

            # Todo: design and implement logic for setting options
            # Todo: Need to figure out exactly /what/ options we want in a group inventory system


            ### _Thoughts_:
            We may need to test for the pre-existance of an inventory system - perhaps some sort of global/system variable
            for a Are you using an Inventory system? Type thing.  If not, we can set some sane defaults or we can write it so this can be ignored
            That should be fairly true for all of the systems.
            """
            text = None
            options = (
                {
                    "key": "_opt1",
                    "desc": None,
                    "goto": "_opt1",
                },
                {
                    "key": "_opt2",
                    "desc": None,
                    "goto": "_opt2",
                },
                {
                    "key": "_opt3",
                    "desc": None,
                    "goto": "_opt3",
                },
                {
                    "key": "_opt4",
                    "desc": None,
                    "goto": "_opt4",
                },
            )

            ret = text, options
            return ret

        text = self._set_vault.__doc__
        options = (
            {
                "key": "_default",
                "exec": "self._get_input",
                "goto": next
            },
        )
        ret = text, options
        self.org_opts["vault"] = self.player_input

        # Create and populate
        opts = self.org_opts
        self.org = Org.create(name=opts["name"], desc=opts["desc"])
        self.org.db.board = opts["board"]
        self.org.db.bucket = opts["bucket"]
        self.org.db.vault = opts["vault"]
        return ret

    def _switch_parser(self, switch):
       """process and run the switches

       :return: Success or error message
       """
       switches = ["add", "create", "list", "delete", "remove", "rename",]
       switch = switch.lower()

       if switch in switches:
           # do stuff
           if switch == "add":
               if can(self.caller, "add"):
                   if not self.org.is_member(character):
                       ret = SUCC_PRE + "{0} added to {1}".format(self.target_string, self.org_string)
                   else:
                       ret = ERROR_PRE + "{0} is already a member of {1} org".format(self.target_string, self.org_string)
               else:
                   ret = ERROR_PRE + "You do not have permission to do that."

           elif switch == "list":
               # Todo: format table display
               if can(self.caller, "list"):
                   ret = org_list() # Todo: write org_list
               else:
                   ret = ERROR_PRE + "You do not have permission to do that."

           elif switch == "delete":
               # Todo: fix logging
               if can(self.caller, "delete"):
                   if is_org(self.org_string):
                       try:
                           self.org.stop()
                           ret = SUCC_PRE + "{0} deleted.".format(self.org_string)
                       except Exception as e:
                           ret = ERROR_PRE + "Something bad happened on deletion.  We're working on getting logging going, be patient."
                           raise e
               else:
                   ret = ERROR_PRE + "You do not have permission to do that."

           elif switch == "remove":
               if can(self.caller, "remove"):
                   if self.org.is_member(self.target_string):
                       character = assign_character(self.target_string)
                       self.org.remove(character)
                       ret = SUCC_PRE + "{0} removed from {0} org".format(self.target_string, self.org_string)
               else:
                   ret = ERROR_PRE + "You do not have permission to do that."

           elif switch == "rename":
               if can(self.caller, "rename"):
                   if is_org(self.org_string):
                       self.org.key = self.target_string
                       ret = SUCC_PRE + "{0} org renamed to {1}".format(self.org_string, self.target_string)
               else:
                   ret = ERROR_PRE + "You do not have permission to do that."

           else:
               ret = "Something very bad happened with a switch."
               raise ValueError("Something very bad happened with a switch.")

           ret = "something"
       else:
           ret = "some error"
           raise ValueError("The switches available to the org command are: {0}".format(repr(switches)))
       return ret

    def can(self, character, switch):
       """:return: boolean permission to access switch"""
       # Todo: fix can()
       ret = True
       return ret
