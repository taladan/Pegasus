from evennia import Command
from evennia import CmdSet
from evennia import default_cmds

class MechCmdSet(CmdSet):
    """
    This allows mechs to do mech stuff.
    """
    key = "mechcmdset"

    def at_cmdset_creation(self):
        "Called once, when cmdset is first created"
        #self.add(default_cmds.CharacterCmdSet)
        self.add(CmdShoot())
        # self.add(CmdLaunch())

class CmdShoot(Command):
    """
    Firing the mech's gun

    Usage:
        shoot [target]

    This will fire your mech's main gun.  If no
    target is given you will shoot in the air.
    """
    key = "shoot"
    aliases = ["fire", "fire!"]

    def func(self):
        "This actually does the shooting"

        caller = self.caller
        location = caller.location

        if not self.args:
            # no argument given to command - shoot in the air
            message = "BOOM! The mech fires its gun in the air!"
            location.msg_contents(message)
            return

        # We have an argument, search for target
        target = caller.search(self.args)
        if target:
            message = "BOOM! The mech fires its gun at %s" % target.key
            location.msg_contents(message)
