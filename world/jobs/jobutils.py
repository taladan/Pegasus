

"""Jobs utilities v0.2"""
import evennia as ev
import jobs_settings as settings

def argparse(lhs, rhs):
    """
    :param lhs: Arguments from the left side of an = (self.lhs)
    :param rhs: Arguments from the right side of an = (self.rhs)
    :return: argument list (lhs_obj, lhs_act, rhs_obj, rhs_act) or False
    """
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
    else:
        ret = False
    return ret

def assign_channel(string):
    """
    :param string: Any string name of a channel object
    :return: Channel object matching string
    """
    return ev.ChannelDB.objects.get_channel(string)

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

def exists(*args):
    """
    Tests args for None
    :param args:
    :return: True if all args are not none
             False if any arg is none
    """
    return all(v is not None for v in args)

def decorate(*args):
    """Takes any num of args and returns them decorated with the desired color code"""
    ret = []
    for text in args:
        ret.append(settings.TEXT_COLOR + str(text) + "|n")
    return tuple(ret)

def is_character(string):
    return ev.utils.utils.inherits_from(string, "typeclasses.characters.Character")

def isaccount(string):
    return ev.utils.utils.inherits_from(string, "typeclasses.accounts.Account")

def isbucket(string):
    """search and return true if obj string is a bucket"""
    return ev.utils.utils.inherits_from(ev.search_channel(string).first(), "world.jobs.bucket.Bucket")

def isjob(string):
    """search and return true if obj string is a job"""
    return ev.utils.utils.inherits_from(ev.search_channel(string).first(), "world.job.Job")
