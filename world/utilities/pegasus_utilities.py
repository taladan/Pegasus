

"""Main utilities file for Pegasus Project systems

"""

# imports go here

# foobar
__author__ = "Jamie Crosby"
__copyright__ = "Copyright 2018, The Pegasus Project"
__credits__ = ["Jamie Crosby",]
__license__ = "GPLv3"
__version__ = "0.1"
__maintainer__ = "Jamie Crosby"
__email__ = "taladan@gmail.com"
__status__ = "Prototype"

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
