

# from builtins import object
import evennia as ev
import jobs_settings as settings
from evennia.utils import lazy_property

class Utils(object):

    def __init__(self):
        pass

    def argparse(self, lhs, rhs):
        if '/' in lhs or '/' in rhs:
            if '/' in lhs:
                lhs_obj, lhs_act = lhs.split('/')
            else:
                lhs_obj, lhs_act = None, None
            if '/' in rhs:
                rhs_obj, rhs_act = rhs.split('/')
            else:
                rhs_obj, rhst_act = None, None
            ret = (lhs_obj, lhs_act, rhs_obj, rhs_act)
            return ret
        else:
            return None

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
        """search and return true if obj string is a bucket"""
        return ev.utils.utils.inherits_from(ev.search_channel(obj).first(), "world.jobs.bucket.Bucket")

    def isjob(self, obj):
        """search and return true if obj string is a job"""
        return ev.utils.utils.inherits_from(ev.search_channel(obj).first(), "world.job.Job")

    def test(self, msg, caller):
        caller.msg(settings._TEST_PRE + msg)

