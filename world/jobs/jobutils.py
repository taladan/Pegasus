from builtins import object
import evennia as ev
import jobs_settings as settings

class Utils(object):

    def __init__(self):
        pass

    def isbucket(self, obj):
        test = ev.ChannelDB.objects.search_channel(repr(obj))
        print(test)
        if test is not None:
            print("True")
            return True
        else:
            print("False")
            return False

    def ischaracter(self, obj):
        return ev.utils.utils.inherits_from(obj, "typeclasses.characters.Character")

    def isaccount(self, obj):
        return ev.utils.utils.inherits_from(obj, "typeclasses.accounts.Account")

    def isbucket(self, obj):
        return ev.utils.utils.inherits_from(obj, "typeclasses.accounts.Account")

    def test(self, msg, caller):
        caller.msg(settings._TEST_PRE + msg)

