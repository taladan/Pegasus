from builtins import object
import evennia as ev
import typeclasses

class Utils(object):

    def __init__(self):
        pass

    def valid_charater(self, obj):
        pass

    def ischaracter(self, obj):
        return ev.utils.utils.inherits_from(obj, "typeclasses.characters.Character")

    def isaccount(self, obj):
        return ev.utils.utils.inherits_from(obj, "typeclasses.accounts.Account")

    def test(self, msg):
        self.caller.msg(_TEST_PRE + msg)
