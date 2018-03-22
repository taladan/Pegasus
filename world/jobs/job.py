
import hashlib
import evennia as ev
from jobutils import Utils
from bucket import Bucket
from jobs_settings import _VALID_JOB_ACTIONS

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
    name = None

    def at_channel_creation(self):
        """This is done when the bucket is created"""
        # Todo: determine vars needed for a Job obj
        self.valid_actions = _VALID_JOB_ACTIONS
        self.db.tagged_players = []


    def _act(self, jobid):
        """
          +job/act <#>
        Display actions on a job
        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _add(self, jobid, comment):
        """
         +job/add <#>=<comments>
         Add comments to a job
        :param self:
        :param jobid:
        :param comment:
        :return:
        """
        return ret

    def _all(self, jobid):
        """
        +job/all
        +job/all <#>
        Displays all comments in a job
        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _approve(self, jobid, comment):
        """
        job/approve <#>=<comment>
        Approves a job with a comment.
        :param self:
        :param jobid:
        :param comment:
        :return:
        """
        return ret

    def _assign(self, jobid, player=None):
        """
        job/assign <#>=<<player>|none>
        Assign a job to player
        :param self:
        :param jobid:
        :param player:
        :return:
        """
        return ret

    def _catchup(self):
        """
        job/catchup
        Clears new jobs

        :param self:
        :return:
        """
        return ret

    def _checkin(self, jobid):
        """
        job/checkin <#>
        Checks in a job

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _clean(self):
        """ job/checkout <#>
        Remove non-players from job data

        :param self:
        :return:
        """
        return ret

    def _credits(self):
        """
        job/credits
        Display credits information

        :param self:
        :return:
        """
        return ret

    def _checkout(self, jobid):
        """
        +job/checkout <#>

        Allows a user to checkout a job and lock it against changes for the duration that it is checked out.
        """
        return ret

    def _claim(self, jobid):
        """
        job/claim <#>
        Allows a user to claim a job, assigning it to that user.

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _clone(self, jobid):
        """
        job/clone <#>
        Clones a job

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _complete(self, jobid, comment):
        """
        job/complete <#>=<comment>
        Completes a job with comment
        """
        return ret

    def _compress(self):
        """
        +job/compress
        Compresses the jobs system - may be unnecessary
        """
        return ret

    def _create(self):
        """
        job/create <bucket>/<title>=<comments>
        Creates a new job in Bucket with Title and Comments

        :param self:
        :param bucket:
        :param title:
        :param text:
        :return:
        """

        # Set up our arguments
        args = [self.lhs_obj, self.lhs_act, self.rhs]
        bucket, title, text = args

        if ju.isbucket(bucket):

            if args:

                # Job Creation
                jhash = '%s %s %s %s' % (bucket, title, date.today().strftime(), str(random.randrange(1,1000000)))
                jid = hashlib.md5(jhash.encode(utf-8)).hexdigest()
                self.job = ev.create_channel(jid, desc=title, typeclass="world.jobs.job.Job")
                self.job.tags.add(bucket, category="jobs")

                # Message Creation
                msgheader = '%s, %s, %s, %s' % (self.caller, date.today().strftime("%B %d, %Y"), title,)
                msghash = '%s %s %s %s' % (self.caller, date.now(), title, str(random.randrange(1,1000000)))
                msgid = haslib.md5(jhash.encode(utf-8)).hexdigest()
                self.msg = ev.create_message(self.caller, msgtext,
                                             channels=bucket, header=msgheader,
                                             recievers=self.job.db.recievers)

                # Handle message tags
                self.msg.tags.add("Job:"+jid, category="jobs")
                self.msg.tags.add("Reply:root", category="jobs")
                self.msg.tags.add("U", category="jobs")

                ret = _SUCC_PRE + "Job: |w%s|n created." % title

            # No args
            else:
                ret = _ERROR_PRE + "The correct syntax is +job/create Bucket/Title=Text"
        # No bucket
        else:
            ret = _ERROR_PRE + "|w%s|n is an invalid bucket." % bucket

        return ret

    def _delete(self, jobid):
        """
        job/delete <#>
        deletes a job

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _deny(self, jobid, comment):
        """
        job/deny <#>=<comment>
        Denies a job with comment

        :param self:
        :param jobid:
        :param comment:
        :return:
        """
        return ret

    def _due(self, jobid, date=None):
        """
        job/due <#>=<<date>|none>
        Sets a due date on a job
        """
        return ret

    def _edit(self, jobid, entryid, old, new):
        """
        job/edit <#>/<entry #>=<old>/<new>
        Edits a specific entry on a job

        :param self:
        :param jobid:
        :param entryid:
        :param old:
        :param new:
        :return:
        """
        return ret

    def _esc(self, jobid, priority):
        """
        job/esc <#>=<green|yellow|red>
        Sets the priority of a job

        :param self:
        :param jobid:
        :param priority:
        :return:
        """
        return ret

    def _help(self, jobid):
        """
        job/help <#>
        Displays help for a job's bucket.
        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _joblist(self, *args, **kwargs):
        """
        +job/all
        +job/mine
        +job/new
        List all/yours/new jobs

        :param self:
        :param args:
        :param kwargs:
        :return:
        """
        return ret

    def _last(self, jobid, num):
        """
        job/last <#>=<X>
        This shows the last X entries on a job

        :param self:
        :param jobid:
        :param num:
        :return:
        """
        return ret

    def _list_untag(self, jobid, player_list):
        """
        job/untag <#>=<player list>
        Untags a list of players from a job
        """
        return ret

    def _list(self, bucket):
        """
        job/list <bucket>
        Displays the list of jobs in Bucket.

        :param self:
        :param bucket:
        :return:
        """
        return ret

    def _lock_job(self, jobid):
        """
        job/lock <#>
        Locks a job from any further modification

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _log(self, jobid):
        """
        job/log <#>
        Logs a particular job - want to add email functionality to this.

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _mail(self, jobid, message):
        """
        job/mail <#>=<message>
        Sends mail to the jobs source(s)

        :param self:
        :param jobid:
        :param message:
        :return:
        """
        return ret

    def _merge(self, source, destination):
        """
        job/merge <source>=<destination>
        Merges one job (source) into another (destination)

        :param self:
        :param source:
        :param destination:
        :return:
        """
        return ret

    def _overdue(self):
        """
        job/overdue
        Displays only a list of overdue jobs

        :param self:
        :return:
        """
        return ret

    def _player_tag(self, jobid, player):
        """
        job/tag <#>=<player>
        tags a job for a player or players

        :param self:
        :param jobid:
        :param player:
        :return:
        """
        return ret

    def _pri(self):
        """
        +job/pri
        Sorts job by priority in descending order

        :param self:
        :return:
        """
        return ret

    def _publish(self, jobid, comment):
        """
        +job/publish <#>[=<comment>]
        publishes a comment on a job if a comment is
        indicated, otherwise publishes a job.

        :param self:
        :param jobid:
        :param comment:
        :return:
        """
        return ret

    def _query(self, player_list, title, query):
        """
        +job/query <players>/<title>=<query>
        Sends a query to <players>

        :param self:
        :param player_list:
        :param title:
        :param query:
        :return:
        """
        return ret

    def _rename(self, jobid, name):
        """
        +job/rename <#>=<name>
        Rename a job

        :param self:
        :param jobid:
        :param name:
        :return:
        """
        return ret

    def _reports(self, report=None):
        """
        +job/reports [<report>]
        Get a report

        :param self:
        :param report:
        :return:
        """
        return ret

    def _search(self, pattern):
        """
        +job/search <pattern>
        Search jobs for <pattern>

        :param self:
        :param pattern:
        :return:
        """
        return ret

    def _select(self, expression):
        """
        +job/select <expression>
        List jobs matching <expression>

        :param self:
        :param expression:
        :return:
        """
        return ret

    def _set(self, jobid, status):
        """
        +job/set <#>=<status>
        Set progress status on a job

        :param self:
        :param jobid:
        :param status:
        :return:
        """
        return ret

    def _sort(self, sorttype):
        """
        +job/sort
        Lists jobs by bucket/mod/pri

        :param self:
        :param sorttype:
        :return:
        """
        return ret

    def _source(self, jobid, player_list):
        """
        +job/source <#>=<player list>
        Changes opened-by to <player list>

        :param self:
        :param jobid:
        :param player_list:
        :return:
        """
        return ret

    def _summary(self, jobid):
        """
        +job/summary <#>
        Views a job's header & SUMMARY

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _sumset(self, jobid, sumset, value):
        """
        +job/sumset <#>/<set>=<value>
        Changes a job SUMMARY setting

        :param self:
        :param jobid:
        :param sumset:
        :param value:
        :return:
        """
        return ret

    def _tag(self, jobid):
        """
        +job/tag <#>
        Tags a job for you

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _trans(self, jobid, bucket):
        """
        +job/trans <#>=<bucket>
        Transfer (or undelete) a job

        :param self:
        :param jobid:
        :param bucket:
        :return:
        """
        return ret

    def _unlock(self, jobid):
        """
        +job/unlock <#>
        Unlocks a job

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _untag(self, jobid):
        """
        +job/untag <#>
        Untags a job

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _who(self, jobid):
        """
        +job/who <player>
        Lists jobs assigned to player

        :param self:
        :param jobid:
        :return:
        """
        return ret

    def _assign_job(self):
        """sets self.job if it exists in the db"""
        try:
            self.job = ev.ChannelDB.objects.get_channel(self.title)
        except AttributeError:
            self.caller.msg(_ERROR_PRE + "Job: |w%s|n does not exist." % self.title)

    def func(self):
        """This does the work of the jobs command"""
        self.valid_actions = _VALID_JOB_ACTIONS
        self.jobs_list = self.all_jobs()

        if self.switches or self.args:
            if self.switches:
                if self.args:
                    passargs = ju.argparse(self.lhs, self.rhs)
                    if passargs:
                        self.lhs_obj, self.lhs_act, self.rhs_obj, self.rhs_act = passargs
                    else:
                        self.lhs_obj = self.lhs_act = self.rhs_obj = self.rhs_act = False
                output = self._action_handler(self.switches[0])
                return output
        # No switch, no args
        else:
            # +job(s) This part should just display the list of available buckets.
            for job in self.jobs_list:
                self.caller.msg(_TEST_PRE + "%s" % job)


