

"""Main utilities file for Pegasus Project systems

"""

# imports go here
import evennia as ev

# foobar
__author__ = "Jamie Crosby"
__copyright__ = "Copyright 2018, The Pegasus Project"
__credits__ = ["Jamie Crosby",]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "Jamie Crosby"
__email__ = "taladan@gmail.com"
__status__ = "Prototype"


class StringTools(object):
    """general tools for dealing with strings across the Pegasus framework"""
    def __init__(self, *args):
        self.string = args

    def junk(self, segment):
        def _pack(segment):
            """parse for '/' :return: list (pack)"""
            ret = []

            if "/" in segment:
                noun, verb = segment.split("/")
            else:
                noun = segment
                verb = False

            pack = noun, verb
            ret.append(pack)
            return ret

        ret = []
        # rhs & lhs
        if "=" in string:
            strings = (first, last) = string.split('=')
            for string in strings:
                res = _pack(string)
                for i in res:
                    ret.append(_pack(string))
        # lhs only
        elif '/' in string:
            strings = (first, last) = string.split('/')
            for string in strings:
                res =_pack(string)
                for i in res:
                    ret.append(_pack(string))

            # RHS doesn't exist
            noun = False
            verb = False
            ret.append(rhs_noun)
            ret.append(rhs_verb)
        else:
            ret = string, False, False, False

        return tuple(ret)

    def parse_args(self, string):
        """split args at '=' and '/'

         :return: noun/verb pairs for any segment in args
         """
        def _slash(string):
            if "/" in string:
                noun, verb = string.split("/")
            else:
                noun, verb = string, False
            ret = noun, verb
            return ret

        def _eq(string):
            if "=" in string:
                lhs, rhs = string.split("=")
                lhs_noun, lhs_verb = _slash(lhs)
                rhs_noun, rhs_verb = _slash(rhs)
            else:
                lhs = string
                lhs_noun, lhs_verb = _slash(lhs)
                rhs_noun, rhs_verb = False, False
            ret = lhs_noun, lhs_verb, rhs_noun, rhs_verb
            return ret

        ret = _eq(string)
        return ret

def assign_character(character):
    """take a character string and return the correct query object"""
    return ev.search_object(character)

def is_board(board):
    # Todo: fix when bbsys is integrated
    boards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if not board.isdigit():
        ret = False
    elif board in boards:
        ret = True
    else:
        ret = False

    return ret

def is_character(character):
    """return bool of character status"""
    return character in ev.DefaultCharacter.objects.all()

def is_date(string):
    """determine if string is a date"""
    from dateutil.parser import parse
    try:
        parse(string)
        ret = True
    except ValueError:
        ret = False
    return ret

def is_org(string):
    """return boolean if string is a group"""
    groups = Group().list
    names = []
    for group in groups:
        names.append(group.key.lower())
    return string.lower() in names

def days_past(date):
    """return how many days have passed since date"""
    from datetime import datetime, timedelta
    now = datetime.now()
    # Todo: finish
    # if date.lower() == "now":
    #     pass
    # else:
    #     pass

def days_until(date):
    """return how many days until date"""
    from datetime import datetime, timedelta
    now = datetime.now()
    # Todo: finish

def isblank(obj):
    """Test object for length

    :return: True if obj has no length"""
    try:
        len(obj)
        ret = False
    except TypeError:
        ret = True

    return ret

def input(caller, raw_string):
    """get input from the user"""
    return raw_string.strip()

def hash(**kwargs):
    """create a hash and return it

    :keyword: key: The db key of the item to be hashed
    :keyword: string: Any string object to hash
    :return: hash: A unique md5().hexdigest string
    """

    import hashlib
    import random
    from datetime import datetime as date

    # Grab the arguments
    key = kwargs.pop("key")
    string = kwargs.pop("string")


    # What we're hashing - uses date.today() and repr(random.random()) to get a unique hash.
    hashable = "{0}, {1}, {2}, {3}".format(
        key,
        string,
        date.today().strftime("%B %d, %Y at %H:%M:%S"),
        repr(random.random()),
    )

    # Create the hash
    hash = hashlib.md5(hashable.encode("utf-8")).hexdigest()
    return hash

def hastag(object, tag):
    """determine if a object has a particular tag on it

    :return:boolean
    """
    return tag in object.tags.all()

def log(msg, exception, system):
    from evennia.utils.logger import EvenniaLogFile
    log = EvenniaLogFile()
    logfile = system + ".log"
    exception = exception + "\n"
    msg = exception + msg
    log.log_file(msg, logfile)


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