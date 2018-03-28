
# -*- coding: utf-8 -*-
"""
Description:

    This system is designed to handle the creation and organization
    of different IC/OOC tasks, requests, feature requests, admin
    issues/discussions (such as theme development, plot development,
    and other tasks that require a collaborative environment. This
    should be similar enough to the BBS that it should feel like a
    discussion that can be closed/archived.  The idea and inspiration
    for this system is Anomaly Jobs:

        Code:    (https://tinyurl.com/ycs3b5za)
        Howto:   (https://tinyurl.com/yd46volk)

TODO: Structure:
    * bucket manager  handles tags.
    * each tag on the bucket manager is a different bucket.
    * You may have many jobs tagged to a single bucket.
    * jobs can not belong to more than one bucket at a time
    * jobs can be moved from one bucket to another.
    * jobs can only be tagged with existing bucket names.
    * Users can see any comments on any job that she can see
    * Users can comment on any job she can see
    * Non-Privilege Users can not access any buckets or jobs unless they are tagged for a specific job.

Command steps:
    * +bucket/create <Bucket> = <Description> - Create a new <Bucket> with <Description>
        - This registers a new channel as a bucket unless bucket exists

    * +bucket/rename <Bucket>=<New> - Rename a bucket may use # for old but must use string for new
        - This should identify the old bucket by name and rename it, retaining any jobs that are children of this channel

    * +bucket/delete <Bucket> - deletes a bucket (must be empty of jobs)
        - This should delete a bucket from the system unless it has jobs associated with it should take only the name of
          Bucket

    * +job/create <Bucket>=<Title>/<Text> - creates a job of <Title> with body of <Text> in <Bucket>
        - This should make sure there are no other jobs with an identical name before adding it to Bucket

    * +job/comment <Name[/#]> - adds a comment to job <Name/#>
        - Job numbers should be unique within the jobs system

    * +job/[un]tag <Player> - Tags or untags a player from a particular job.
        - A job being tagged for a specific player means their input is required/requested on the job


Author: taladan@gmail.com
"""
from datetime import datetime
import evennia as ev
from jobutils import Utils
from evennia import default_cmds
from evennia.utils import evtable
import jobs_settings as settings
from bucket import Bucket

MuxCommand = default_cmds.MuxCommand
ju = Utils()
date = datetime
CORNER_TOP_LEFT_CHAR = settings.CORNER_TOP_LEFT_CHAR
CORNER_TOP_RIGHT_CHAR = settings.CORNER_TOP_RIGHT_CHAR
CORNER_BOTTOM_LEFT_CHAR = settings.CORNER_BOTTOM_LEFT_CHAR
CORNER_BOTTOM_RIGHT_CHAR = settings.CORNER_BOTTOM_RIGHT_CHAR
BORDER_LEFT_CHAR = settings.BORDER_LEFT_CHAR
BORDER_RIGHT_CHAR = settings.BORDER_RIGHT_CHAR
BORDER_TOP_CHAR = settings.BORDER_TOP_CHAR
BORDER_BOTTOM_CHAR = settings.BORDER_BOTTOM_CHAR
HEADER_BOTTOM_LEFT_CHAR = settings.HEADER_BOTTOM_LEFT_CHAR
HEADER_BOTTOM_RIGHT_CHAR = settings.HEADER_BOTTOM_RIGHT_CHAR
HEADER_LINE_CHAR = settings.HEADER_LINE_CHAR
ERROR_PRE = settings.ERROR_PRE
SUCC_PRE = settings.SUCC_PRE
TEST_PRE = settings.TEST_PRE
VALID_BUCKET_ACTIONS = settings.VALID_BUCKET_ACTIONS
VALID_JOB_ACTIONS = settings.VALID_JOB_ACTIONS
VALID_BUCKET_SETTINGS = settings.VALID_BUCKET_SETTINGS
VALID_JOB_SETTINGS = settings.VALID_JOB_SETTINGS
VALID_TIMEOUT_INTERVALS = settings.VALID_TIMEOUT_INTERVALS


class CmdBuckets(MuxCommand):
    """
    Usage:
        +buckets[/switch syntax]

    Description:

        A bucket holds a series of jobs associated with the topic of the bucket.
        The bucket is the base object of the jobs system.  Jobs is designed to give
        the users of the system fine grained control over the entire system including
        who may access individual bucket actions.  This should allow staff to have
        control of a very useful task management system, but it also means that
        players who need to be able to administer buckets can have access to
        player controlled buckets, lending its use in faction/group based play.\f


        Available switch syntaxes:

            * - /access <bucket>/<action|all>=<character>

                This grants access to bucket administration actions

            * - /check <character>
                Displays buckets and actions Character has access to

            * - /create <bucket>=<description>
                Creates a bucket

            * - /delete <bucket>
                Deletes an empty bucket

            * - /info <bucket>
                Display status info about a bucket

            * - /monitor <bucket>
                Toggles monitoring a bucket

            * - /set <bucket>/<option>=<value>
                Sets options on a bucket

            Valid options for /set are:

                - completion = ##
                        Jobs completed from this bucket go
                        to this board.  (## Must be integer)

                        This is not necessary if your game
                        does not run a BBsys

                - approval = ##
                        Jobs approved from this bucket go
                        to this board.  (## Must be integer)

                        This is not necessary if your game
                        does not run a BBsys

                - denial = ##
                        Jobs denied from this bucket go
                        to this board.  (## Must be integer)

                        This is not necessary if your game
                        does not run a BBsys

                - due = <## <hours|days>|-1>
                        Jobs due in ## <hours|days>
                        (## must be a positive integer)
                        -1 = No timeout

                        The default is -1 which means jobs will
                        not timeout by default.

    """
    key = "buckets"
    aliases = ["+buckets", "+bucket", "bucket"]
    lock = "cmd:all()"
    help_category = "Jobs"

    def _access(self, caller):
        """grants player access to a specific bucket"""
        # Todo: fix adding multiple identical access types to bucket
        action = self.lhs_text.lower()
        if not ju.ischaracter(self.character):
            self.caller.msg(ERROR_PRE + "%s is not a valid character." % ju.decorate(self.character))
        if self.bucket.has_access(action, self.character):
            self.bucket.remove_access(action, self.character)
            caller.msg(SUCC_PRE + "Removing access to %s bucket action %s from %s"
                       % ju.decorate(self.bucket_name, action, self.character))
        elif action in self.valid_actions:
            self.bucket.grant_access(action, self.character)
            caller.msg(SUCC_PRE + "Granting access to %s bucket action %s to %s."
                       % (ju.decorate(self.bucket_name, action), self.character))
        elif action == 'all':
            caller.msg(SUCC_PRE + "Granting %s access to all bucket actions for %s %s"
                       % ju.decorate(self.character, self.bucket_name, self.valid_actions))
            self.bucket.grant_access(self.valid_actions, self.character)
        else:
            self.caller.msg(ERROR_PRE + "%s is not a valid action for Bucket: %s" % ju.decorate(action, self.bucket_name))

    def _argparse(self):
        """Check args and parse a little more tightly"""
        if self.args:
            if self.lhs:
                self.lhs_target, self.lhs_text = self._parse_left()
                self.action = self.lhs_text
                self.bucket_name = self.lhs_target

            if self.rhs:
                self.rhs_target, self.rhs_text = self._parse_right()
                self.character = self.rhs_target
            else:
                self.character = self.lhs_target
        else:
            self.bucket_name = False
            self.action = False

        # set our bucket instance
        if self.bucket_name:
            self._assign_bucket(self.bucket_name)

        # Don't do multiple switch operations - this will get confusing
        if self.switches:
            self.switch = self.switches[0].lower()
        else:
            self.switch = False

    def _assign_bucket(self, bucket):
        """sets self.bucket if it exists in the db"""
        try:
            self.bucket = ev.ChannelDB.objects.get_channel(bucket)
        except AttributeError:
            self.caller.msg(ERROR_PRE + "Bucket: %s does not exist." % ju.decorate(bucket))

    def _bucket_table(self, buckets):
        """creates and returns the populated table of bucket info"""
        ret = evtable.EvTable("Bucket", "Description", "# Jobs", "Pct", "C", "A", "D", "Due", "ARTS",
                              header=True,
                              border="table",
                              header_line_char=HEADER_LINE_CHAR,
                              width=110,
                              corner_top_left_char=CORNER_TOP_LEFT_CHAR,
                              corner_top_right_char=CORNER_TOP_RIGHT_CHAR,
                              corner_bottom_left_char=CORNER_BOTTOM_LEFT_CHAR,
                              corner_bottom_right_char=CORNER_BOTTOM_RIGHT_CHAR,
                              border_left_char=BORDER_LEFT_CHAR,
                              border_right_char=BORDER_RIGHT_CHAR,
                              border_top_char=BORDER_TOP_CHAR,
                              border_bottom_char=BORDER_BOTTOM_CHAR)

        # layout the column widths
        ret.reformat_column(0, width=12, align="l")  # Bucket
        ret.reformat_column(1, width=45, align="l")  # Description
        ret.reformat_column(2, width=8, align="r")   # Number of Jobs
        ret.reformat_column(3, width=5, align="r")   # Percent completed
        ret.reformat_column(4, width=4, align="r")   # Completion Board
        ret.reformat_column(5, width=4, align="r")   # Approval Board
        ret.reformat_column(6, width=4, align="r")   # Denial Board
        ret.reformat_column(7, width=10, align="l")   # Due
        ret.reformat_column(8, width=10, align="r")   # Average Resolution Times

        # fix header corners
        ret.table[0][0].reformat(corner_bottom_left_char=HEADER_BOTTOM_LEFT_CHAR)
        ret.table[8][0].reformat(corner_bottom_right_char=HEADER_BOTTOM_RIGHT_CHAR)

        # populate the table.
        if isinstance(buckets, list):
            for bucket in buckets:
                if self.caller in bucket.db.per_player_actions or self._pass_lock(self.caller):
                    info = bucket.info()
                    ret.add_row(*info)
            self.caller.msg(ret)
        else:
            info = buckets.info()
            ret.add_row(*info)
            self.caller.msg(ret)

    def _can_access(self, action, obj):
        """lock validation falls through to bucket.has_access(action, obj)"""
        if self._pass_lock(obj) or (self.bucket is not None and self.bucket.has_access(action, obj)):
            return True
        else:
            return False

    def _check(self, obj):
        """displays bucket actions that an object has access to"""
        # Todo: Fix bucket check not displaying properly
        buckets = []
        actions = []
        if self._pass_lock(self.caller):
            for bucket in self.buckets:
                actions = self._check_actions(bucket, obj)
                if actions:
                    buckets.append(bucket)

            if actions:
                ret = self._check_table(buckets)
            else:
                ret = SUCC_PRE + "%s can not perform any actions on any bucket." % self.character
        else:
            ret = ERROR_PRE + "You do not have administrator access to the bucket system."

        self.caller.msg(ret)

    def _check_actions(self, bucket, obj):
        """build list of actions target can access on given bucket"""
        actions = []
        for action in self.valid_actions:
            if bucket.has_access(action, obj):
                actions.append(action[0])
        return actions

    def _check_table(self, bucket):
        """build the table for the _check and return it"""
        ret = evtable.EvTable("Buckets %s has access to:" % self.character, "Actions available to: %s" % self.character,
                              header=True,
                              border="table",
                              header_line_char="-",
                              width=95,
                              corner_top_left_char=CORNER_TOP_LEFT_CHAR,
                              corner_top_right_char=CORNER_TOP_RIGHT_CHAR,
                              corner_bottom_left_char=CORNER_BOTTOM_LEFT_CHAR,
                              corner_bottom_right_char=CORNER_BOTTOM_RIGHT_CHAR,
                              border_left_char=BORDER_LEFT_CHAR,
                              border_right_char=BORDER_RIGHT_CHAR,
                              border_top_char=BORDER_TOP_CHAR,
                              border_bottom_char=BORDER_BOTTOM_CHAR, )
        # layout the column widths
        ret.reformat_column(0, width=40, align="l")   # Buckets target can access
        ret.reformat_column(1, width=55, align="c")   # Actions available to target
        # fix header corners
        ret.table[0][0].reformat(corner_bottom_left_char=HEADER_BOTTOM_LEFT_CHAR)
        ret.table[1][0].reformat(corner_bottom_right_char=HEADER_BOTTOM_RIGHT_CHAR)
        # populate the table.
        if isinstance(bucket, list):
            for buck in bucket:
                ret.add_row(buck.key, ', '.join(str(x) for x in buck.db.per_player_actions[self.character]))
        else:
            ret.add_row(', '.join(str(x) for x in bucket.info()))
        return ret

    def _character_validate(self):
        """validates character objects"""
        char_obj = ev.search_object(self.character).first()
        if ju.ischaracter(char_obj):
            self.character = char_obj
            return True
        else:
            return False

    def _create(self):
        """creates buckets unless they already exist"""
        if self.bucket:
            self.caller.msg(ERROR_PRE + "Bucket: %s already exists." % ju.decorate(self.bucket_name))
            return
        else:
            ev.create_channel(self.bucket_name, desc=self.rhs, typeclass="world.jobs.bucket.Bucket")
            self._assign_bucket(self.bucket_name)
            self.bucket.db.createdby = self.caller
            self.caller.msg(SUCC_PRE + "Bucket: %s has been created." % ju.decorate(self.bucket_name))

    def _delete(self):
        """Deletes bucket.  Bucket may not have any jobs inside of bucket"""
        if self.bucket is not None:
            if not self.bucket.has_jobs():
                # Todo: check bucket for jobs first
                self.caller.msg(SUCC_PRE + "Bucket: %s deleted." % ju.decorate(self.bucket_name))
                ev.search_channel(self.bucket_name).first().delete()
            else:
                self.caller.msg(ERROR_PRE + "Cannot delete Bucket: %s, jobs are associated with that bucket"
                                % ju.decorate(self.bucket_name))
        else:
            self.caller.msg(ERROR_PRE + "Bucket: %s does not exist." % ju.decorate(self.bucket_name))
            return

    def _info(self, bucket):
        """Display info for particular bucket"""
        if ju.isbucket(bucket):
            bucket = ju.assign_channel(bucket)
            self._bucket_table(bucket)
        else:
            self.msg(ERROR_PRE + "That is not a valid bucket.")

    def _monitor(self, obj):
        """toggles monitoring of a particular bucket"""
        if self.bucket.has_connection(obj):
            status = True if self.caller in self.bucket.mutelist else False
            if status:
                status='On'
                self.bucket.unmute(self.caller)
            else:
                status = 'Off'
                self.bucket.mute(self.caller)
        else:
            status = 'On'
            self.bucket.connect(obj)
        self.caller.msg(SUCC_PRE + "Toggling monitor for bucket: %s %s" % ju.decorate(self.bucket_name, status))

    def _rename(self, newname):
        """renames a particular bucket"""
        if ju.isbucket(newname):
            self.caller.msg(ERROR_PRE + "Bucket: %s already exists." % ju.decorate(newname))
        else:
            self.bucket.key = newname
            self.caller.msg(SUCC_PRE + "Bucket: %s renamed to %s." % ju.decorate(self.bucket, newname))

    def _parse(self, side):
        """parses side for /"""
        if side == self.rhs:
            side = self.rhs
        else:
            side = self.lhs
        if '/' in side:
            ret = side.split('/')
        else:
            ret = [side, side]
        return ret

    def _parse_right(self):
        """parse if self.rhs has /"""
        if self.rhs is not None:
            if '/' in self.rhs:
                self.rhs_target, self.rhs_text = self._parse(self.rhs)
            else:
                self.rhs_target, self.rhs_text = self.rhs, self.rhs
            return self.rhs_target, self.rhs_text
        else:
            rhs_target, rhs_text = False, False
            return rhs_target, rhs_text

    def _parse_left(self):
        """parse if self.lhs has /"""
        if self.lhs is not None:
            if self.lhs:
                if '/' in self.lhs:
                    lhs_target, lhs_text = self._parse(self.lhs)
                else:
                    lhs_target, lhs_text = self.lhs, self.lhs
                return lhs_target, lhs_text
        else:
            lhs_target, lhs_text = False, False
            return lhs_target, lhs_text

    def _pass_lock(self, obj):
        """bucket perm locks here."""
        has_perm = obj.check_permstring
        return has_perm("Admin)") or has_perm("BucketAdmin")

    def _set(self, setting, value):
        """sets options on the bucket"""
        if setting in VALID_BUCKET_SETTINGS.keys():
            self._setting_validate(setting, value)
        else:
            self.caller.msg(ERROR_PRE + "%s is not a valid setting for bucket %s" % ju.decorate(setting, self.bucket_name))

    def _set_timeout(self, setting, value):
        """timeout is a special thing.  Handle it seperately"""
        parts = value.split(" ")
        time = parts[0]
        ival = parts[1]
        if ival.lower() in VALID_TIMEOUT_INTERVALS:
            if time.isdigit():
               self.bucket.set(setting, int(time), interval=ival)
               self.caller.msg(SUCC_PRE + "Timeout for bucket %s set to: %s."
                               % ju.decorate(self.bucket_name, self.bucket.db.timeout_string))
            else:
               self.caller.msg(ERROR_PRE + "The timeout must be an integer")
        else:
            self.caller.msg(ERROR_PRE + "The interval must be 'hours', 'days', 'months', or 'years'.")

    def _setting_validate(self, setting, value):
        """ensures that only allowed settings get run"""
        if setting == "desc":
            if len(value)>45:
                self.bucket.set(setting, value)
                self.caller.msg(SUCC_PRE + "Bucket: %s description set to: %s" % ju.decorate(self.bucket_name, value))
            else:
                self.caller.msg(ERROR_PRE + "Bucket descriptions must be less than 45 characters.")
        elif setting == "timeout":
            self._set_timeout(setting, value)
        elif value.isdigit():
            self.bucket.set(setting, int(value))
            self.caller.msg(SUCC_PRE + "Bucket %s: %s set to %s" % ju.decorate(self.bucket_name, setting, value))
        else:
            self.caller.msg(ERROR_PRE + "%s setting must be an integer." % ju.decorate(setting))

    def switchparse(self):
        """switch workhorse, hard coding switches is probably bad, but it works right now
       Todo: Figure out if there's a way to cleanly handle sysop added functionality by calling modules
        """
        if self.switch and self._can_access(self.switch, self.caller):
            # create
            if self.switch == "create":
                if self.lhs_target and self.rhs:
                    self._create()
                else:
                    self.caller.msg(ERROR_PRE +
                                    "The syntax for the create command is +bucket/create <Bucket> = <Description>")
            # check
            elif self.switch == "check":
                if self.lhs:
                    self._check(self.character)
                else:
                    self.caller.msg(ERROR_PRE + "The syntax for the check command is +bucket/check <Character>")
            # access
            elif self.switch == "access":
                if self.lhs and self.rhs:
                    self._access(self.caller)
                else:
                    self.caller.msg(ERROR_PRE +
                                    "The syntax for the access command is +bucket/access <Bucket>/<action>=<Character>")
            # delete
            elif self.switch == "delete":
                if self.lhs:
                    self._delete()
                else:
                    self.caller.msg(ERROR_PRE + "The syntax for the delete command is +bucket/delete <Bucket>")
            # info
            elif self.switch == "info":
                if self.bucket_name:
                    self._info(self.bucket_name)
                else:
                    self.caller.msg(ERROR_PRE + "The syntax for the info command is +bucket/info <Bucket>")
            # monitor
            elif self.switch == "monitor":
                if self.bucket_name:
                    self._monitor(self.caller)
                else:
                    self.caller.msg(ERROR_PRE + "The syntax for the monitor command is +bucket/monitor <Bucket>")
            # rename
            elif self.switch == "rename":
                if self.rhs:
                    self._rename(self.rhs)
                else:
                    self.caller.msg(ERROR_PRE + "The syntax for the rename command is +bucket/rename <Bucket>=<value")
            # set
            elif self.switch == "set":
                if self.lhs and self.rhs:
                    self._set(self.lhs_text.lower(), self.rhs_text.lower())
                else:
                    self.caller.msg(ERROR_PRE +
                                    "The syntax for the set command is +bucket/set <Bucket>/<setting>=<value")
            else:
                self.caller.msg(ERROR_PRE + "That is not a valid bucket action. See +help buckets.")
        elif self.switch and not self._can_access(self.switch, self.caller):
            self.caller.msg(ERROR_PRE + "You may not access that action for Bucket: %s." % ju.decorate(self.bucket))
        else:
            self._bucket_table(self.buckets)

    def func(self):
        """this does the work of the +buckets command"""
        self.valid_actions = VALID_BUCKET_ACTIONS

        self.buckets = []
        for bucket in Bucket.objects.all():
            self.buckets.append(bucket)

        self._argparse()

        if self.switch in ("access", "check",):
            if self.lhs:
                if self._character_validate():
                    self.switchparse()
                else:
                    self.caller.msg(ERROR_PRE + "%s is not a valid character." % ju.decorate(self.character))
                    return
        else:
            self.switchparse()
