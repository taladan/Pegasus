

from evennia import default_cmds
from jobutils import Utils


MuxCommand = default_cmds.MuxCommand
argparse = Utils.argparse


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

        def _catchup(self):
            """Clears new jobs"""
            pass

        def _checkin(self, jobid):
            """Checks in a job"""
            pass

        def _clean(self):
            """Remove non-players from job data"""
            pass

        def _credits(self):
            """Display credit information"""
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

        def _compress(self):
            """Compresses job list (Wiz)"""
            pass

        def _create(self, bucket, title, text):
            """Create a job manually"""
            ev.create_channel(self.job_name, desc=text, typeclass="world.jobs.Job",
                              bucket=bucket, creator=self.caller, title=title, text=text)

        def _delete(self, jobid):
            """Delete a job (Wiz)"""
            # archive the job
            # remove it from the bucket association
            pass

        def _deny(self, jobid, comment):
            """Deny a player request"""
            # move the job to the denied stack
            # mail the player
            # post the board
            pass

        def _due(self, jobid, date=None):
            """Set job due date"""
            # override default due date with new date
            pass

        def _edit(self, jobid, entryid, old, new):
            """Edits a job"""
            # search and replace the old text with the new
            pass

        def _esc(self, jobid, priority):
            """Escalate a job's priority"""
            # replace job priority
            pass

        def _joblist(self, *args, **kwargs):
            """List all/yours/new jobs"""
            pass

        def _last(self, jobid, num):
            """List last num entries in jobid"""
            pass

        def _list_untag(self, jobid, player_list):
            """Untags a job for <player list>"""
            pass

        def _list(self, bucket):
            """List all jobs in <bucket>"""
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

        def _overdue(self):
            """List overdue jobs"""
            pass

        def _player_tag(self, jobid, player):
            """Tags a job for <player>"""
            pass

        def _publish(self, jobid, comment):
            """Publishes a job or <comment>"""
            pass

        def _query(self, player_list, title, query):
            """Sends a query to <players>"""
            pass

        def _rename(self, jobid, name):
            """Rename a job"""
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

        def _set(self, jobid, status):
            """Set progress status on a job"""
            pass

        def _sort(self, sorttype):
            """Lists jobs by bucket/mod/pri"""
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

        def _trans(self, jobid, bucket):
            """Transfer (or undelete) a job"""
            pass

        def _unlock(self, jobid):
            """Unlocks a job"""
            pass

        def _untag(self, jobid):
            """Untags a job"""
            pass

        def _who(self, jobid):
            """Lists jobs assigned to player"""
            pass

    def _switch_handler(self):
        """This handles the switches and arguments assignments"""
        # parse up args
        passargs = argparse(self.lhs, self.rhs)
        if passargs is not None:
            self.lhs_obj, self.lhs_act, self.rhs_obj, self.rhs_act = passargs
        else:
            self.lhs_obj = self.lhs_act = self.rhs_obj = self.rhs_act = False

        if self.switches or self.args:
            if self.switches:
                # parse and process switches
                output = _action_handler(self.switches[0])
                return output
            elif self.args:
                pass
        # This handles @job # - it should display a list of jobs in the bucket. The
        # arg should match a bucket name or bucket id.
        else:
            # +job(s) This part should just display the list of available buckets.
            pass

    def func(self):
        """This does the work of the jobs command"""


        self._switch_handler()

        self.valid_actions = self.job.valid_actions


        """
        RHS commands:
        
            These commands require processing of lhs '/' and rhs '/', self.lhs, and self.rhs
                +job/edit <#>/<#>=<old>/<new>           : Edits a job
            
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
                +job/list <bucket>                      : List all jobs in <bucket>
                +job/reports [<report>]                 : Get a report
                +job/search <pattern>                   : Search jobs for <pattern>
                +job/select <expression>                : List jobs matching <expression>
                +job/who <player>                       : Lists jobs assigned to player
                +job/act <#>                            : Display actions on a job
                +job/all <#>                            : Displays all comments in a job
                +job/checkin <#>                        : Checks in a job
                +job/checkout <#>                       : Checks out a job
                +job/claim <#>                          : Assign a job to yourself
                +job/clone <#>                          : Clones a job
                +job/help <#>                           : Display help for a job's bucket
                +job/lock <#>                           : Locks a job and prevents changes
                +job/log <#>                            : Logs a job
                +job/summary <#>                        : Views a job's header & SUMMARY
                +job/tag <#>                            : Tags a job for you
                +job/unlock <#>                         : Unlocks a job
                +job/untag <#>                          : Untags a job
                +job/delete <#>                         : Delete a job (Wiz)
            
            These commands take no arguments
                
                +job/<all|mine|new>                 : List all/yours/new jobs
                +job/catchup                        : Clears new jobs
                +job/clean                          : Remove non-players from job data
                +job/credits                        : Display credit information
                +job/overdue                        : List overdue jobs
                +job/<sort|date|pri>                : Lists jobs by bucket/mod/pri
                +job/compress                       : Compresses job list (Wiz)
        """
