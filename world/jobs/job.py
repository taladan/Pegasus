
import evennia as ev
from evennia.utils import lazy_property
from jobs_settings import VALID_JOB_ACTIONS
import jobutils as ju
from world.jobs.bucket import Bucket

class Job(Bucket):
    """Job object for holding messages and replies

    Methods:
    ---
    * create - this creates a job with a unique hash and assigns it to a bucket.
        - requires Job.create(bucket, title, msgtext)
    * info - returns info about a job


    """

    def at_channel_creation(self):
        """This is done when the bucket is created

        The following attributes are inherited from Bucket:

        self.db.approval_board = '0'
        self.db.completion_board = '0'
        self.db.createdby = None
        self.db.denial_board = '0'
        self.db.due_timeout = 0
        self.db.timeout_string = "0"
        self.db.num_completed_jobs = 0
        self.db.num_approved_jobs = 0
        self.db.num_denied_jobs = 0
        self.db.num_of_jobs = self.associated
        self.db.total_jobs = self._total_jobs
        self.db.per_player_actions = {}
        self.db.percent_complete = self._pct_complete
        self.db.resolution_time = 0
        self.db.valid_actions = VALID_BUCKET_ACTIONS
        self.db.valid_settings = VALID_BUCKET_SETTINGS
        self.db.default_notification = SUCC_PRE + "A new job has been posted to %s" % ju.decorate(self.db.key)
        self.db.group = "admin"
        """
        # Todo: determine vars needed for a Job obj
        self.valid_actions = VALID_JOB_ACTIONS
        self.db.actions_list = {}
        self.db.assigned_to = False
        self.db.assigned_by = False
        self.db.checked_out = False
        self.db.checker = ""
        self.db.comments = {}
        self.db.bucket = ""
        self.db.due = False
        self.db.locked = False
        self.db.messages = {}
        self.db.status = "new"
        self.db.tagged = []
        self.db.title = ""
        self.db.priority = ""
        self.ndb.all = self._all

    def create(self, bucket, title, msgtext):
        """Create new job
        Syntax:
        +job/create <bucket>/<title>=<comments>
        (cmd/v lh.n/lh.v = rh.n)

        :param self: Job
        :param bucket:lh.n
        :param title:lh.v
        :param text:rh.n
        :return: dict{
                    "act": action code (str),
                    "actlist: Action list (tuple),
                    "caller": Enactor (ev object),
                    "stat": Exit status (global string),
                    "sysmsg": Message (str),
                    }
        """

        from jobs_settings import ERROR_PRE
        from jobs_settings import SUCC_PRE

        try:
            # return message data
            act = "cre"
            code = SUCC_PRE
            sysmsg = "Job: {0} created".format(ju.decorate(title))

            # hash the job for an id
            jid = self._hashobj(bucket=bucket, title=title)

            # create the job
            job = ev.create_channel(jid, desc=title, typeclass="world.jobs.job.Job")

            # add creation metadata
            job.db.id = jid
            job.tags.add(bucket, category="jobs")
            job.tags.add(jid, category="jobs")

            # add the actual message
            job._add_msg(jid=jid, bucket=bucket, title=title, msgtext=msgtext, action=act, parent=jid)

        except Exception as e:
            # Capture exception data for processing and returning
            act = False
            code = ERROR_PRE
            sysmsg = "Unexpected error of type: {0}, Arguments: {1}".format(type(e).__name__, e.args)
            job = False
            # Reraise the error
            raise
        ret = {"act": act, "exit_status": code, "msg": sysmsg, "job": job,}
        return ret

    def info(self):
        """return job info

        :return: job info
        """
        ret = (self.db.bucket,
               self.db.title,
               self.db.createdby,
               self.db.due,
               self.db.assigned_to)
        return ret

    @lazy_property
    def _all(self):
        return True

    def _hashobj(self, **kwargs):
        """create a hash and return it"""
        import hashlib
        import random
        from datetime import datetime as date

        # Grab the arguments
        bucket = kwargs.pop("bucket")
        title = kwargs.pop("title")


        # What we're hashing - uses date.today() and repr(random.random()) to get a unique hash.
        hashable = "{0}, {1}, {2}, {3}".format(
            bucket,
            title,
            date.today().strftime("%B %d, %Y at %H:%M:%S"),
            repr(random.random()),
        )

        # Create the hash
        hash = hashlib.md5(hashable.encode("utf-8")).hexdigest()
        return hash

    def _act_update(self, i, act):
        self.db.actions_list[i] = act

    def _add_msg(self,**kwargs):
        """add message to job

         * Set attributes that reflect a message being added to the job
         * Peform hash of message to get unique identifier
         * Save message to job
         * Update the action code
        """

        # assign attributes
        self.db.jid = kwargs.pop("jid")
        self.db.bucket = kwargs.pop("bucket")
        self.db.title = kwargs.pop("title")
        self.db.parent = kwargs.pop("parent")

        act = kwargs.pop("action")
        msgtext = kwargs.pop("msgtext")

        # Id the message
        msghash = self._hashobj(bucket=self.db.bucket, title=self.db.title)
        self.db.messages[msghash] = msgtext

        # update the action list
        self._act_update(msghash, act)
