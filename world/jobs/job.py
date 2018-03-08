
from jobs_settings import *

class Job(Bucket):

    # TODO: Access stuff:

    """
    I can have a jobtype - bucket or job, each one is a channel.

    flags:
        jobtype
        isjob
        ismessage

    * Messages belong to a job
    * Jobs belong to buckets
    * Messages can not belong to a bucket
    * Perhaps allow a "Reply" type functionality that appends messages to extant messages
    *
    """
    """
        My ideas on access:
            Players who run factions should be able to be tagged as a bucket administrator
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
        self.tags.add(self.bucketname)
        self.valid_actions = _VALID_JOB_ACTIONS

    def create_job(self, **kwargs):
        """create and populate job instances"""
        creator = self.kwargs.pop("creator")
        title = self.kwargs.pop("title")
        text = self.kwargs.pop("text")

        # Create the job
        # ev.create_channel(self.job_name, desc=text, typeclass="world.jobs.Job")

        # Populate the instance variables
        self.job.db.creator = creator
        self.job.db.title= title
        self.db.createdby = creator
        self.db.createdon = '{:%m-%d-%Y at %H:%M %Z}'.format.date.now()


