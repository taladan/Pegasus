

import hashlib
import random
from datetime import datetime as date
import evennia as ev
from evennia import default_cmds
from evennia.utils import evtable
from jobutils import Utils
from jobs_settings import VALID_JOB_ACTIONS
from jobs_settings import SUCC_PRE
from jobs_settings import ERROR_PRE
from jobs_settings import SORT_DIRECTION
from jobs_settings import SORT_METHOD
from jobs_settings import VALID_SORT_METHODS

ju = Utils()
MuxCommand = default_cmds.MuxCommand
"""
argless_actions = ("all", "catchup", "clean", "compress", "credits", "mine", "new", "overdue", "sort")
lhs_only_actions = ("act", "all", "checkin", "checkout", "claim", "clone", "delete", "help", "list",
                    "lock", "log", "reports", "search", "select", "summary", "tag", "unlock", "untag", "who")
rhs_lhs_actions = ("add", "approve", "assign", "complete", "create", "deny", "due", "edit", "esc", "last",
                   "mail", "merge", "publish", "query", "rename", "set", "source", "sumset", "tag",
                   "trans", "untag")

self.switch = self.switches[0]
if self.switch in argless_actions:
    pass
elif self.switch in lhs_only_actions:
    pass
elif self.switch in rhs_lhs_actions:
    pass
else:
    self.caller.msg(ERROR_PRE + "|w%s|n is not a valid switch for the +jobs command." % self.switch)

RHS commands:

    These commands require processing of lhs '/' and rhs '/', self.lhs, and self.rhs
    
        +job/edit <#>/<entry #>=<old>/<new>     : Edits a job
    
    These commands require processing of lhs '/', self.lhs, and self.rhs
    
        +job/sumset <#>/<set>=<value>           : Changes a job SUMMARY setting
        +job/query <players>/<title>=<query>    : Sends a query to <players>
        +job/create <bucket>/<title>=<comments> : Create a job manually
    
    These commands require processing of self.lhs and self.rhs
    
        +job/add <#>=<comments>                 : Add comments to a job
        +job/approve <#>=<comment>              : Approve a player request
        +job/assign <#>=<<player>|none>         : Assign a job to player
        +job/complete <#>=<comment>             : Complete a job
        +job/deny <#>=<comment>                 : Deny a player request
        +job/due <#>=<<date>|none>              : Set job due date
        +job/esc <#>=<green|yellow|red>         : Escalate a job's priority
        +job/last <#>=<X>                       : List last <X> entries in <#>
        +job/mail <#>=<message>                 : Mails opener with <message>
        +job/merge <source>=<destination>       : Merge <source> into <destination>
        +job/rename <#>=<name>                  : Rename a job
        +job/publish <#>=<comment>              : Publishes a job or <comment>
        +job/set <#>=<status>                   : Set progress status on a job
        +job/source <#>=<player list>           : Changes opened-by to <player list>
        +job/tag <#>=<player>                   : Tags a job for <player>
        +job/trans <#>=<bucket>                 : Transfer (or undelete) a job
        +job/untag <#>=<player list>            : Untags a job for <player list>
        
    
LHS commands:
    If it's lhs only, there is no need for processing additional / arguments.
            "       , there is no need to process rhs arguments
            "       , the target can be either a bucket type, report type, pattern, expression, 
                      jobid or other, so self.lhs will always be the target for these commands.
                      
    These commands take an argument
    
        +job/act <#>                            : Display actions on a job
        +job/all <#>                            : Displays all comments in a job
        +job/checkin <#>                        : Checks in a job
        +job/checkout <#>                       : Checks out a job
        +job/claim <#>                          : Assign a job to yourself
        +job/clone <#>                          : Clones a job
        +job/delete <#>                         : Delete a job (Wiz)
        +job/help <#>                           : Display help for a job's bucket
        +job/list <bucket>                      : List all jobs in <bucket>
        +job/lock <#>                           : Locks a job and prevents changes
        +job/log <#>                            : Logs a job
        +job/reports [<report>]                 : Get a report
        +job/search <pattern>                   : Search jobs for <pattern>
        +job/select <expression>                : List jobs matching <expression>
        +job/summary <#>                        : Views a job's header & SUMMARY
        +job/tag <#>                            : Tags a job for you
        +job/unlock <#>                         : Unlocks a job
        +job/untag <#>                          : Untags a job
        +job/who <player>                       : Lists jobs assigned to player
    
    These commands take no arguments
        
        +job/<all|mine|new>                 : List all/yours/new jobs
        +job/catchup                        : Clears new jobs
        +job/clean                          : Remove non-players from job data
        +job/credits                        : Display credit information
        +job/overdue                        : List overdue jobs
        +job/<sort|date|pri>                : Lists jobs by bucket/mod/pri
        +job/compress                       : Compresses job list (Wiz)
"""


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


# decorator
    class actupdate(object):
        """decorator class to update actions on a job automatically

        This decorator takes the returned output from specific commands and
        appends the actioncode (act) along with the caller, the exit status,
        and the message passed and appends a formatted header and body to the
        job's actions list.  It will return the output of the function on
        to the outter part of the system.


        :return:  returns the value of the output of the function wrapped
        """
        # Todo: testing of decorator
        def __init__(self, f):
            self.f = f

        def __call__(self, f):
            """ takes function as a parameter, decorates and returns wrapped function"""
            # Always start from 0
            actid = len(actlist) + 1 if len(actlist) < 0 else len(actlist)
            time = '%s' % date.today().strftime("%B %d, %Y at %H:%M")
            output = function()
            act = output.get("act")
            actlist = output.get("actlist")
            caller = output.get("caller")
            msg = output.get("msg")
            actheader = (time, act, caller, msg[0:40])
            actlist.append(actid + ":" + actheader)

    # switches go here
    def _act(self):
      """
      Displays a summary of actions that have been peformed on a job.
        +job/act <#>
      :param self:
      :return: job action summary or error
      """
      ret = {}
      ret[msg] = {"act": act, "caller": self.caller, "stat": exit_status, "msg": msg}
      return ret

    def _all(self):
        """
        +job/all
        +job/all <#>
        Displays all comments in a job
        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _approve(self):
        """
        job/approve <#>=<comment>
        Approves a job with a comment.
        :param self:
        :param jobid:
        :param comment:
        :return:
        """
        ret = {}
        job = self.job
        msg = self.rhs
        title = self.job.db.title,
        creator = self.job.db.createdby
        header = "Your job %s has been approved by %s." % ju.decorate(title, self.caller)
        self._mail(creator, header, body)
        # package message for decorator
        act = "apr"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _assign(self):
        """
        job/assign <#>=<<player>|none>
        Assign a job to player
        :param self:
        :param jobid:
        :param player:
        :return:
        """
        ret = {}
        act = "asn"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _catchup(self):
        """
        job/catchup
        Clears new jobs

        :param self:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _clean(self):
        """ job/checkout <#>
        Remove non-players from job data

        :param self:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _checkin(self):
        """
        job/checkin <#>
        Checks in a job

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        act = "cki"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _checkout(self):
        """
        +job/checkout <#>

        Allows a user to checkout a job and lock it against changes for the duration that it is checked out.
        """
        ret = {}
        act = "cko"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _claim(self):
        """
        job/claim <#>
        Allows a user to claim a job, assigning it to that user.

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        act = "asn"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _clone(self):
        """
        job/clone <#>
        Clones a job

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        act = "cln"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _complete(self):
        """
        job/complete <#>=<comment>
        Completes a job with comment
        """
        ret = {}
        act = "com"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
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
        bucket, title, msgtext = args

        if ju.isbucket(bucket):

            if args:

                # Job Creation
                jhash = '%s %s %s %s' % (bucket, title, date.today().strftime(), str(random.randrange(1,1000000)))
                jid = hashlib.md5(jhash.encode(utf-8)).hexdigest()
                self.job = ev.create_channel(jid, desc=title, typeclass="world.jobs.job.Job")
                self.job.tags.add(bucket, category="jobs")
                self.job.tags.add(job, category="jobs")
                self._add_msg(jid=jid, bucket=bucket, title=title, msgtext=msgtext, action="create", parent=jid)
                ret = SUCC_PRE + "Job: %s created." % ju.decorate(title)

            # No args
            else:
                sysmsg = ERROR_PRE + "The correct syntax is +job/create Bucket/Title=Text"
        # No bucket
        else:
            sysmsg = ERROR_PRE + "%s is an invalid bucket." % ju.decorate(bucket)

        ret = {}
        act = "cre"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _credits(self):
        """
        job/credits
        Display credits information

        :param self:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _delete(self, jobid):
        """
        job/delete <#>
        deletes a job

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        act = "del"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _deny(self, jobid, comment):
        """
        job/deny <#>=<comment>
        Denies a job with comment

        :param self:
        :param jobid:
        :param comment:
        :return:
        """
        ret = {}
        act = "dny"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _due(self, jobid, date=None):
        """
        job/due <#>=<<date>|none>
        Sets a due date on a job
        """
        ret = {}
        act = "due"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
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
        ret = {}
        act = "edt"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _esc(self, jobid, priority):
        """
        job/esc <#>=<green|yellow|red>
        Sets the priority of a job

        :param self:
        :param jobid:
        :param priority:
        :return:
        """
        ret = {}
        act = "sta"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def get_sortby(self, character):
        """
        Retrieves jsort attribute from a character (if it exists) and returns the method
        and sorting direction.  If the attribute does not exist, it returns the default
        sortby method and direction.

        :param character: the object db.jsort is pulled from
        :return: (method, direction)
        """
        # Todo: fix return
        sort = character.db.jsort
        if sort:
            method, direction = sort.split(':')
            return (method, direction)
        else:
            ret = (SORT_METHOD, SORT_DIRECTION)
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _help(self, jobid):
        """
        job/help <#>
        Displays help for a job's bucket.
        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
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
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _last(self, jobid, num):
        """
        job/last <#>=<x>
        this shows the last x entries on a job

        :param self:
        :param jobid:
        :param num:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

        """
        job/untag <#>=<player list>
        untags a list of players from a job
        """
        return ret

    def _list(self, bucket):
        """
        job/list <bucket>
        displays the list of jobs in bucket.

        :param self:
        :param bucket:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _lock_job(self, jobid):
        """
        job/lock <#>
        locks a job from any further modification

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        act = "lok"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _log(self, jobid):
        """
        job/log <#>
        Logs a particular job - want to add email functionality to this.

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        act = "log"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _mail(self, creator, header, body):
        """
        job/mail <#>=<message>
        Sends mail to the jobs source(s)

        :param self:
        :param jobid:
        :param message:
        :return:
        """
        ret = {}
        act = "mai"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _merge(self, source, destination):
        """
        job/merge <source>=<destination>
        Merges one job (source) into another (destination)

        :param self:
        :param source:
        :param destination:
        :return:
        """
        ret = {}
        act = "mrg"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _overdue(self):
        """
        job/overdue
        Displays only a list of overdue jobs

        :param self:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _pri(self):
        """
        +job/pri
        Sorts job by priority in descending order

        :param self:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
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
        ret = {}
        act = "pub"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
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
        ret = {}
        act = "qry"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _rename(self, jobid, name):
        """
        +job/rename <#>=<name>
        Rename a job

        :param self:
        :param jobid:
        :param name:
        :return:
        """
        ret = {}
        act = "nam"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _reports(self, report=None):
        """
        +job/reports [<report>]
        Get a report

        :param self:
        :param report:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _search(self, pattern):
        """
        +job/search <pattern>
        Search jobs for <pattern>

        :param self:
        :param pattern:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _select(self, expression):
        """
        +job/select <expression>
        List jobs matching <expression>

        :param self:
        :param expression:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _set(self, jobid, status):
        """
        +job/set <#>=<status>
        Set progress status on a job

        :param self:
        :param jobid:
        :param status:
        :return:
        """
        ret = {}
        act = "sta"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _sortby(self):
        """
        +job/sortby [Alpha|Date|Priority][/][asc|des]
        Without arguments, this displays the character's current
        sortby method for displaying jobs (+jobs/all, +jobs/mine, +jobs/new)

        Alpha    - Sorts alphabetically by bucket
        Date     - Sorts by date due
        Priorty  - Sorts by priorty

            /asc - sorts ascending
            /des - sorts descending (default)

        :param self:
        :param sorttype:
        :return:
        """
        # Todo: fix ret
        # Sortby and Direction
        if self.lhs_obj and self.lhs_act:
            sortby = self.lhs_obj
            direction = self.lhs_act
            sortby = sortby.lower()
            direction = direction.lower()

            if sortby in VALID_SORT_METHODS and direction in ("asc", "des"):
                self.caller.db.jsort=sortby + ":" + direction
                ret = SUCC_PRE + "Sortby method set to %s, %s" % (ju.decorate(sortby), 'descending' if direction == 'des' else 'ascending')
            else:
                ret = ERROR_PRE + "Method must be one of: %s Direction must be 'asc' or 'des' or left blank." % ju.decorate(VALID_SORT_METHODS)
        # Sortby only
        elif self.lhs:
            sortby = self.lhs_obj
            sortby = sortby.lower()
            if sortby in VALID_SORT_METHODS:
                self.caller.db.jsort=sortby + ":" + "des"
                ret = SUCC_PRE + "Sortby method set to %s, descending" % sortby
        else:
            ret = self.get_sortby(self.caller)
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _source(self, jobid, player_list):
        """
        +job/source <#>=<player list>
        Changes opened-by to <player list>

        :param self:
        :param jobid:
        :param player_list:
        :return:
        """
        ret = {}
        act = "src"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _summary(self, jobid):
        """
        +job/summary <#>
        Views a job's header & SUMMARY

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
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
        ret = {}
        act = "sum"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _tag(self, jobid):
        """
        +job/tag <#>
        Tags a job for you

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        act = "tag"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _trans(self, jobid, bucket):
        """
        +job/trans <#>=<bucket>
        Transfer (or undelete) a job

        :param self:
        :param jobid:
        :param bucket:
        :return:
        """
        ret = {}
        act = "trn"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _unlock(self, jobid):
        """
        +job/unlock <#>
        Unlocks a job

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        act = "lok"
        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    @actupdate
    def _untag(self):
        """
        +job/untag <#>=<player>
        Untags a job

        :param self:
        :param jobid:
        :return:
        """
        charname = self.rhs
        job = self.jobid
        if ju.ischaracter(charname):
            ret = {}
            act = "tag"
            character = ev.ObjectDB.objects.search(charname)
            character.tags.remove(job, category="jobs")
            msg = "%s untagged %s from job %s" % (self.caller, charname, job)
            exit_status = SUCC_PRE
        else:
            act = False
            exit_status = ERROR_PRE
            msg = ERROR_PRE + "%s is not a valid character." % charname

        ret[msg] = {"act": act, "actlist": self.job.db.actions_list, "caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    def _who(self, jobid):
        """
        +job/who <player>
        Lists jobs assigned to player

        :param self:
        :param jobid:
        :return:
        """
        ret = {}
        ret[msg] = {"caller": self.caller, "stat": exit_status, "msg": msg}
        return ret

    # Executes when command is run
    def func(self):
        """This does the work of the jobs command"""
        self.valid_actions = VALID_JOB_ACTIONS
        self.jobs_list = self.all_jobs()

        # No switch, no args
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
        # +job(s) This part should just display the list of available buckets.
        else:
            self.caller.msg(self.table())
        """
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

    # Utility Functions
    def _action_handler(self, switch, *args):
        """
        The action handler munges up the switch and then runs it.
        The switches are function calls.  It should also parse
        through the args and assign them correctly.
        """

        # set the method we're going to call against
        method_name = '_' + str(switch)
        method = getattr(self, method_name)

        if args:
            self.job_number = self._set_job_number(self.switch)
            if self.job_number:
                self.job = self.set_job(self.job_number)
                if not self.job:
                    ret = "%s is not a valid job number" % self.job_number
            else:
                # Todo: non-id specific job tasks
                pass
        if not method:
            ret = "%s is not a valid switch for the +job system" % method_name
        else:
            ret = method()

        self.caller.msg(ret)

    def all_jobs(self):
        """
       Returns a queryset of jobs the character has access to.

        :return: queryset of jobs
        """
        try:
            character = self.caller.character
        except AttributeError:
            character = self.caller
        jobs = ev.Msg.objects.get_by_tag(category="jobs").filter(db_receivers_objects=character)
        return jobs

    def _add_msg(self, *kwargs):
        """
        Adds a message to a particular job

            _add_msg(jid="", bucket="", title="", msgtext="", action="", parent="")

        :param kwargs: Required kwargs: jid, bucket, title, msgtext, action, parent
        :return: the message object or false
        """
        try:
            jid = kwargs.pop("jid")
            bucket = kwargs.pop("bucket")
            title = kwargs.pop("title")
            msgtext = kwargs.pop("msgtext")
            action = kwargs.pop("action")
            parent= kwargs.pop("parent")

            msgheader = '%s, %s, %s, %s' % (self.caller, date.today().strftime("%B %d, %Y"), title,)
            msghash = '%s %s %s %s' % (self.caller, date.now(), title, str(random.randrange(1,1000000)))
            msgid = haslib.md5(msghash.encode(utf-8)).hexdigest()
            msg = ev.create_message(self.caller, msgtext, channels=bucket, header=msgheader, recievers=self.job.db.recievers)

            msg.tags.add("job:"+jid, category="jobs")
            msg.tags.add("msg", category="jobs")
            msg.tags.add("msgid:"+msgid, category="jobs")
            msg.tags.add("bucket:"+bucket, category="jobs")
            msg.tags.add("act:"+action, category="jobs")
            msg.tags.add("reply:"+parent, category="jobs")
            msg.tags.add("u", category="jobs")
            ret = msg
        except KeyError:
            ret = False
        return ret

    def _assign_job(self):
        """sets self.job if it exists in the db"""
        try:
            self.job = ev.ChannelDB.objects.get_channel(self.title)
        except AttributeError:
            self.caller.msg(ERROR_PRE + "Job: %s does not exist." % ju.decorate(self.title))

    def _set_job_number(self, switch):
        """
       Parses the switch for jobs needing to be called by id and assigns the appropriate value

        :param switch:
        :return: job number or false
        """
        lhs_id_required = ("act", "all", "checkin", "checkout", "claim", "clone", "delete", "list_untag",
                           "lock_job", "log", "summary", "tag", "unlock", "untag")
        rhs_id_required = ("add", "approve", "assign", "complete", "deny", "due",  "esc", "last", "list_untag",
                           "mail", "player_tag", "publish", "rename", "set", "source", "tag", "trans", "untag")

        if switch == "edit" or self.switch == "sumset":
            ret = self.lhs_obj
        elif switch in rhs_id_required:
            ret = self.lhs
        elif switch in lhs_id_required:
            ret = self.lhs
        else:
            ret =False
        return ret

    def set_job(self, number):
        """gets and returns the correct job"""
        jobs_max = max(0, self.jobs_list.count() - 1)
        try:
            i = max(0, min(jobs_max, int(number) - 1))
            ret = self.jobs_list[i]
        except ValueError, IndexError:
            ret = False

        return ret

    class default_table(object):
        def __init__(self):
            from job import Job
            self.head = "Job", "Type", "Title", "Opened By", "Due on", "Assigned to"
            self.jobs = Job.objects.all()

            """
            ######What are the steps to getting a job?
            
            * get list of all jobs
            * 
            * Caller must have access to a particular job
            * 
            """
            # self.body =


    def table(self, head=False, body=False, layout=False):
        """
        Builds a table with header from data
        :param header: tuple(string1, string2, ... )
        :param data: iterable
        :return: formatted table
        """
        # Todo: Finish building table

        dt = self.default_table()
        # Create the table
        if head:
            pass
        else:
            head = dt.head

        if body:
            pass
        else:
            from job import Job
            jobs = Job.objects.all()
            # Todo: munge jobs to test for access
            body = jobs

        # Create the table
        table = evtable.EvTable()

        # Add columns
        for i in head:
            table.add_column(i)

        # Add rows
        for i in body:
            info = job.info()
            table.addrow(*info)

        if layout:
            pass
        else:
            import jobs_settings as jset
            table.header = True
            table.border = "table"
            table.header_line_char = jset.HEADER_LINE_CHAR
            table.width = jset.TABLE_WIDTH
            table.corner_top_left_char = jset.CORNER_TOP_LEFT_CHAR
            table.corner_top_right_char = jset.CORNER_TOP_RIGHT_CHAR
            table.corner_bottom_left_char = jset.CORNER_BOTTOM_LEFT_CHAR
            table.corner_bottom_right_char = jset.CORNER_BOTTOM_RIGHT_CHAR
            table.border_left_char = jset.BORDER_LEFT_CHAR
            table.border_right_char = jset.BORDER_RIGHT_CHAR
            table.border_top_char = jset.BORDER_TOP_CHAR
            table. border_bottom_char = jset.BORDER_BOTTOM_CHAR

        return table


