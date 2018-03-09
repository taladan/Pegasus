

from datetime import datetime
import evennia as ev
from typeclasses.channels import Channel
from evennia.utils import lazy_property
from jobutils import Utils
import jobs_settings as settings

_VALID_BUCKET_SETTINGS = settings._VALID_BUCKET_SETTINGS
_VALID_BUCKET_ACTIONS = settings._VALID_BUCKET_ACTIONS

date = datetime
ju = Utils()

class Bucket(Channel):
    """
    The Bucket is the base object for the jobs system.  This object
    inherits from the Channel object so that it can use the underlying
    hooks to deliver messages to Users.
    """

    def at_channel_creation(self):
        """This is done when the bucket is created"""
        # set sane defaults
        self.db.approval_board = '0'
        self.db.completion_board = '0'
        self.db.createdby = None
        self.db.createdon = '{:%m-%d-%Y at %H:%M %Z}'.format(date.utcnow())
        self.db.denial_board = '0'
        self.db.due_timeout = 0
        self.db.timeout_string = "0"
        self.db.completed_jobs = 0
        self.db.num_of_jobs = len(self.associated)
        self.db.per_player_actions = {}
        self.db.percent_complete = 0
        self.db.resolution_time = 0
        self.db.valid_actions = _VALID_BUCKET_ACTIONS
        self.db.valid_settings = _VALID_BUCKET_SETTINGS
        self.db.group = "admin"

    @lazy_property
    def associated(self):
        """search for and return any jobs associated with this bucket"""
        jobs = []
        for job in ev.search_tag(self.key, category="jobs"):
            jobs.append(job)
        return jobs

    def check_access(self, obj):
        """return whether the caller is in the actions dict"""
        if self.db.per_player_actions.keys() is not None:
            return obj in self.db.per_player_actions.keys()

    def grant_access(self, action, obj):
        """give an object access to a bucket"""
        action = [action]
        ppa = self.db.per_player_actions
        for act in action:
            if obj in ppa.keys():
                ppa[obj].append(act)
            else:
                ppa[obj] = [act]

    def has_jobs(self):
        """return true if the bucket has any jobs on it, false if not"""
        return self.db.num_of_jobs < 0

    def has_access(self, action, obj):
        """if self.caller is on the access list, allow this action"""
        ppa = self.db.per_player_actions.get(obj)
        return ppa and action in ppa
        # if obj is not None:
        #     if obj.locks.check_lockstring(obj, "dummy:perm(Admin)"):
        #         return True
        #     else:
        #         return ppa and action in ppa
        # else:
        #     return False

    def info(self):
        """returns bucket info as a list"""
        ret = [self.key,
               self.db.desc,
               self.db.num_of_jobs,
               self.db.percent_complete,
               self.db.completion_board,
               self.db.approval_board,
               self.db.denial_board,
               self.db.timeout_string,
               self.db.resolution_time,]
        return ret

    def monitor(self, obj):
        """Allows you to see a bucket when you type +jobs.  Toggling it again turns it off"""
        pass

    def remove_access(self,action, obj):
        """removes action access from obj for bucket"""
        try:
            self.db.per_player_actions[obj].remove(action)
            return True
        except KeyError:
            return false

    def set(self, setting, value, **kwargs):
        """used to change settings on a particular bucket"""
        if "interval" in kwargs:
            interval = kwargs.pop("interval")
            self.db.due_timeout = value
            self.db.interval = interval
            self.db.timeout_string = str(self.db.due_timeout) + " " + self.db.interval
        else:
            attr = "self.db." + _VALID_BUCKET_SETTINGS[setting]
            exec(attr + "=" + str(value))
