

"""Jobs utilities v0.2"""
import evennia as ev
import jobs_settings as settings

def assign_channel(string):
    """
    :param string: Any string name of a channel object
    :return: Channel object matching string
    """
    return ev.ChannelDB.objects.get_channel(string)

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

def ischaracter(string):
    return ev.utils.utils.inherits_from(string, "typeclasses.characters.Character")

def isaccount(string):
    return ev.utils.utils.inherits_from(string, "typeclasses.accounts.Account")

def isbucket(string):
    """search and return true if obj string is a bucket"""
    return ev.utils.utils.inherits_from(ev.search_channel(string).first(), "world.jobs.bucket.Bucket")

def isjob(string):
    """search and return true if obj string is a job"""
    return ev.utils.utils.inherits_from(ev.search_channel(string).first(), "world.job.Job")
