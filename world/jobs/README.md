# Bucket

Bucket Creation Mockup
---

```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs System.........1 .......Bucket Creation.....2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Name                           A    6. Grant Access                  F  ║
║  2. Description                    B    7. Options Submenu               G  ║
║  3. Approval Board                 C    8. Finalize Creation             H  ║
║  4. Denial Board                   D                                        ║
║  5. Completion Board               E                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ..Help is available.................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

#### Menu Variables
1. System
2. Menu Title
3. Gamename
4. Menu_text

|Menu Variable|DB Variable                              |
|-------------|-----------------------------------------|
|System       |`evennia.world.jobs.jobs_defaults.SYSTEM`|
|Menu Title   |self.menu_title                          | 
|Menu Text    |self.menu_text                           |

#### Creation menu choices:<sup1</sup

A. Name ~: if bucket doesn't exist: if name isn't too long: dbsave else: reprompt too long else: reprompt exists
B. Description ~: if desc exists, if it is too long: trunc and dbsave, else dbsave, else error
C. Approval board ~: if board exists and bucket can post, dbsave
D. Denial Board ~:  if board exists and bucket can post, dbsave
E. Completion Board ~: if board exists and bucket can post, dbsave
F. Grant Access ~: if player exists and doesn't have access, dbsave
G. Set options ~: submenu
H. Finalize Creation ~: Test Bucket.db.key, db.desc, db.approval, db.denial, db.completion are set then create bucket and write to bucket (Bucket.flush())


|Choice | DB Attr                |
|-------|------------------------|
|access | `ndb._menutree.access` |
|admin  | `ndb._menutree.admin`  |
|app    | `ndb._menutree.app`    |
|comp   | `ndb._menutree.comp`   |
|deny   | `ndb._menutree.deny`   |
|desc   | `ndb._menutree.desc`   |
|name   | `ndb._menutree.name`   |
|options| `ndb._menutree.options`|

---

Bucket Options Mockup
---
```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs System.........1 .......Bucket Options......2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Timeout                        A    6. Bucket Manager(s)             F  ║
║  2. Privacy                        B    7. Write permissions to bucket   G  ║
║  3. Visibility                     C                                        ║
║  4. Act Codes                      D                                        ║
║  5. Permissions Submenu            E                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ..Help is available.................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

#### Menu Variables
1. System
2. Menu Title
3. Gamename
4. Menu_text

|Menu Variable|DB Variable                              |
|-------------|-----------------------------------------|
|System       |`evennia.world.jobs.jobs_defaults.SYSTEM`|
|Menu Title   |self.menu_title                          | 
|Menu Text    |self.menu_text                           |


#### Set options menu choices:<sup1</sup
A. Timeout ~: if input exists and in 'digit str' format: dbsave else: default, reprompt
B. Privacy  ~: toggle boolean for public/private; notify
C. Visibility (hidden) ~: toggle boolean for hidden; notify
D. Act Codes ~: review act codes and exit
E. Permissions ~: submenu
F. Bucket Manager(s) ~: add player(s) to the Bucket.db.manager_list
G. Write permissons to bucket ~: aggregate changes in permssions and write to bucket (Bucket.flush())

|Opt    | DB Attr                |
|-------|------------------------|
|act    | `ndb._menutree.act`    |
|hidden | `ndb._menutree.hidden` |
|perm   | `ndb._menutree.perm`   |
|privacy| `ndb._menutree.privacy`|
|timeout| `ndb._menutree.timeout`|


---

Bucket Permission Mockup
---
```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs System.........1 ........Bucket Permissions.2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Resolution                     A    6. Stats                         F  ║
║  2. Creation                       B    7. Log                           G  ║
║  3. Add                            C    8. Mail                          H  ║
║  4. Grant                          D    9. Write permissions to bucket   I  ║
║  5. Edit                           E                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ..Help is available.................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝

```
#### Menu Variables
1. System
2. Menu Title
3. Gamename
4. Menu_text

|Menu Variable|DB Variable                              |
|-------------|-----------------------------------------|
|System       |`evennia.world.jobs.jobs_defaults.SYSTEM`|
|Menu Title   |self.menu_title                          | 
|Menu Text    |self.menu_text                           |


#### Menu options
A. BBsys ~: If player can /complete/approve/deny jobs
B. Creation ~: If player can use the /create command
C. Add ~: If player can use the /add command
D. Grant ~: If player can use +bucket/access
E. Edit ~: If player can use the /edit command
F. Stats ~: If player can use the /edit command
G. Log ~:  If player can /log a job
H. Mail ~: If player can /query and /mail
I. Write permissions to bucket ~: Aggregate changed permissions and write to bucket (Bucket.flush())

|Permission |Boolean Test               |
|-----------|---------------------------|
|complete   | `.ndb._menutree.complete` |
|approval   | `.ndb._menutree.approval` |
|deny       | `.ndb._menutree.deny`     |
|create     | `.ndb._menutree.create`   |
|add        | `.ndb._menutree.add`      |
|grant      | `.ndb._menutree.grant`    |
|edit       | `.ndb._menutree.edit`     |
|stats      | `.ndb._menutree.stats`    |
|log        | `.ndb._menutree.log`      |
|mail       | `.ndb._menutree.mail`     |

---

Bucket Creation
---

#### Main Menu
1. +bucket
2. Option 3 (Create Bucket)
3. The following options have to be set: 1 (Name), 2 (Desc), 3-5 (bbsys - only if the game is using a bboard), 8 (Set options) must be run before bucket can be created
4. 6 (bucket manager) is only necessary if this is a non-staff bucket
5. 7 (grant access) is not necessary for bucket creation

#### Options Menu
1. The following options must be set before the bucket can be created: 1 (Timeout)
2. If it is a non staff bucket, then it will have to have Permissions set, as well as Privacy and Visibility before the bucket can be created
3. If it is a staff bucket, it will default to: Admin Perms, 30 day timeout, public visibility and unhidden privacy.


---

Bucket Limits and legend                                                      
---                                                                           
                                                                              
header_char_limit = 72                                                        
node_name_char_limit = 34                                                     
node_text_char_limit = 70 * 5                                                 
                                                                              
header_section = 1
node_options = [A-J]
body_section = 2


## Bucket Functionality

### Access
+bucket/access Player = Bucket - grants Player(s)/Org(s) access to Bucket.  Bucket Admin/Admin only command. 

##### Tests
Caller has perms
BB == Existing Bucket
PP Exists and not in BB.db.access_list

needed attr: Bucket.db.access_list
##### Logic
| Command             | What it does                         |
|---------------------|--------------------------------------|
|+bucket/access PP=BB | Grants player PP access to bucket BB |


```
switch = "access"
PP = self.lhs
BB = self.lhs
```

### Check

##### Tests
Caller has perms
PP == Existing Player

##### Logic
| Command         | What it does                                   |
|-----------------|------------------------------------------------|
|+bucket/check PP | Return list of buckets player PP has access to |

```
switch = "check"
PP = self.lhs
```

### Create

##### Tests
Caller has perms
BB != Existing Bucket
@@ != None

##### Logic
| Command             | What it does                                |
|---------------------|---------------------------------------------|
|+bucket/create BB=@@ | Creates Bucket named BB with description @@ |

```
switch = "create"
BB = self.lhs
@@ = self.rhs
```

### Delete

##### Tests
Caller has perms
BB == Existing Bucket
BB.db.total_jobs = 0

needed attribute Bucket.db.total_jobs

##### Logic
| Command          | What it does                      |
|------------------|-----------------------------------|
|+bucket/delete BB | Deletes bucket BB (must be empty) |

```
switch = "delete"
BB = self.lhs
```

### Help

##### Tests
Caller has perms
BB == Existing Bucket

##### Logic
| Command        | What it does              |
|----------------|---------------------------|
|+bucket/help BB | Return help for bucket BB |

```
switch = "help"
BB = self.lhs
```
### Info

##### Tests
Caller has perms
BB == Existing Bucket

##### Logic
| Command        | What it does              |
|----------------|---------------------------|
|+bucket/info BB | Return info for bucket BB |

```
switch = "info"
BB = self.lhs
```
### Monitor

##### Tests
Caller has perms
BB == Existing Bucket

##### Logic
| Command           | What it does                   |
|-------------------|--------------------------------|
|+bucket/monitor BB | Toggle monitoring of bucket BB |

```
switch = "monitor"
BB = self.lhs
```
### Options

##### Tests
Caller has perms
BB == Existing bucket
XX == Valid option
@@ == Valid option setting

##### Logic
| Command             | What it does                            |
|---------------------|-----------------------------------------|
|+bucket/set BB/XX=@@ | Sets option XX on bucket BB to value @@ |

```
switch = "set"
BB = self.lhs_noun
XX = self.lhs_verb
@@ = self.rhs
```
### Bucket List

##### Tests
Caller has perms

##### Logic
| Command | What it does                                             |
|---------|----------------------------------------------------------|
|+buckets | Display the current list of buckets caller has access to |

```
switch = ""
```
---

# Jobs


Jobs menu-driven interface mock
---

1. [+jobs](#+jobs)
2. [+job #](#+job-42)
3. [+job/reply #](#+job/reply-jobnum)
4. [+job/com](#+job/coms-job#) - Open communications menu
5. [+job/set](#+job/set-job#) - Open settings menu
6. [+job/info](#+job/info) - Open info menu
7. [+job/work](#+job/work-jobnum) - Open workbench menu
8. [+job/views](#+job/view:) - Open views menu
9. [+job/credits](#+job/credits) - Display credit information

### +jobs
```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs System.........1 ...........Job 42..........2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Create new job.................A                                        ║
║  2. Clear all new jobs.............B                                        ║
║  3. Search jobs....................C                                        ║
║  4. Views..........................D                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ..Help is available.................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
1. +job/create - Create a job manually
2. +job/clear - Clear new jobs
3. +job/search <pattern - Search jobs for <pattern
4. +job/views - Open the views menu

```
### +job/view:
also available with +job/view(s)
```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs System - Views.1 ...........................2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Yours..........................A    6. All jobs in a bucket..........F  ║
║  2. All............................B    7. By mod........................G  ║
║  3. New............................C    8. By priority...................H  ║
║  4. Overdue........................D    9. By player.....................I  ║
║  5. By Bucket......................E   10. Range in bucket...............J  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ..Help is available.................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
```


### +job 42

```
╔═════════════════════════════════════════════════════════════════════════════╗
║  .Jobs........1... ...............Job 42..........  2... .Mygamename..3...  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Communications.................A                                        ║
║  2. Settings.......................B                                        ║
║  3. Info...........................C                                        ║
║  4. Workbench......................D                                        ║
║  5. Lists..........................E                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ...........Type:.XXXX35 Character LimitXXXXXXXXXXXXX....Replies:.999999 │ ║
║ │ ......Opened by:.XXXX50 Character LimitXXXXXXXXXXXXXXXXXXXXXXXXXXXX.... │ ║
║ │ ......Opened on:.04/29/2018............................................ │ ║
║ │ ............Due:.05/22/2018.........4.................................. │ ║
║ │ ..........Title:.XXXX50 Character LimitXXXXXXXXXXXXXXXXXXXXXXXXXXXX.... │ ║
║ │ ....Assigned to:.XXXX50 Character LimitXXXXXXXXXXXXXXXXXXXXXXXXXXXX.... │ ║
║ │ ....Checked out: Y/N................................................... │ ║
║ │ .........Locked: Y/N...........Priority:.XXXX25 Character LimitXXXX...4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝

```
### +job/coms Job#

Also Option one(1) on `+job Job#`

```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs Communications.1 ...........Job 42..........2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Add comment....................A    6. Publish.......................F  ║
║  2. Mail Opener....................B    7. Email a log...................G  ║
║  3. Approve........................C                                        ║
║  4. Complete.......................D                                        ║
║  5. Deny...........................E                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ..Help is available.................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
1. Add a comment directly to job
2. Sends a message to the job opener(s)
3. Approves a job with user message
4. Completes a job with user message
5. Denies a job with user message
6. Publishes a job
7. Emails a log of the job to user input (format: someone@somewhere.com)
```
### +job/set Job#

Also Option two(2) on `+job Job#`

```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs Settings.......1 ...........Job 42..........2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Assign.........................A                                        ║
║  2. Change Summary.................B                                        ║
║  3. Change opener(s)...............C                                        ║
║  4. Tags...........................D                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ..Help is available.................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
1. Assign/Claim job
2. Change summary
3. Change Opener
4. Change Tags
```
### +job/info ##

Also Option three(3) on `+job Job#`

```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs Info...........1 ...........Job 42..........2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Actions........................A                                        ║
║  2. Header.........................B                                        ║
║  3. Summary........................C                                        ║
║  4. Report.........................D                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ..Help is available.................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
1. Display all actions performed on this job
2. Display the job header
3. Display the job summary
4. Pull a report
```



### +job/work JobNum

Also Option four(4) on `+job Job#`

```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs Workbench......1 ...........Job 42..........2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Clone..........................A    6. Transfer......................F  ║
║  2. Delete.........................B    7. Check In/Out..................G  ║
║  3. Edit...........................C    8. Lock/Unlock...................H  ║
║  4. Merge with another job.........D                                        ║
║  5. Set due date...................E                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ..Help is available.................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
1. Create a clone of this job, replies and actions
2. Delete this job (admin only)
3. Edit a job, name, header, body, or your reply/replies (may not edit replies that do not belong to you)
4. Merge this job into another
6. Set this job's due date (must be in valid local date format)
7. Transfer
8. Check the job out/in if it's not already checked
9. Lock or unlock the job
```

### +job/reply JobNum
```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs Workbench......1 ...........Job 42..........2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Show job message...............A    6. Reply to last comment.........F  ║
║  2. Reply to job...................B    7. Show flat list of comments....G  ║
║  3. List comments..................C                                        ║
║  4. Show Comment...................D                                        ║
║  5. Reply to comment...............E                                        ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ .Total threads:.XXXXXX................................................. │ ║
║ │ Total comments:.XXXXXX................................................. │ ║
║ │ .....Opened by:.XXXX50 Character LimitXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.... │ ║
║ │ Last commenter:.XXXX50 Character LimitXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.... │ ║
║ │ ..Last comment:.XXXXXX................................................. │ ║
║ │ .....Opened on:.04/29/2018............................................. │ ║
║ │ ...........Due:.05/22/2018............................................. │ ║
║ │ ....................................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
1. Displays the initial message submitted with the job
2. Replies to the initial message submitted with the job
3. Displays a list of comments to the job, with thread indicators
4. Shows a specific comment
5. Replies to a specific comment
6. Replies to the last comment
6. Displays non-threaded list of comments by time
```


## +job/credits
```
╔═════════════════════════════════════════════════════════════════════════════╗
║  Jobs Workbench......1 ...........Job 42..........2 Mygamename...........3  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. Credit #1......................A    6. ..............................F  ║
║  2. Credit #2......................B    7. ..............................G  ║
║  3. Credit #3......................C    8. ..............................H  ║
║  4. Credit #4......................D    9. ..............................I  ║
║  5. ...............................E   10. ..............................J  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ....................................................................... │ ║
║ │ ......................................................................4 │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
```



Single command driven Jobs interface mock
---

#### Jobs header mock 
```
╓═══════════════════════════════════XX1XX═════════════════════════════════════╖
│     Bucket: XXXXXXXX2XXXXXXXXX   Due Date: XXXXXXXXXXXXXXXX5XXXXXXXXXXXXXX  │
│ Created on: XXXXXXXX3XXXXXXXXX     Tagged: XXXXXXXXXXXXXXXX6XXXXXXXXXXXXXX  │
│ Created by: XXXXXXXX4XXXXXXXXX             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  │
│                                                                             │
│ Assigned to: XXXXXXXXXXXXXXXXXXXXXXXXX7XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  │
╰═════════════════════════════════════════════════════════════════════════════╯
```


Header variables
---
1. Job Number 
2. Bucket Name
3. Creation Date
4. Creator
5. Due Date
6. Tagged Players
7. Assignment

|Name         |DB Variable                |
|-------------|---------------------------|
|Job-number   | `self.db.job_number`      |
|Bucket       | `self.db.bucket`          |
|Creation Date| `self.db.createdon`       |
|creator      | `self.db.createdby`       |
|due date     | `self.db.due_by`          |
|tagged       | `self.db.tagged_players`  |
|assignment   | `self.db.assigned_players`|


#### Jobs initial message mock

```
╭┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╮
┇ .............................Initial Message............................... ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ Replies: XX2XX..................................Submitted By: XXXXX3XXXXXX. ┇
╰┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╯

View replies? (Default to yes - Enter opens a menu of replies if there are more than one, otherwise just loads the next reply)
```

Menu variables
---
1. Initial Message Body
2. total replies
3. job creator

|Name   |DB Variable                |
|-------|---------------------------|
|Msg    | `self.db.initial_msg`     |
|replies| `self.db.total_replies`   |
|creator| `self.db.created_by`      |


#### Jobs Reply Mock

```
╭┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╮
┇                           Reply to: XXXXXXXXXXX1XXXXXXXXXXXXX               ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX2XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ┇
┇ Replies: XX3XX..................................Submitted By: XXXXXX4XXXXX. ┇
╰┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╯

View replies? (Default to yes - Enter opens a menu of replies if there are more than one, otherwise just loads the next reply)
```
Menu variables
---
1. Parent msg/job
2. reply body
3. total replies
4. job creator

|Name   |DB Variable                |
|-------|---------------------------|
|parent | `self.db.msg_parent`      |
|reply  | `self.db.reply_msg`       |
|replies| `self.db.total_replies`   |
|creator| `self.db.created_by`      |


available replies:

1. Cleric Bob said: Foo bar baz....
2. Staffer Joe says: But then you could hold him by the nose...
3. Ranger Bill added a loot roll to the job
4. Taladan has approved this job with a message

Actions on job:
1. Creation
2. Assigned to taladan
3. Greenie was tagged for this job
4. Job was approved and posted to board 42, all triggers run successfully


#### Header fields

1 - Job Number as it appears in the system (not the hashed job id)
A - Bucket name
B - Job title
C - creation Date
D - Creator
E - Assignment
F - Due date
G - Status of job
H - Players/staff tagged in this job


### Job creation

+job/create - spawn job creation menu

```
╔═════════════════════════════════════════════════════════════════════════════╗
║  XXXXX1XXXXXXX.............XXXXXXXXXXX2XXXXXXXXXXX............XXXXXX3XXXXX  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. XXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXX                                        ║
║  2. XXXXXXXXXXXXXXXBXXXXXXXXXXXXXXXX                                        ║
║  3. XXXXXXXXXXXXXXXCXXXXXXXXXXXXXXXX                                        ║
║  4. XXXXXXXXXXXXXXXDXXXXXXXXXXXXXXXX                                        ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX4XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

Menu variables
---
1. System
2. Menu Title
3. Gamename
4. Menu text

Menu Options
---
A. Title ~:> if title is not None, dbsave
B. bucket ~:> if exists and player can post, dbsave
C. Tagged players ~:> if player(s) exist, dbsave
D. Message ~:> if msg is not None, dbsave


|Option|DB Variable                   |
|------|------------------------------|
|Title |`ndb._menutree.title`         |
|Bucket|`ndb._menutree.bucket`        |
|Tags  |`ndb._menutree.tagged_players`|
|Msg   |`ndb._menutree.message`       |


Jobs Limits and legend
---
job_number = 1
message_line_length = 75
message_line_count = 18+??

## Jobs functionality

Please note:  When I refer to job id or message id in the functionality, I am only referring to the number that appears in the output of the display.  Each job and comment/reply will have its own unique hash id, and I will refer to these specifically as 'job hash id' or 'message hash id'.

### Communication

#### Add comments to a job

We should be able to do threaded replies into a job structure available to users.  Functionality we could do something like:

+job/reply 42=This is my comment to job -- this just tags a standard straight line of comments (reply to initial comment)
+job/reply 42/5=This is my comment to Staffer Jolene's reply to job 42.

How do I thread more deeply?

Maybe use a menu driven system completely to interact with jobs.

##### Tests: 
Caller has perms
@@ != None
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False
If using +job/reply, there must be an initial comment on the job.
If using +job/reply, the comment passed in XX must exist.

##### Logic:

Job exists with comment.  

|Command                | What it does                                                                               |
|-----------------------|--------------------------------------------------------------------------------------------|
|+job/comment JJ = @@   | Add a comment to the initial message +job/comment JJ=comment                               |
|+job/reply JJ/XX = @@  | Reply to a comment that already exists, where JJ == Job id and XX == the Comment/reply id. |

```
switch == ("comment","reply")
JJ == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs

```

#### Mails opener with <message>

##### Tests: 
Caller has perms
@@ != None
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Hooks:
mailsys

##### Logic:

|Command           | What it does                         |
|------------------|--------------------------------------|
|+job/mail JJ = @@ | Mails opener of job id J with message|

```
switch == ("mail")
JJ == self.lhs
@@ == self.rhs
```

##### Boilerplate message:

```

=============================================================================== 
| XXXXXX1XXXXXXXX            Reply to Job XX2XX             XXXXXXX3XXXXXXXX  |
=============================================================================== 
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX4XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
=============================================================================== 

```
|Variable|Area   |DB attr                            |
|--------|-------|-----------------------------------|
|1       |System | `evennia.world.jobs.SYSTEM`       |
|2       |Job ID | `evennia.world.jobs.job.db.number`|
|3       |Date   | `datetime.datetime.now`           |
|4       |Message| user input                        |



#### Publish a job or <comment>

##### Tests:
Caller has perms
@@ != None
JJ == Existing Job
if XX: XX == Existing comment
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Hooks:
bbsys

##### Logic:
|Command               | What it does                             |
|----------------------|------------------------------------------|
|+job/publish JJ       | Publishes job to publish board           |
|+job/publish JJ/XX    | Publishes comment to publish board       |

```
switch == ("publish")
JJ == self.lhsnoun
XX == self.lhsverb
```

#### Send a query to <players>

##### Tests:
Caller has perms
@@ != None
XX != None
PP == Valid player or player list

##### Logic:
|Command               | What it does                                            |
|----------------------|---------------------------------------------------------|
|+job/query PP/XX = @@ | Query list of players (PP) with message (@@) titled (XX)|

```
switch == ("query")
PP == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs
```
### Finalization

#### Approve a player job

> ##### AJ Notes
> When you close out a LOOT queue using +job/approve, add your closing message to each player's +journal.

##### Tests:
Caller has perms
@@ != None
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Hooks:
bbsys
mailsys

##### Logic:
|Command            | What it does                   |
|-------------------|--------------------------------|
|+job/approve JJ=@@ | Approve job JJ with message @@ |

```
switch == ("approve")
JJ == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs
```

#### Complete a job

##### Tests:
Caller has perms
@@ != None
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Hooks:
bbsys
mailsys

##### Logic:

|Command             | What it does                    |
|--------------------|---------------------------------|
|+job/complete JJ=@@ | Complete job JJ with message @@ |

```
switch == ("complete")
JJ == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs
```

#### Deny a player job

##### Tests:
Caller has perms
@@ != None
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:

|Command         | What it does                |
|----------------|-----------------------------|
|+job/deny JJ=@@ | Deny job JJ with message @@ |

```
switch == ("deny")
JJ == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs
```

#### Logs a job

First step - need to research logging within Evennia a bit more.  

##### Tests:

Caller has perms
JJ == Existing Job
@@ == string in format 'someone@somewhere.com'
JJ.db.checked_out == caller or False
Log directory must be set (internal)

##### Logic:

|Command        | What it does                        |
|---------------|-------------------------------------|
|+job/log JJ=@@ | Mails a log of job JJ to address @@ |

```
switch == ("log")
JJ == self.lhs
@@ == self.rhs
```

### Job Settings Functionality

#### Search jobs for <pattern>

##### Tests:

Caller has perms
@@ != None

##### Logic:

|Command        | What it does           |
|---------------|------------------------|
|+job/search @@ | Search all jobs for @@ |

```
switch == ("search")
@@ == self.lhs
```


# TODO: NEEDED FUNCTION

def player_perm():


#### Assign a job to player

##### Tests:
Caller has perms
JJ == Existing Job
@@ == Valid player list or "me"
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Hooks:
eventsys

##### Logic:

|Command           | What it does                     |
|------------------|----------------------------------|
|+job/assign JJ=@@ | Assign Job JJ to Player (list) @@|

- This assigns a job to a player or player list
- Mails notification

```
switch == ("assign")
JJ == self.lhs
@@ == self.rhs # Special, if self.rhs.lower() == "me", assign to caller
```

#### Change a job summary setting

The following systems should be able to use the sumset to automate some task handling:

* Events:

> ---
> 
> On event creation, automatically create job or allow users to relink events to different/multiple jobs??
> # TODO: DEPRECATED
> +event/link <event#>=<job#> -  link the specifed event# to the specified PLOTS job#
> 
> Include name, date/time, DM, and confirmed players (if any).
> 
> ---


NOTES 1: +event/link NEVER GOT USED. It was an idea we'd love to have had, and would help players, but it was one of those 'one more things' atop the camel's back. A GM runs a scene, and they shouldn't need to worry about additional fiddly bits like that.

* Calendar
??
> Recurring dates (IC or OOC) that automatically post/update jobs ??

* Orgs
??
> Org leaders should be able to update summaries on org jobs...org events tie-in...

* Chargen
> Player application processed through jobs automatically

* NPC System
> Documentation and creation of NPC's/tracking npc's that recur

---

# TODO: needed job attribute

self.db.summary = {key:setting, key1: setting, key3: setting,}
Query: Do we want to allow parsing of summaries in jobs system for locks or other special strings?  Perhaps we can use job summaries to simulate triggers/hooks in AJ.

Expose `Job.sumset()`

---

##### Tests:
Caller has perms
JJ == Existing Job
XX != None
@@ != None
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:

|Command              | What it does                                       |
|---------------------|----------------------------------------------------|
|+job/sumset JJ/XX=@@ | Sets (creates) field XX with contents @@ on job JJ |

```
switch == ("sumset")
JJ == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs
```

#### Change opened-by to <player list>

##### Tests:
Caller has perms
JJ == Existing Job
@@ == Valid player or player list or org
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Hooks:
orgsys

##### Logic:
|Command           | What it does                                                     |
|------------------|------------------------------------------------------------------|
|+job/source JJ=@@ | Changes Job JJ's `self.db.createdby` to @@ (may be a player list)|

```
switch == ("source")
JJ == self.lhs
@@ == self.rhs
```

#### Clear new jobs

##### Tests:
check for new jobs

##### Logic:
|Command    | What it does                             |
|-----------|------------------------------------------|
|+job/clear | Clear 'new' flag from jobs on any bucket |

```
switch == ("clear")
```
jobid hash goes into character.db.jobs_read = [ASDF, HJLK, QWER]


Code frag
```
for job in jobs:
  if job not in character.db.jobs_read:
    # Mark job as read
    character.db.jobs_read.append(job.id)
```

#### Clone a job

##### Tests:
Caller has perms
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:
|Command      | What it does                                     |
|-------------|--------------------------------------------------|
|+job/clone JJ| Makes an identical copy of Job JJ (new instance) |

```
switch == ("clone")
JJ == self.lhs
```

---

#### Create a job manually

Query to Beag: Does anybody actually need to be able to manually create a job??  Should this be deprecated due to the menu integration for job creation?
Query Reply - Yes 
Integration with menu creation should override the need for any line-level setting of job options.  Should this still be a thing?  Perhaps after I get a working product I'll explore the need for the ability to have attribute-level access to the job object from within the game (+job/set timeout=XX days, etc.)

##### Tests:

##### Logic:

On hold until testing can be done with menu-based creation system.

---

#### Delete a job (Admin)

##### Tests:
Caller has perms
JJ == Existing job
JJ.db.locked == False
JJ.db.checked_out == caller or False


##### Hooks:
bbsys
mailsys
eventsys
orgsys

##### Logic:
|Command       | What it does   |
|--------------|----------------|
|+job/delete JJ| Deletes Job JJ |


```
switch == ("delete")
JJ == self.lhs
```

When the job is deleted it should not be locked, it shouldn't be checked out or in any other paused state and should fire delete_hooks

---

# TODO: needed job function

def delete_hook(self, num):
    """run these hooks in at_channel_delete()"""
    pass

Query: Should we expose `Job.delete_hook()`?
---



#### Edits a job - Any part of the job may be edited - Creator or bucket admin perms

##### Tests:
Caller has perms
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False
if XX: XX == Valid coment on job JJ
if OLD in JJ or JJ/XX: replace OLD with NEW else: caller.msg: Old not found in JJ


##### Logic:
|Command                 | What it does                                    |
|------------------------|-------------------------------------------------|
|+job/edit JJ=OLD/NEW    | Edits Initial comment on Job JJ repl OLD w/ NEW |
|+job/edit JJ/XX=OLD/NEW | Edits comment XX on Job JJ repl OLD w/ NEW      |


```
switch == ("edit")
JJ == self.lhsnoun
XX == self.lhsverb
OLD == self.rhsnoun
NEW == self.rhsverb

pull `evennia.world.jobs.jobutils.argparse(self.lhs, self.rhs)`
```

#### Escalate a job's priority

##### Tests:
Caller has perms
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False
@@ in JJ.db.valid_priorities

---

Query to Beag: 
would it be more useful to be able to implement your own prioritization schema instead of using a stock l/m/h type scheme in job Priority stuff? Or would you rather just have a stock l/m/h?

---

##### Logic:
|Command        | What it does                      |
|---------------|-----------------------------------|
|+job/esc JJ=@@ | Escalates job JJ's priority to @@ |


```
switch == ("esc")
JJ == self.lhs
@@ == self.rhs

pull `evennia.world.jobs.jobutils.argparse(self.lhs, self.rhs)`
```

#### Merge <source> into <destination>

This allows a Caller to merge one job into another.  Single merge-type, appending source onto destination

##### Tests:
Caller has perms
@@ == Existing Job
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False
@@.db.locked == False
@@.db.checked_out == caller or False

##### Logic:
|Command          | What it does                            |
|-----------------|-----------------------------------------|
|+job/merge JJ=@@ | Merge job JJ into @@ (appends JJ to @@) |


```
switch == ("merge")
JJ == self.lhs
@@ == self.rhs
```

#### Rename a job

##### Tests:
Caller has perms
@@ != None
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:
|Command           | What it does        |
|------------------|---------------------|
|+job/rename JJ=@@ | Rename job JJ to @@ |


```
switch == ("rename")
JJ == self.lhs
@@ == self.rhs
```

#### Set job due date - Due date defaults to bucket timeout in days

##### Tests:
Caller has perms
@@ == valid date format (MM/DD/YYYY, MM-DD-YYYY, localize option: DD-MM-YYYY, DD/MM/YYYY)
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:
|Command        | What it does              |
|---------------|---------------------------|
|+job/due JJ=@@ | Set job JJ due date to @@ |


```
switch == ("due")
JJ == self.lhs
@@ == self.rhs
```

#### Set progress status on a job


query Beag: Should progress (AJ: +job/set #=hold|new|underway|25|50|75|100) be set on job?  Does anyone use this?


##### Tests:
##### Logic:

#### Transfer (or undelete) a job

##### Tests:
Caller has perms
@@ == Valid bucket
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:
|Command             | What it does                 |
|--------------------|------------------------------|
|+job/transfer JJ=@@ | Transfer job JJ to bucket @@ |


```
switch == ("due")
JJ == self.lhs
@@ == self.rhs
```

### Locks

#### Check in/out a job

##### Tests:
Caller has perms
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:
|Command       | What it does         |
|--------------|----------------------|
|+job/check JJ | Checks in/out job JJ |

if JJ.db.checked_out == False:
    JJ.db.checked_out = caller
elif: JJ.db.checked_out == caller:
    JJ.db.checked_out = False
else:
    caller.msg(Checked out error)

```
switch == ("check")
JJ == self.lhs
```

#### Locks/Unlocks a job and prevents changes

##### Tests:
Caller has perms
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:
|Command      | What it does         |
|-------------|----------------------|
|+job/lock JJ | Locks/Unlocks job JJ |

if JJ.db.locked == False:
    JJ.db.locked = True
else:
    JJ.db.locked = False

```
switch == ("lock")
JJ == self.lhs
```

### Tags

#### Tags a job for <player>

##### Tests:
Caller has perms
@@ == Existing player or list of existing players
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:
|Command        | What it does                 |
|---------------|------------------------------|
|+job/tag JJ=@@ | Tags job JJ for player(s) @@ |


```
switch == ("tag")
JJ == self.lhs
@@ == self.rhs
```

#### Untags a job

##### Tests:
Caller has perms
@@ == Existing player or list of existing players
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:
|Command          | What it does                   |
|-----------------|--------------------------------|
|+job/untag JJ=@@ | Untags job JJ for player(s) @@ |


```
switch == ("untag")
JJ == self.lhs
@@ == self.rhs
```
### Display

#### Display actions on a job

##### Tests:
Caller has perms
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

##### Logic:
|Command      | What it does                                        |
|-------------|-----------------------------------------------------|
|+job/acts JJ | Display list of actions performed on job JJ to date |

```
switch == ("acts")
JJ == self.lhs
```

#### Display credit information 
Refer to [menu driven](#+job/credits) mock for credits display reference.

##### Tests:

##### Logic:
|Command      | What it does                                 |
|-------------|----------------------------------------------|
|+job/credits | Display list contributors to the jobs system |

```
switch == ("credits")
```


#### Display help for a job's bucket

##### Tests:
Caller has perms
JJ == Existing Job

##### Logic:
|Command      | What it does                            |
|-------------|-----------------------------------------|
|+job/help JJ | Display help for the job and its bucket |

```
switch == ("help")
JJ == self.lhs
```

#### Display replies to a job or job reply

##### Tests:
Caller has perms
JJ == Existing Job
JJ.db.locked == False
JJ.db.checked_out == caller or False

---

04-29-18, (10:57) - Query to Beag:  Do we want threaded messages in jobs or is a flat message structure preferred?

---

##### Logic:
|Command           | What it does                            |
|------------------|-----------------------------------------|
|+job/thread JJ    | Display help for the job and its bucket |
|+job/thread JJ/XX | Display help for the job and its bucket |

# Todo - Finish this

```
switch == ("help")
JJ == self.lhs
```

#### Get a report


---

04-29-18, (11:18) - query Beag: Does anyone ever use the reports functionality of jobs system?

---

04-29-18, (17:40) - This should be a backend item on the webserver. -- Tal

##### Tests:
##### Logic:

#### List all/yours/new/overdue/player/bucket jobs

##### Tests:
Caller has perms
JJ in ("all", "mine", "new", "overdue", "playername", "bucketname")

##### Logic:
|Command      | What it does                                                    |
|-------------|-----------------------------------------------------------------|
|+job/list JJ | Lists jobs by pattern (all, mine, new, overdue, Player, bucket) |

```
switch == ("list")
JJ == self.lhs
```

#### View a job

##### Tests:
Caller has perms
JJ == Existing Job

##### Logic:
|Command | What it does   |
|--------|----------------|
|+job JJ | Display job JJ |

```
switch == (None)
JJ == self.lhs
```

#### View a job's header & summary

##### Tests:
Caller has perms
JJ == Existing Job

##### Logic:
|Command      | What it does                          |
|-------------|---------------------------------------|
|+job/info JJ | Display header and summary for job JJ |

```
switch == ("info")
JJ == self.lhs
```

#### AJ Action codes
_(these may or may not all make it into the system, they are simply here for reference)_


|CODE|Description                                                           |
|----|:--------------------------------------------------------------------:|
|ADD |Player comment. Generated with +job/add.                              |
|APR |+job/approve closing action.                                          |
|ASN |Assignment to a user.                                                 |
|AUT |Automatic hook. If set, will run daily.                               |
|CKI |Checked In.                                                           |
|CKO |Checked Out.                                                          |
|CLN |Clone action. Only appears on the newly created job.                  |
|COM |+job/complete generates this closing action.                          |
|CRE |Can only be first comment. Generated with +job/create.                |
|DEL |+job/delete closing action.                                           | 
|DNY |+job/deny closing action.                                             |
|DUE |Due date change.                                                      |
|EDT |Indicates when a comment has been edited.                             |
|LOK |Indicates when a job has been locked.                                 |
|MRG |Indicates a job that has been merged from two jobs.                   |
|NAM |Indicates a title change.                                             |
|OTH |A job created by any means other than /create triggers the OTH hook.  |
|PUB |Indicates a job/comment has been published.                           |
|SRC |Indicates when a job's OPENED_BY (source) has changed.                |
|STA |A +job/set status change.                                             |
|SUM |Indicates a change in the summary settings.                           |
|TAG |Indicates a job has been tagged or untagged.                          |
|TRN |Indicates a job has been transferred.                                 |
|UNL |Job unlocking action.                                                 |
|UNP |Indicates a job/comment has been unpublished.                         |
                                                                              
                                                                              
                                                                              
