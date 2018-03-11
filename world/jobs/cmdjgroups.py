
from evennia import default_cmds
MuxCommand = default_cmds.MuxCommand


class CmdJgroups(MuxCommand):
    """
    Usage:
        +jgroups/[switches]

        /info <jgroup>
        /create <jgroup>=<description>
        /delete <jgroup>
        /member <player>=<jgroup>


    Description:

        +jgroups    - aggregate lists of names to be able to do group (un)tagging,
                      (un)assigning, query,  and source commands
    """

    key = "jgroups"
    aliases = ["+jgroups"]
    lock = "cmd:perm(Admin)"
    help_category = "Jobs"

    def info(self, jgroup):
        pass

    def create(self, jgroup, description):
        pass

    def delete(self, jgroup):
        pass

    def member(self, player, jgroup):
        pass

    def func():
        """This does the work of the jgroups command"""
        pass
