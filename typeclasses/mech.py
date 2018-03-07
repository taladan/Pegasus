# in the new file mygame/typeclasses/mech.py

from objects import Object
from commands.mechcommands import MechCmdSet

class Mech(Object):
    """
    This typeclass describes an armed Mech.
    """
    def at_object_creation(self):
        "This is called only when object is first created"
        self.cmdset.add_default(MechCmdSet)
        self.locks.add("puppet:all()")
        self.db.desc = "This is a huge mech.  It has missles and stuff."
