
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
_CORNER_TOP_LEFT_CHAR = settings._CORNER_TOP_LEFT_CHAR
_CORNER_TOP_RIGHT_CHAR = settings._CORNER_TOP_RIGHT_CHAR
_CORNER_BOTTOM_LEFT_CHAR = settings._CORNER_BOTTOM_LEFT_CHAR
_CORNER_BOTTOM_RIGHT_CHAR = settings._CORNER_BOTTOM_RIGHT_CHAR
_BORDER_LEFT_CHAR = settings._BORDER_LEFT_CHAR
_BORDER_RIGHT_CHAR = settings._BORDER_RIGHT_CHAR
_BORDER_TOP_CHAR = settings._BORDER_TOP_CHAR
_BORDER_BOTTOM_CHAR = settings._BORDER_BOTTOM_CHAR
_HEADER_BOTTOM_LEFT_CHAR = settings._HEADER_BOTTOM_LEFT_CHAR
_HEADER_BOTTOM_RIGHT_CHAR = settings._HEADER_BOTTOM_RIGHT_CHAR
_HEADER_LINE_CHAR = settings._HEADER_LINE_CHAR
_ERROR_PRE = settings._ERROR_PRE
_SUCC_PRE = settings._SUCC_PRE
_TEST_PRE = settings._TEST_PRE
_VALID_BUCKET_ACTIONS = settings._VALID_BUCKET_ACTIONS
_VALID_JOB_ACTIONS = settings._VALID_JOB_ACTIONS
_VALID_BUCKET_SETTINGS = settings._VALID_BUCKET_SETTINGS
_VALID_JOB_SETTINGS = settings._VALID_JOB_SETTINGS
_VALID_TIMEOUT_INTERVALS = settings._VALID_TIMEOUT_INTERVALS


class CmdJgroups(MuxCommand):
    """
    Usage:
        +jgroups/[switches]

        /info <jgroup>
        /create <jgroup>=<description>
        /delete <jgroup>
        /member <player>=<jgroup>


    Description:

        +jgroups    - aggregate lists of names to be able to do group (un)tagging,
                      (un)assigning, query,  and source commands
    """

    key = "jgroups"
    aliases = ["+jgroups"]
    lock = "cmd:perm(Admin)"
    help_category = "Jobs"

    def info(self, jgroup):
        pass

    def create(self, jgroup, description):
        pass

    def delete(self, jgroup):
        pass

    def member(self, player, jgroup):
        pass

    def func():
        """This does the work of the jgroups command"""
        pass


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
        action = self.lhs_text.lower()
        if not ju.ischaracter(self.character):
            self.caller.msg(_ERROR_PRE + "|w%s|n is not a valid character." % self.character)
        if self.bucket.has_access(action, self.character):
            self.bucket.remove_access(action, self.character)
            caller.msg(_SUCC_PRE + "Removing access to |w%s|n bucket action |w%s|n from |w%s|n"
                       % (self.bucket_name, action, self.character))
        elif action in self.valid_actions:
            self.bucket.grant_access(action, self.character)
            caller.msg(_SUCC_PRE + "Granting access to |w%s|n bucket action |w%s|n to %s."
                       % ( self.bucket_name, action, self.character))
        elif action is 'all':
            caller.msg(_SUCC_PRE + "Granting %s access to all bucket actions for %s %s"
                       % (self.character, self.bucket_name, self.valid_actions))
            self.bucket.grant_access(self.valid_actions, self.character)
        else:
            self.caller.msg(_ERROR_PRE + "|w%s|n is not a valid action for Bucket: |w%s|n" % (action, self.bucket_name))

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
            self.caller.msg(_ERROR_PRE + "Bucket: |w%s|n does not exist." % bucket)

    def _bucket_table(self, buckets):
        """creates and returns the populated table of bucket info"""
        ret = evtable.EvTable("Bucket", "Description", "# Jobs", "Pct", "C", "A", "D", "Due", "ARTS",
                              header=True,
                              border="table",
                              header_line_char=_HEADER_LINE_CHAR,
                              width=100,
                              corner_top_left_char=_CORNER_TOP_LEFT_CHAR,
                              corner_top_right_char=_CORNER_TOP_RIGHT_CHAR,
                              corner_bottom_left_char=_CORNER_BOTTOM_LEFT_CHAR,
                              corner_bottom_right_char=_CORNER_BOTTOM_RIGHT_CHAR,
                              border_left_char=_BORDER_LEFT_CHAR,
                              border_right_char=_BORDER_RIGHT_CHAR,
                              border_top_char=_BORDER_TOP_CHAR,
                              border_bottom_char=_BORDER_BOTTOM_CHAR)

        # layout the column widths
        ret.reformat_column(0, width=12, align="l")  # Bucket
        ret.reformat_column(1, width=45, align="l")  # Description
        ret.reformat_column(2, width=8, align="r")   # Number of Jobs
        ret.reformat_column(3, width=5, align="r")   # Percent completed
        ret.reformat_column(4, width=3, align="r")   # Completion Board
        ret.reformat_column(5, width=3, align="r")   # Approval Board
        ret.reformat_column(6, width=3, align="r")   # Denial Board
        ret.reformat_column(7, width=10, align="l")   # Due
        ret.reformat_column(8, width=10, align="r")   # Average Resolution Times

        # fix header corners
        ret.table[0][0].reformat(corner_bottom_left_char=_HEADER_BOTTOM_LEFT_CHAR)
        ret.table[8][0].reformat(corner_bottom_right_char=_HEADER_BOTTOM_RIGHT_CHAR)

        # populate the table.
        if isinstance(buckets, list):
            if self.switch:
                for bucket in buckets:
                    info = bucket.info()
                    ret.add_row(*info)
            else:
                for bucket in self.buckets:
                    if self.caller in bucket.db.per_player_actions or self._pass_lock(self.caller):
                        info = bucket.info()
                        ret.add_row(*info)
        else:
            info = buckets.info()
            ret.add_row(*info)
        self.caller.msg(ret)

    def _can_access(self, action, obj):
        """lock validation falls through to bucket.has_access(action, obj)"""
        locks = obj.locks.check_lockstring
        if self._pass_lock(obj) or (self.bucket is not None and self.bucket.has_access(action, obj)):
            return True
        else:
            return False

    def _check(self, obj):
        """displays bucket actions that an object has access to"""
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
                ret = _SUCC_PRE + "%s can not perform any actions on any bucket." % self.character
        else:
            ret = _ERROR_PRE + "You do not have administrator access to the bucket system."

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
                              corner_top_left_char=_CORNER_TOP_LEFT_CHAR,
                              corner_top_right_char=_CORNER_TOP_RIGHT_CHAR,
                              corner_bottom_left_char=_CORNER_BOTTOM_LEFT_CHAR,
                              corner_bottom_right_char=_CORNER_BOTTOM_RIGHT_CHAR,
                              border_left_char=_BORDER_LEFT_CHAR,
                              border_right_char=_BORDER_RIGHT_CHAR,
                              border_top_char=_BORDER_TOP_CHAR,
                              border_bottom_char=_BORDER_BOTTOM_CHAR,)
        # layout the column widths
        ret.reformat_column(0, width=40, align="l")   # Buckets target can access
        ret.reformat_column(1, width=55, align="c")   # Actions available to target
        # fix header corners
        ret.table[0][0].reformat(corner_bottom_left_char=_HEADER_BOTTOM_LEFT_CHAR)
        ret.table[1][0].reformat(corner_bottom_right_char=_HEADER_BOTTOM_RIGHT_CHAR)
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
        # Exists?
        if self.bucket:
            self.caller.msg(_ERROR_PRE + "Bucket: |w%s|n already exists." % self.bucket_name)
            return
        # Description?
        try:
            ev.create_channel(self.bucket_name, desc=self.rhs_text, typeclass="world.jobs.bucket.Bucket")
            self._assign_bucket(self.bucket_name)
            self.bucket.db.createdby = self.caller.key
            self.caller.msg(_SUCC_PRE + "Bucket: |w%s|n has been created." % self.bucket_name)
        except AttributeError:
            self.caller.msg(_ERROR_PRE + "A description must be provided for the bucket.")

    def _delete(self):
        """Deletes bucket.  Bucket may not have any jobs inside of bucket"""
        if self.bucket is not None:
            if not self.bucket.has_jobs():
                # Todo: check bucket for jobs first
                self.caller.msg(_SUCC_PRE + "Bucket: |w%s|n deleted." % self.bucket_name)
                ev.search_channel(self.bucket_name).first().delete()
            else:
                self.caller.msg(_ERROR_PRE + "Cannot delete Bucket: |w%s|n, jobs are associated with that bucket"
                           % self.bucket_name)
        else:
            self.caller.msg(_ERROR_PRE + "Bucket: |w%s|n does not exist." % self.bucket_name)
            return

    def _info(self, bucket):
        """Display info for particular bucket"""
        isbucket = ev.ChannelDB.objects.search_channel(bucket).first()
        if isbucket:
            self.caller.msg(self._bucket_table(isbucket))
        else:
            self.msg(_ERROR_PRE + "That is not a valid bucket.")

    def _rename(self, newname):
        """renames a particular bucket"""
        self.caller.msg(_SUCC_PRE + "Bucket: |w%s|n renamed to |w%s|n." % (self.bucket, newname))
        self.bucket.key = newname

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
        return has_perm("Admin)") or has_perm("BucketCreator")


    def _set(self, setting, value):
        if setting in _VALID_BUCKET_SETTINGS.keys():
            self._setting_validate(setting, value)
        else:
            self.caller.msg(_ERROR_PRE + "|w%s|n is not a valid setting for bucket |w%s|n" % (setting, self.bucket_name))

    def _set_timeout(self, setting, value):
        parts = value.split(" ")
        time = parts[0]
        ival = parts[1]
        if ival.lower() in _VALID_TIMEOUT_INTERVALS:
            if time.isdigit():
               self.bucket.set(setting, int(time), interval=ival)
               self.caller.msg(_SUCC_PRE + "Timeout for bucket |w%s|n set to: %s."
                               % (self.bucket_name, self.bucket.db.timeout_string))
            else:
               self.caller.msg(_ERROR_PRE + "The timeout must be an integer")
        else:
            self.caller.msg(_ERROR_PRE + "The interval must be 'hours', 'days', 'months', or 'years'.")

    def _setting_validate(self, setting, value):
        if setting == "desc":
            if len(value)>45:
                self.bucket.set(setting, value)
                self.caller.msg(_SUCC_PRE + "Bucket: |w%s|n description set to: %s" % (self.bucket_name, value))
            else:
                self.caller.msg(_ERROR_PRE + "Bucket descriptions must be less than 45 characters.")
        elif setting == "timeout":
            self._set_timeout(setting, value)
        elif setting.isdigit():
            self.bucket.set(setting, int(value))
        else:
            self.caller.msg(_ERROR_PRE + "|w%s|n setting must be an integer.")

    def func(self):
        """this does the work of the +buckets command"""
        self.valid_actions = _VALID_BUCKET_ACTIONS

        self.buckets = []
        for bucket in Bucket.objects.all():
            self.buckets.append(bucket)

        self._argparse()

        if self.switch in ("access", "check",):
            if self.lhs:
                if self._character_validate():
                    pass
                else:
                    self.caller.msg(_ERROR_PRE + "|w%s|n is not a valid character." % self.character)
                return
            else:
                pass
        else:
            pass

        # Each switch is its own function, parse and run if capable.
        if self.switch and self._can_access(self.switch, self.caller):
            if self.switch == "create":
                if self.lhs_target and self.rhs:
                    self._create()
                else:
                    self.caller.msg(_ERROR_PRE +
                                    "The syntax for the create command is +bucket/create <Bucket> = <Description>")
            elif self.switch == "check":
                if self.lhs:
                    self._check(self.character)
                else:
                    self.caller.msg(_ERROR_PRE + "The syntax for the check command is +bucket/check <Character>")
            elif self.switch == "access":
                if self.lhs and self.rhs:
                    self._access(self.caller)
                else:
                    self.caller.msg(_ERROR_PRE +
                                    "The syntax for the access command is +bucket/access <Bucket>/<action>=<Character>")
            elif self.switch == "delete":
                if self.lhs:
                    self._delete()
                else:
                    self.caller.msg(_ERROR_PRE + "The syntax for the delete command is +bucket/delete <Bucket>")
            elif self.switch == "info":
                if self.bucket_name:
                    self._info(self.bucket_name)
                else:
                    self.caller.msg(_ERROR_PRE + "The syntax for the info command is +bucket/info <Bucket>")
            elif self.switch == "rename":
                if self.rhs:
                    self._rename(self.rhs)
                else:
                    self.caller.msg(_ERROR_PRE + "The syntax for the rename command is +bucket/rename <Bucket>=<value")
            elif self.switch == "set":
                if self.lhs and self.rhs:
                    self._set(self.lhs_text.lower(), self.rhs_text.lower())
                else:
                    self.caller.msg(_ERROR_PRE +
                                    "The syntax for the set command is +bucket/set <Bucket>/<setting>=<value")
            else:
                self.caller.msg(_ERROR_PRE + "That is not a valid bucket action. See +help buckets.")
        elif self.switch and not self._can_access(self.switch, self.caller):
            self.caller.msg(_ERROR_PRE + "You may not access that action for Bucket: |w%s|n." % self.bucket)
        else:
            self.caller.msg(self._bucket_table(self.buckets))


class CmdJobs(MuxCommand):
    """
    Jobs v0.1

    Usage:
        +jobs <#>
        +jobs/<switches> [#]

    ___________________________________________________________________________

    Switches:
    ___________________________________________________________________________

        /<all|mine|new>                     : List all/yours/new jobs
        /catchup                            : Clears new jobs
        /clean                              : Remove non-players from job data
        /credits                            : Display credit information
        /list <bucket>                      : List all jobs in <bucket>
        /overdue                            : List overdue jobs
        /reports [<report>]                 : Get a report
        /search <pattern>                   : Search jobs for <pattern>
        /select <expression>                : List jobs matching <expression>
        /<sort|date|pri>                    : Lists jobs by bucket/mod/pri
        /who <player>                       : Lists jobs assigned to player
        /act <#>                            : Display actions on a job
        /add <#>=<comments>                 : Add comments to a job
        /all <#>                            : Displays all comments in a job
        /approve <#>=<comment>              : Approve a player request
        /assign <#>=<<player>|none>         : Assign a job to player
        /checkin <#>                        : Checks in a job
        /checkout <#>                       : Checks out a job
        /claim <#>                          : Assign a job to yourself
        /clone <#>                          : Clones a job
        /complete <#>=<comment>             : Complete a job
        /create <bucket>/<title>=<comments> : Create a job manually
        /deny <#>=<comment>                 : Deny a player request
        /due <#>=<<date>|none>              : Set job due date
        /edit <#>/< from decemberntry#>=<old>/<new>      : Edits a job
        /esc <#>=<green|yellow|red>         : Escalate a job's priority
        /help <#>                           : Display help for a job's bucket
        /last <#>=<X>                       : List last <X> entries in <#>
        /lock <#>                           : Locks a job and prevents changes
        /log <#>                            : Logs a job
        /mail <#>=<message>                 : Mails opener with <message>
        /merge <source>=<destination>       : Merge <source> into <destination>
        /rename <#>=<name>                  : Rename a job
        /publish <#>=<comment>              : Publishes a job or <comment>
        /query <players>/<title>=<query>    : Sends a query to <players>
        /set <#>=<status>                   : Set progress status on a job
        /source <#>=<player list>           : Changes opened-by to <player list>
        /summary <#>                        : Views a job's header & SUMMARY
        /sumset <#>/<set>=<value>           : Changes a job SUMMARY setting
        /tag <#>                            : Tags a job for you
        /tag <#>=<player>                   : Tags a job for <player>
        /trans <#>=<bucket>                 : Transfer (or undelete) a job
        /unlock <#>                         : Unlocks a job
        /untag <#>                          : Untags a job
        /untag <#>=<player list>            : Untags a job for <player list>
        /delete <#>                         : Delete a job (Wiz)
        /compress                           : Compresses job list (Wiz)
    """

    key = "jobs"
    aliases = ["+jobs", "+job", "job"]
    lock = "cmd:perm(Admin)"
    help_category = "Jobs"

    def _action_handler(self, switch, *args):
        # This handles the switches
        # I need to take the switch and run it as a function

        # Switches are set up as function calls.  No switch, no
        # execution.
        method_name = '_' + str(switch)
        possibles = globals.copy()
        possibles.update(locals())
        method = possibles.get(method_name)

        if args:
            output = method()

        if not method:
            output = "%s is not a valid switch for the +job system" % switch


        def _joblist(self, *args, **kwargs):
            """List all/yours/new jobs"""
            pass

        def _catchup(self):
            """Clears new jobs"""
            pass

        def _clean(self):
            """Remove non-players from job data"""
            pass

        def _credits(self):
            """Display credit information"""
            pass

        def _list(self, bucket):
            """List all jobs in <bucket>"""
            pass

        def _overdue(self):
            """List overdue jobs"""
            pass

        def _reports(self, report=None):
            """Get a report"""
            pass

        def _search(self, pattern):
            """Search jobs for <pattern>"""
            pass

        def _select(self, expression):
            """List jobs matching <expression>"""
            pass

        def _sort(self, sorttype):
            """Lists jobs by bucket/mod/pri"""
            pass

        def _who(self, jobid):
            """Lists jobs assigned to player"""
            pass

        def _act(self, jobid):
            """Display actions on a job"""
            pass

        def _add(self, jobid, comment):
            """Add comments to a job"""
            pass

        def _all(self, jobid):
            """Displays all comments in a job"""
            pass

        def _approve(self, jobid, comment):
            """Approve a player request"""
            pass

        def _assign(self, jobid, player=None):
            """Assign a job to player"""
            pass

        def _checkin(self, jobid):
            """Checks in a job"""
            pass

        def _checkout(self, jobid):
            """Checks out a job"""
            pass

        def _claim(self, jobid):
            """Assign a job to yourself"""
            pass

        def _clone(self, jobid):
            """Clones a job"""
            pass

        def _complete(self, jobid, comment):
            """Complete a job"""
            pass

        def _create(self, bucket, title, comment):
            """Create a job manually"""
            pass

        def _deny(self, jobid, comment):
            """Deny a player request"""
            pass

        def _due(self, jobid, date=None):
            """Set job due date"""
            pass

        def _edit(self, jobid, entryid, old, new):
            """Edits a job"""
            pass

        def _esc(self, jobid, priority):
            """Escalate a job's priority"""
            pass

        def _help(self, jobid):
            """Display help for a job's bucket"""
            pass

        def _last(self, jobid, num):
            """List last num entries in jobid"""
            pass

        def _lock_job(self, jobid):
            """Locks a job and prevents changes"""
            pass

        def _log(self, jobid):
            """Logs a job"""
            pass

        def _mail(self, jobid, message):
            """Mails opener with <message>"""
            pass


        def _merge(self, source, destination):
            """Merge <source> into <destination>"""
            pass

        def _rename(self, jobid, name):
            """Rename a job"""
            pass

        def _publish(self, jobid, comment):
            """Publishes a job or <comment>"""
            pass

        def _query(self, player_list, title, query):
            """Sends a query to <players>"""
            pass

        def _set(self, jobid, status):
            """Set progress status on a job"""
            pass

        def _source(self, jobid, player_list):
            """Changes opened-by to <player list>"""
            pass

        def _summary(self, jobid):
            """Views a job's header & SUMMARY"""
            pass

        def _sumset(self, jobid, sumset, value):
            """Changes a job SUMMARY setting"""
            pass

        def _tag(self, jobid):
            """Tags a job for you"""
            pass

        def _player_tag(self, jobid, player):
            """Tags a job for <player>"""
            pass

        def _trans(self, jobid, bucket):
            """Transfer (or undelete) a job"""
            pass

        def _unlock(self, jobid):
            """Unlocks a job"""
            pass

        def _untag(self, jobid):
            """Untags a job"""
            pass

        def _list_untag(self, jobid, player_list):
            """Untags a job for <player list>"""
            pass

        def _delete(self, jobid):
            """Delete a job (Wiz)"""
            pass

        def _compress(self):
            """Compresses job list (Wiz)"""
            pass

        return output


    def func(self):
        """This does the work of the jobs command"""
        # I want to display the list of buckets available if no switches or arguments
        # have been given.  If a switch has been given, process it and call the appropriate
        # method.  if no switches have been given but args have been given this is a bucket
        # request -- it should display the bucket that is passed.  If it's not a bucket it should
        # return an error message.

        self.valid_actions = _VALID_JOB_ACTIONS

        if self.switches or self.args:
            if self.switches:
                # parse and process switches
                output = _action_handler(self.switches[0])
                return output

            elif self.args:
                # This handles @job # - it should display a list of jobs in the bucket. The
                # arg should match a bucket name or bucket id.
                pass

            pass
        else:
            # +job(s) This part should just display the list of available buckets.
            pass

