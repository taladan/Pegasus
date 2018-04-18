
import evennia as ev
import jobs_settings as settings
from evennia.utils import lazy_property
from evennia.utils import logger as log
from typeclasses.channels import Channel
import jobutils as ju
import world.utilities.pegasus_utilities as pegasus

VALID_BUCKET_SETTINGS = settings.VALID_BUCKET_SETTINGS
VALID_BUCKET_ACTIONS = settings.VALID_BUCKET_ACTIONS
SUCC_PRE = settings.SUCC_PRE
ERROR_PRE = settings.ERROR_PRE



# todo: hasacces/ppa    04-13-18, (12:53) -

class Bucket(Channel):
    """
    The Bucket is the base object for the jobs system.  This object
    inherits from the Channel object so that it can use the underlying
    hooks to deliver messages to Users.
    Todo: Work on jobs integration and finish setting up monitoring
    # self.db.total_jobs = ev.search_tag(self.db.key, category="jobs")
    """
    def at_channel_creation(
            self):
        """This is done when the bucket is created"""
        self.db.approval_board = '0'
        self.db.completion_board = '0'
        self.db.createdby = None
        self.db.denial_board = '0'
        self.db.due_timeout = 0
        self.db.group = "admin"
        self.db.hash = pegasus.hash(key=self.db.key, string=self.db.desc)
        self.db.locked = False
        self.db.num_completed_jobs = 0
        self.db.num_approved_jobs = 0
        self.db.num_denied_jobs = 0
        self.db.num_of_jobs = self.associated
        self.db.resolution_time = 0
        self.db.percent_complete = self._pct_complete
        self.db.total_jobs = self._total_jobs
        self.db.valid_actions = VALID_BUCKET_ACTIONS
        self.db.valid_settings = VALID_BUCKET_SETTINGS
        self.db.default_notification = SUCC_PRE + "A new job has been posted to {0}".format(ju.decorate(self.db.key))

    @lazy_property
    def associated(self):
        """search for and return any jobs associated with this bucket"""
        jobs = []
        # Todo: fix search for jobs
        from job import Job
        try:
            for job in Job.objects.all():
                if job.db.bucket == self:
                    jobs.append(job)
        except Exception as e:
            template = "Caught exception of type: {0}, Arguments: {1}".format(type(e), e.args)
        return len(jobs)

    def per_player_actions(self, character):
        """per_player_actions returns the bucket attribute from the player (if any)"""
        hash = self.db.hash
        ret = character.db.hash
        return ret

    def create(self, **kwargs):
        """create bucket if it doesn't exist

       :return: dict with message
        """
        bucket = kwargs.pop("bucket").capitalize()
        desc = kwargs.pop("desc")
        self.bucket = None

        # Bucket exists?
        if ju.isbucket(bucket):
            code = ERROR_PRE
            sysmsg = "Bucket: {0} already exists".format(ju.decorate(bucket))
        else:
            try:
                # Package the message
                code = SUCC_PRE
                sysmsg = "Bucket: {0} created".format(ju.decorate(bucket))

                # create the bucket
                self.bucket = ev.create_channel(bucket, desc=desc, typeclass=Bucket)
            # Bad juju beyond
            except Exception as e:
                # build the stack for trace
                time = log.timeformat()
                code = ERROR_PRE
                sysmsg = "Unexpected error of type: {0}, Arguments: {1}".format(type(e).__name__, e.args)
                stack = time + "-->" + code + sysmsg

                #log
                log.log_trace(stack)

                # Reraise the error
                raise
        if self.bucket is None:
            self.bucket = False

        ret = {"bucket": self.bucket, "code": code, "sysmsg": sysmsg}
        return ret

    def grant_access(self, action, character):
        """give a character access to a bucket"""
        action = [action]
        actions = self.db.per_player_actions(character)
        for act in action:
            if act not in actions:
                actions.appenc(act)

    def has_jobs(self):
        """return true if the bucket has any jobs on it, false if not"""
        return self.db.num_of_jobs < 0

    def has_access(self, action, character):
        """if self.caller is on the access list, allow this action"""
        # Todo: refactor for per_player_actions()
        actions = self.db.per_player_actions(character)
        return action in actions

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

    def monitoring(self, obj):
        """Tracks those monitoring a bucket."""
        # self.monitors = self.
        pass

    @lazy_property
    def _pct_complete(self):
        """returns a lazy percentage complete"""
        if self.db.num_completed_jobs and self.db._total_jobs is not None:
            return self.db.num_completed_jobs/self.db._total_jobs*100
        else:
            return 0

    def remove_access(self, action, character):
        """removes action access from obj for bucket"""
        try:
            action = action.lower()
            actions = self.db.per_player_actions(character)
            actions.remove(action)
            ret = True
        except ValueError:
            ret = False
        return ret

    @staticmethod
    def my_jobs(self):
        return ev.search_tag(self.db.key, category="jobs")

    def jobids(self):
        buckets = Bucket.objects.all()
        jobs = []
        for bucket in buckets:
           jobs.extend(job for job in bucket.my_jobs)
        return jobs

    def set(self, setting, value, **kwargs):
        """used to change settings on a particular bucket"""
        if "interval" in kwargs:
            interval = kwargs.pop("interval")
            self.db.due_timeout = value
            self.db.interval = interval
            self.db.timeout_string = str(self.db.due_timeout) + " " + self.db.interval
        else:
            attr = "self.db." + VALID_BUCKET_SETTINGS[setting]
            exec("%s = '%s'" % (attr, str(value).capitalize()))

    @lazy_property
    def _total_jobs(self):
        """returns the total number of jobs processed by and still on the system"""
        # Todo: refactor for clarity
        if not self.db.num_of_jobs:
            ret = self.db.num_completed_jobs + self.db.num_approved_jobs + self.db.num_denied_jobs
        else:
            ret = self.db.num_completed_jobs + self.db.num_approved_jobs + self.db.num_denied_jobs + self.db.num_of_jobs
        return ret
