"""
Commands

Commands describe the input the account can do to the game.

"""

from evennia import Command as BaseCommand
from evennia import create_object
from evennia import default_cmds
import random


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """
    pass
"""test cruft below"""
# -------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
# -------------------------------------------------------------

# from evennia.utils import utils
#
#
# class MuxCommand(Command):
#     """
#     This sets up the basis for a MUX command. The idea
#     is that most other Mux-related commands should just
#     inherit from this and don't have to implement much
#     parsing of their own unless they do something particularly
#     advanced.
#
#     Note that the class's __doc__ string (this text) is
#     used by Evennia to create the automatic help entry for
#     the command, so make sure to document consistently here.
#     """
#     def has_perm(self, srcobj):
#         """
#         This is called by the cmdhandler to determine
#         if srcobj is allowed to execute this command.
#         We just show it here for completeness - we
#         are satisfied using the default check in Command.
#         """
#         return super(MuxCommand, self).has_perm(srcobj)
#
#     def at_pre_cmd(self):
#         """
#         This hook is called before self.parse() on all commands
#         """
#         pass
#
#     def at_post_cmd(self):
#         """
#         This hook is called after the command has finished executing
#         (after self.func()).
#         """
#         pass
#
#     def parse(self):
#         """
#         This method is called by the cmdhandler once the command name
#         has been identified. It creates a new set of member variables
#         that can be later accessed from self.func() (see below)
#
#         The following variables are available for our use when entering this
#         method (from the command definition, and assigned on the fly by the
#         cmdhandler):
#            self.key - the name of this command ('look')
#            self.aliases - the aliases of this cmd ('l')
#            self.permissions - permission string for this command
#            self.help_category - overall category of command
#
#            self.caller - the object calling this command
#            self.cmdstring - the actual command name used to call this
#                             (this allows you to know which alias was used,
#                              for example)
#            self.args - the raw input; everything following self.cmdstring.
#            self.cmdset - the cmdset from which this command was picked. Not
#                          often used (useful for commands like 'help' or to
#                          list all available commands etc)
#            self.obj - the object on which this command was defined. It is often
#                          the same as self.caller.
#
#         A MUX command has the following possible syntax:
#
#           name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#         The 'name[ with several words]' part is already dealt with by the
#         cmdhandler at this point, and stored in self.cmdname (we don't use
#         it here). The rest of the command is stored in self.args, which can
#         start with the switch indicator /.
#
#         This parser breaks self.args into its constituents and stores them in the
#         following variables:
#           self.switches = [list of /switches (without the /)]
#           self.raw = This is the raw argument input, including switches
#           self.args = This is re-defined to be everything *except* the switches
#           self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                      no = is found, this is identical to self.args.
#           self.rhs: Everything to the right of = (rhs:'right-hand side').
#                     If no '=' is found, this is None.
#           self.lhslist - [self.lhs split into a list by comma]
#           self.rhslist - [list of self.rhs split into a list by comma]
#           self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#           All args and list members are stripped of excess whitespace around the
#           strings, but case is preserved.
#         """
#         raw = self.args
#         args = raw.strip()
#
#         # split out switches
#         switches = []
#         if args and len(args) > 1 and args[0] == "/":
#             # we have a switch, or a set of switches. These end with a space.
#             switches = args[1:].split(None, 1)
#             if len(switches) > 1:
#                 switches, args = switches
#                 switches = switches.split('/')
#             else:
#                 args = ""
#                 switches = switches[0].split('/')
#         arglist = [arg.strip() for arg in args.split()]
#
#         # check for arg1, arg2, ... = argA, argB, ... constructs
#         lhs, rhs = args, None
#         lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#         if args and '=' in args:
#             lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#             lhslist = [arg.strip() for arg in lhs.split(',')]
#             rhslist = [arg.strip() for arg in rhs.split(',')]
#
#         # save to object properties:
#         self.raw = raw
#         self.switches = switches
#         self.args = args.strip()
#         self.arglist = arglist
#         self.lhs = lhs
#         self.lhslist = lhslist
#         self.rhs = rhs
#         self.rhslist = rhslist
#
#         # if the class has the account_caller property set on itself, we make
#         # sure that self.caller is always the account if possible. We also create
#         # a special property "character" for the puppeted object, if any. This
#         # is convenient for commands defined on the Account only.
#         if hasattr(self, "account_caller") and self.account_caller:
#             if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                 # caller is an Object/Character
#                 self.character = self.caller
#                 self.caller = self.caller.account
#             elif utils.inherits_from(self.caller, "evennia.accounts.accounts.DefaultAccount"):
#                 # caller was already an Account
#                 self.character = self.caller.get_puppet(self.session)
#             else:
#                 self.character = None

# class CmdSmile(BaseCommand):
#     """
#     A smile command
#
#     Usage:
#       smile [at] [<someone>]
#       grin [at] [<someone>]
#
#     Smiles to someone in your vicinity or to the room
#     in general.
#
#     (This initial string (The __doc__ string)
#     is also used to auto-generate the help
#     for this command)
#     """
#
#     key = "smile"
#     aliases = ["smile at", "grin", "grin at",]
#     locks = "cmd:all()"
#     help_category = "General"
#
#     def parse(self):
#         "very trivial parser"
#         self.target = self.args.strip()
#
#     def func(self):
#         "This actually does things"
#         caller = self.caller
#         if not self.target or self.target == "here":
#             string = "%s smiles." % caller.name
#             caller.location.msg_contents(string, exclude=caller)
#             caller.msg("You smile.")
#         else:
#             target = caller.search(self.target)
#             if not target:
#                 # caller.search handles error messages
#                 return
#             string = "%s smiles at you." % caller.name
#             target.msg(string)
#             string = "You smile at %s" % target.name
#             caller.msg(string)
#             string = "%s smiles at %s." % (caller.name, target.name)
#             caller.location.msg_contents(string, exclude=[caller, target])
#
#
# class CmdWait(BaseCommand):
#     """
#     A dummy command to show how to wait
#
#     Usage:
#       wait
#
#     """
#
#     key = "wait"
#     locks = "cmd:all()"
#     help_category = "General"
#
#     def func(self):
#         """Command execution."""
#         self.msg("Starting to wait ...")
#         yield 5
#         self.msg("... This shows after 5 seconds.  Waiting ...")
#         yield 2
#         self.msg("... And now another 2 seconds have passed.")
#
# class CmdConfirm(BaseCommand):
#     """
#     A dummy command to show confirmation.
#
#     Usage:
#       confirm
#
#     """
#
#     key = "confirm"
#
#     def func(self):
#         answer = yield("Are you sure you want to go on?")
#         if answer.strip().lower() in ("yes", "y"):
#             self.msg("Yes!")
#         else:
#             self.msg("No!")
#
# class CmdSetPower(Command):
#     """
#     set the power of a character
#
#     Usage:
#     +setpower <1-10>
#
#     This sets the pwoer of the current character.  This can only be
#     used during character generation.
#     """
#
#     key = "+setpower"
#     help_category = "mush"
#
#     def func(self):
#         "This performs the actual command"
#         errmsg = "You must supply a number between 1 and 10."
#         if not self.args:
#             self.caller.msg(errmsg)
#             return
#         try:
#             power = int(self.args)
#         except ValueError:
#             self.caller.msg(errmsg)
#             return
#         if not (1 <= power <= 10):
#             self.caller.msg(errmsg)
#             return
#         # At this point the argument is tested as valid.  Let's set it.
#         self.caller.db.power = power
#         self.caller.msg("Your Power was set to %i." % power)
#
#
# class CmdAttack(Command):
#     """
#     Issues an attack
#
#     Usage:
#       +attack
#
#     This will calculate a new combat score based on your Power.
#     Your combat score is visible to everyone in the same location.
#     """
#     key = "+attack"
#     help_category = "mush"
#
#     def func(self):
#         "Calculate the random score between 1-10*Power"
#         caller = self.caller
#         power = caller.db.power
#         if not power:
#             # This can happen if caller is not of
#             # our custom Character typeclass
#             power = 1
#         combat_score = random.randint(1, 10 * power)
#         caller.db.combat_score = combat_score
#
#         # annouce
#         message = "%s +attacks %s with a combat score of %s!"
#         caller.msg(message % ("You", "", combat_score))
#         caller.location.msg_contents(message %
#                                      (caller.key, "s", combat_score),
#                                      exclude=caller)
#
# class CmdCreateNPC(Command):
#     """
#     create a new npc
#
#     Usage:
#       +createNPC <name>
#
#     Creates a new, named NPC.  The NPC will start with a Power of 1.
#     """
#     key = "+createnpc"
#     aliases = ["+createNPC"]
#     locks = "call:not perm(nonpcs)"
#     help_category = "mush"
#
#     def func(self):
#         "Creates the object and names it"
#         caller = self.caller
#         if not self.args:
#             caller.msg("Usage: +createNPC <name>")
#             return
#         if not caller.location:
#             # may not create npc when OOC
#             caller.msg("You must have a location to create an npc.")
#             return
#         # Make name always start with capital letter
#         name = self.args.strip().capitalize()
#         # Create npc in caller's location
#         npc = create_object("characters.Character",
#                             key=name,
#                             location=caller.location,
#                             locks="edit:id(%i) and perm(Builders);call:false()" % caller.id)
#         # announce the creation
#         message = "%s created the NPC '%s'."
#         caller.msg(message % ("You", name))
#         caller.location.msg_contents(message % (caller.key, name), exclude=caller)
#
# class CmdEditNPC(Command):
#     """
#     Edit an existing NPC
#
#     Usage:
#       +editnpc <name>[/<attribute> [= value]]
#
#     Examples:
#       +editnpc mynpc/power = 5  - Sets your npc's power to 5
#       +editnpc mynpc/power      - Displays power value
#       +editnpc mynpc            - Shows all editable
#                                   attributes and values
#
#     This command edits an existing NPC.  You must have
#     permission to edit the NPC to use this.
#     """
#     key = "+editnpc"
#     aliases = ["+editNPC"]
#     locks = "cmd:not perm(nonpcs)"
#     help_category = "mush"
#
#     def parse(self):
#         "We need to do some parsing here"
#         args = self.args
#         propname, propval = None, None
#         if "=" in args:
#             args, propval = [part.strip() for part in args.rsplit("=", 1)]
#         if "/" in args:
#             args, propname = [part.strip() for part in args.rsplit("/", 1)]
#         # store, so we can access it below in func()
#         self.name = args
#         self.propname = propname
#         # a propval without a propname is meaningless
#         self.propval = propval if propname else None
#
#     def func(self):
#         "Do the editing"
#
#         allowed_propnames = ("power", "attribute1", "attribute2")
#
#         caller = self.caller
#         if not self.args or not self.name:
#             caller.msg("Usage: +editnpc name[/propname][=propval]")
#             return
#         npc = caller.search(self.name)
#         if not npc:
#             return
#         if not npc.access(caller, "edit"):
#             caller.msg("You cannot change this NPC.")
#             return
#         if not self.propname:
#             # this means we just list the values
#             output = "Properties of %s:" % npc.key
#             for propname in allowed_propnames:
#                 propvalue = npc.attributes.get(propname, default="N/A")
#                 output += "\n %s = %s" % (propname, propvalue)
#             caller.msg(output)
#         elif self.propname not in allowed_propnames:
#             caller.msg("You may only change %s." % ", ".join(allowed_propnames))
#         elif self.propval:
#             # assigning a new propvalue
#             # in this example, the properties are all integers...
#             intpropval = int(self.propval)
#             npc.attributes.add(self.propname, intpropval)
#             caller.msg("Set %s's property '%s' to %s" % (npc.key, self.propname, self.propval))
#         else:
#             # propname set, but not propval - show current value
#             caller.msg("%s has property %s = %s" % (npc.key, self.propname, npc.attributes.get(self.propname, default="N/A")))

class CmdAbilities(Command):
    """List abilities
    Usage:
        [+]abilities

    Displays a list of your current ability values.
    """
    key = "abilities"
    aliases = ["abi", "abil"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self):
        """implements the functionality of CmdAbilities"""
        str, agi, mag = self.caller.get_abilities()
        string = "STR: %s, AGI: %s, MAG: %s" % (str, agi, mag)
        self.caller.msg(string)
