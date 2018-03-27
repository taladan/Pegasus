
from jobutils import Utils
from bucket import Bucket
from jobs_settings import VALID_JOB_ACTIONS

ju = Utils()

class Job(Bucket):
    """
    * Messages belong to a job
    * Jobs belong to buckets
    * Messages can not belong to a bucket
    * Perhaps allow a "Reply" type functionality that appends messages to extant messages
        Reply structure:

        +job/reply Job/id=message

        The job will be the listing of the job in the order of self.jobs_list

        Ideas for tiered level commenting system:
            Each message should have a unique id (hash)
            Comment children can be handled via tags.

        My ideas on access:
            Players who run factions should be able to be tagged as "BucketAdmin" category:"jobs"
            and be allowed to administer just that bucket for faction stuff...perhaps a jobs
            subsystem for guilds or factions so they can separate issues?

            Need hooks so that when a person is added to a faction the addition to the job/bbsys
            can be automagic.

            Anomaly stuff:
                Jobs has a tiered access structure. By changing who has access to
                various commands, you can selectively allow players like builders into the
                system so they can work. The access locks are on the bucket object.
                Bucket access locks are stored at the bucket level.

                  HAS_ACCESS: Return TRUE if a player can access the +jobs system.

                     ADD_ACCESS:      Returns True if a player can use the /add command.
                     APPROVE_ACCESS:  Returns True if a player can /approve jobs.
                     COMPLETE_ACCESS: Returns True if a player can /complete jobs.
                     CREATE_ACCESS:   Returns True if a player can use the /create command.
                     DENY_ACCESS:     Returns True if a player can /deny jobs.
                     EDIT_ACCCESS:    Returns True if a player can use the /edit command.
                     GIVE_ACCESS:     Returns True if a player can use +bucket/access.
                     LOG_ACCESS:      Returns True if a player can /log a job.
                     MAIL_ACCESS:     Returns True if a player can /query and /mail.
                     STATS_ACCESS:    Returns True if a player can pull reports on the system.

                  A player must pass HAS_ACCESS before the other locks are applied.

                  Access to buckets are set at the bucket level (see 'baccess').
                  You can also restrict actions by bucket (see 'aaccess').

                  Actions can be restricted by bucket. This allows you to customize the
                  available actions to, for instance, prevent jobs from being tampered
                  with in automated buckets. The format for this is:

                  &<action code>_ACCESS <bucket>=<return 1 to access, 0 to deny>

                  The <action>_ACCESS code allows for one argument: %0 == PlayerDB#.

                       Example: If you do not want a job to ever be transferred out
                       of an automated XP bucket (not included) you can prevent
                       this behavior if you know the three-letter action code (in this
                       example, TRN):

                       &TRN_ACCESS XP=0

                  See also: access, codes

                  Bucket access is set on the bucket itself, as the ACCESS attribute:

                     &ACCESS <Bucket DB#>=[switch(get(%0/RACE),VAMPIRE,1,0)]

                  It should return True for access and False for no access.
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
        self.db.status = "new"
        self.db.tagged = []
        self.db.title = ""
        self.db.priority = ""
        self.ndb.all = self._all()

    def info(self):
        ret = (self.db.bucket,
               self.db.title,
               self.db.createdby,
               self.db.due,
               self.db.assigned_to)
        return ret

    # def _approve(self, jobid, comment):
    # def _assign(self, jobid, player=None):
    # def _catchup(self):
    # def _checkin(self, jobid):
    # def _clean(self):
    # def _credits(self):
    # def _checkout(self, jobid):
    # def _claim(self, jobid):
    # def _clone(self, jobid):
    # def _complete(self, jobid, comment):
    # def _create(self):
    # def _delete(self, jobid):
    # def _deny(self, jobid, comment):
    # def _due(self, jobid, date=None):
    # def _edit(self, jobid, entryid, old, new):
    # def _esc(self, jobid, priority):
    # def _help(self, jobid):
    # def _joblist(self, *args, **kwargs):
    # def _last(self, jobid, num):
    # def _list_untag(self, jobid, player_list):
    # def _list(self, bucket):
    # def _lock_job(self, jobid):
    # def _log(self, jobid):
    # def _mail(self, jobid, message):
    # def _merge(self, source, destination):
    # def _overdue(self):
    # def _player_tag(self, jobid, player):
    # def _pri(self):
    # def _publish(self, jobid, comment):
    # def _query(self, player_list, title, query):
    # def _rename(self, jobid, name):
    # def _reports(self, report=None):
    # def _search(self, pattern):
    # def _select(self, expression):
    # def _set(self, jobid, status):
    # def _sort(self, sorttype):
    # def _source(self, jobid, player_list):
    # def _summary(self, jobid):
    # def _sumset(self, jobid, sumset, value):
    # def _tag(self, jobid):
    # def _trans(self, jobid, bucket):
    # def _unlock(self, jobid):
    # def _untag(self, jobid):
    # def _who(self, jobid):
    # def _assign_job(self):
