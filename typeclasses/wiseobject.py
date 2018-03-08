from random import choice
from typeclasses.objects import Object

class WiseObject(Object):
    """
    An object speaking when someone looks at it.
    We assume it looks like a stone in this example.
    """
    def at_object_creation(self):
        "Called when object is firxt created"
        self.db.wise_texts = \
                ["Stones have feelings too.",
                 "To live like a stone is to not have lived at all.",
                 "The world is like a rock of chocolate.",
                 "Obduracy is a blessing.",
                 "Patience like a stone.",]

    def return_appearance(self, looker):
        """
        Called by the look command.  We want to return
        a wisdom when we get looked at.
        """
        # first get the base string from the
        # parent's return_appearance.
        string = super(WiseObject, self).return_appearance(looker)
        wisewords = "\n\nIt grumbles and says: '%s'"
        wisewords = wisewords % choice(self.db.wise_texts)
        return string + wisewords
