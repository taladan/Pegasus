

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
                lhs_obj, lhs_act = False, False
            if '/' in rhs:
                rhs_obj, rhs_act = rhs.split('/')
            else:
                rhs_obj, rhs_act = False, False
            ret = (lhs_obj, lhs_act, rhs_obj, rhs_act)
            return ret
        else:
            return False

    def assign_channel(self,obj):
        return ev.ChannelDB.objects.get_channel(obj)

    def base36encode(integer):
        """encodes integer to a base 36 number"""
        chars, encoded, sign = '0123456789abcdefghijklmnopqrstuvwxyz', '', ''

        if (integer < 0):
            sign = '-'
            integer = -1 * integer

        elif (integer == 0):
            sign = '0'

        while integer > 0:
            integer, remainder = divmod(integer, 36)
            encoded = chars[remainder] + encoded
        return sign + encoded

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

