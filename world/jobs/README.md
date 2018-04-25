Bucket
---

### Bucket Creation Mockup

```
╔═════════════════════════════════════════════════════════════════════════════╗
║  XXXXX1XXXXXXX.............XXXXXXXXXXX2XXXXXXXXXXX............XXXXXX3XXXXX  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. XXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXX    6. XXXXXXXXXXXXXXFXXXXXXXXXXXXXXXX  ║
║  2. XXXXXXXXXXXXXXXBXXXXXXXXXXXXXXXX    7. XXXXXXXXXXXXXXGXXXXXXXXXXXXXXXX  ║
║  3. XXXXXXXXXXXXXXXCXXXXXXXXXXXXXXXX    8. XXXXXXXXXXXXXXHXXXXXXXXXXXXXXXX  ║
║  4. XXXXXXXXXXXXXXXDXXXXXXXXXXXXXXXX                                        ║
║  5. XXXXXXXXXXXXXXXEXXXXXXXXXXXXXXXX                                        ║
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

Menu Variables
--------------
1. System
2. Menu Title
3. Gamename
4. Menu_text

|Menu Variable|DB Variable                              |
|-------------|-----------------------------------------|
|System       |`evennia.world.jobs.jobs_defaults.SYSTEM`|
|Menu Title   |self.menu_title                          | 
|Menu Text    |self.menu_text                           |

Creation menu choices:<sup>1</sup>
----------------------

A. Name ~:> if bucket doesn't exist: if name isn't too long: dbsave else: reprompt too long else: reprompt exists
B. Description ~:> if desc exists, if it is too long: trunc and dbsave, else dbsave, else error
C. Approval board ~:> if board exists and bucket can post, dbsave
D. Denial Board ~:>  if board exists and bucket can post, dbsave
E. Completion Board ~:> if board exists and bucket can post, dbsave
F. Bucket manager (test if it's a player, default is admin perms) ~:>  if player exists: dbsave else: dbsave; set admin perms
G. Grant Access ~:> if player exists and doesn't have access, dbsave
H. Set options ~:> submenu


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

### Bucket Options Mockup
```
╔═════════════════════════════════════════════════════════════════════════════╗
║  XXXXX1XXXXXXX.............XXXXXXXXXXX2XXXXXXXXXXX............XXXXXX3XXXXX  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. XXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXX                                        ║
║  2. XXXXXXXXXXXXXXXBXXXXXXXXXXXXXXXX                                        ║
║  3. XXXXXXXXXXXXXXXCXXXXXXXXXXXXXXXX                                        ║
║  4. XXXXXXXXXXXXXXXDXXXXXXXXXXXXXXXX                                        ║
║  5. XXXXXXXXXXXXXXXEXXXXXXXXXXXXXXXX                                        ║
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

Menu Variables
--------------
1. System
2. Menu Title
3. Gamename
4. Menu_text

|Menu Variable|DB Variable                              |
|-------------|-----------------------------------------|
|System       |`evennia.world.jobs.jobs_defaults.SYSTEM`|
|Menu Title   |self.menu_title                          | 
|Menu Text    |self.menu_text                           |


Set options menu choices:<sup>1</sup>
-------------------------------------
A. Timeout ~:> if input exists and in 'digit str' format: dbsave else: default, reprompt
B. Privacy  ~:> toggle boolean for public/private; notify
C. Visibility (hidden) ~:> toggle boolean for hidden; notify
D. Act Codes ~:> review act codes and exit
E. Permissions ~:> submenu

|Opt    | DB Attr                |
|-------|------------------------|
|act    | `ndb._menutree.act`    |
|hidden | `ndb._menutree.hidden` |
|perm   | `ndb._menutree.perm`   |
|privacy| `ndb._menutree.privacy`|
|timeout| `ndb._menutree.timeout`|


---

### Bucket Permission Mockup
```
╔═════════════════════════════════════════════════════════════════════════════╗
║  XXXXX1XXXXXXX.............XXXXXXXXXXX2XXXXXXXXXXX............XXXXXX3XXXXX  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  1. XXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXX    6. XXXXXXXXXXXXXXFXXXXXXXXXXXXXXXX  ║
║  2. XXXXXXXXXXXXXXXBXXXXXXXXXXXXXXXX    7. XXXXXXXXXXXXXXGXXXXXXXXXXXXXXXX  ║
║  3. XXXXXXXXXXXXXXXCXXXXXXXXXXXXXXXX    8. XXXXXXXXXXXXXXHXXXXXXXXXXXXXXXX  ║
║  4. XXXXXXXXXXXXXXXDXXXXXXXXXXXXXXXX    9. XXXXXXXXXXXXXXIXXXXXXXXXXXXXXXX  ║
║  5. XXXXXXXXXXXXXXXEXXXXXXXXXXXXXXXX   10. XXXXXXXXXXXXXXJXXXXXXXXXXXXXXXX  ║
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
Access Permissions<sup>1</sup>
------------------------------

Menu Variables
--------------
1. System
2. Menu Title
3. Gamename
4. Menu_text

|Menu Variable|DB Variable                              |
|-------------|-----------------------------------------|
|System       |`evennia.world.jobs.jobs_defaults.SYSTEM`|
|Menu Title   |self.menu_title                          | 
|Menu Text    |self.menu_text                           |


Menu options
------------
A. Completion ~:> If player can /complete jobs
B. Approval ~:> If player can /approve jobs
C. Denial ~:> If player can /deny jobs
D. Creation ~:> If player can use the /create command
E. Add ~:> If player can use the /add command
F. Grant ~:> If player can use +bucket/access
G. Edit ~:> If player can use the /edit command
H. Stats ~:> If player can use the /edit command
I. Log ~:>  If player can /log a job
J. Mail ~:> If player can /query and /mail

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

## The bucket creation process

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


<sup>1</sup> - **_Each choice in a menu needs to have an attendant help file._**

---

Copypasta stuff for later

Bucket Limits and legend                                                      
---                                                                           
                                                                              
header_char_limit = 72                                                        
node_name_char_limit = 34                                                     
node_text_char_limit = 70 * 5                                                 
                                                                              
header_section = 1
node_options = [A-J]
body_section = 2


## Bucket Functionality

# Todo: fix this
+bucket/access <player>=<bucket>
+bucket/check <player>
+bucket/create <bucket>=<description>
+bucket/delete <bucket>
+bucket/help <bucket>
+bucket/info <bucket>
+bucket/monitor <bucket>
+bucket/set <bucket>/<setting>=<value>
+buckets


---

Jobs
---



#### Anomaly jobs output
```
===============================| View Job 1 |================================
   Bucket: CODE                             Due On: -
    Title: Building System                  Status: Green (New)
Opened On: Sun Apr 27 16:10:57 2008    Assigned To: Nobody
Opened By: Swift
   Tagged: Meg and Aurinko
-----------------------------------------------------------------------------
This is the main body message - what's tagged onto the job at creation
-----------------------------------------------------------------------------
[2+] This is an addt'l message in reply
-----------------------------------------------------------------------------
[5+] This is the 5th action on this job hence the number.
-----------------------------------------------------------------------------
[6+]  they continue
================================| [Myjobs] |=================================
```

#### Data fields
Bucketname
Job Number As it appears on the system (seperate from job id -- which is a hash)
Title
Date Created
Creator
Tags
Due Date
Status
Assigned to

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

##### Tests: 

- Job must exist
- Player commenting must have permission to access
- If using +job/reply, there must be an initial comment on the job.

##### Logic:

Job exists with comment.  

|Command              | What it does                                                                               |
|---------------------|--------------------------------------------------------------------------------------------|
|+job/comment ## = @@ | Add a comment to the initial message +job/comment ##=comment                               |
|+job/reply ##/XX=@@  | Reply to a comment that already exists, where ## == Job id and XX == the Comment/reply id. |

```
switch == ("comment","reply")
## == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs

```

#### Mails opener with <message>

##### Tests: 

- hook into mail sys * (waiting on mail system integration)

##### Logic:
|Command               | What it does                         |
|----------------------|--------------------------------------|
|+job/mail ## = message| Mails opener of job id # with message|

```
switch = ("mail")
## == self.lhs
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

- Job/comment must exist
- hook into bbsys * (waiting on bbsys integration)

|Command               | What it does                             |
|----------------------|------------------------------------------|
|+job/publish ##       | Publishes job to publish board           |
|+job/publish ##/XX    | Publishes comment to publish board       |

```
switch = ("publish")
## == self.lhsnoun
XX == self.lhsverb
```

#### Send a query to <players>

##### Tests:

- Players must exist and be tagged to job
- hook into mail sys * (waiting on mail system integration)

##### Logic:

|Command               | What it does                                            |
|----------------------|---------------------------------------------------------|
|+job/query ##/XX = @@ | Query list of players (##) with message (@@) titled (XX)|

```
switch = ("query")
## == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs
```
### Finalization

#### Approve a player job

##### Tests:
- Job must exist
- hook into bbsys #### (waiting on bbsys integration)
- hook into mail sys #### (waiting on mail system integration)

##### Logic:

|Commandi           | What it does                   |
|-------------------|--------------------------------|
|+job/approve ##=@@ | Approve job ## with message @@ |

```
switch = ("approve")
## == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs
```

#### Complete a job

##### Tests:
- Job must exist
- hook into bbsys #### (waiting on bbsys integration)
- hook into mail sys #### (waiting on mail system integration)

##### Logic:

|Command             | What it does                    |
|--------------------|---------------------------------|
|+job/complete ##=@@ | Complete job ## with message @@ |

```
switch = ("complete")
## == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs
```

#### Deny a player job

##### Tests:
- Job must exist
- hook into bbsys #### (waiting on bbsys integration)
- hook into mail sys #### (waiting on mail system integration)

##### Logic:

|Command         | What it does                |
|----------------|-----------------------------|
|+job/deny ##=@@ | Deny job ## with message @@ |

```
switch = ("deny")
## == self.lhsnoun
XX == self.lhsverb
@@ == self.rhs
```

#### Logs a job

##### Tests:
##### Logic:


### Manipulation

#### Search jobs for <pattern>

##### Tests:
##### Logic:

#### Assign a job to player

##### Tests:
##### Logic:

#### Assign a job to yourself

##### Tests:
##### Logic:

#### Changes a job SUMMARY setting

##### Tests:
##### Logic:

#### Changes opened-by to <player list>

##### Tests:
##### Logic:

#### Clear new jobs

##### Tests:
##### Logic:

#### Clone a job

##### Tests:
##### Logic:

#### Create a job manually

##### Tests:
##### Logic:

#### Delete a job (Admin)

##### Tests:
##### Logic:

#### Edits a job - Any part of the job may be edited - Creator or bucket admin perms

##### Tests:
##### Logic:

#### Escalate a job's priority

##### Tests:
##### Logic:

#### Merge <source> into <destination>

##### Tests:
##### Logic:

#### Rename a job

##### Tests:
##### Logic:

#### Set job due date - Due date defaults to bucket timeout in days

##### Tests:
##### Logic:

#### Set progress status on a job

##### Tests:
##### Logic:

#### Transfer (or undelete) a job

##### Tests:
##### Logic:


### Locks

#### Check in a job

##### Tests:
##### Logic:

#### Check out a job

##### Tests:
##### Logic:

#### Locks a job and prevents changes

##### Tests:
##### Logic:

#### Unlocks a job

##### Tests:
##### Logic:


### Tags

#### Tags a job for <player>

##### Tests:
##### Logic:

#### Tags a job for you

##### Tests:
##### Logic:

#### Untags a job

##### Tests:
##### Logic:

#### Untags a job for <player list>

### Display

#### Display actions on a job

##### Tests:
##### Logic:

#### Display credit information ??

##### Tests:
##### Logic:

#### Display help for a job's bucket

##### Tests:
##### Logic:

#### Display replies to a job or job reply

##### Tests:
##### Logic:

#### Get a report

##### Tests:
##### Logic:

#### List all jobs in <bucket>

##### Tests:
##### Logic:

#### List all/yours/new jobs

##### Tests:
##### Logic:

#### List jobs

##### Tests:
##### Logic:

#### List jobs matching <expression>

##### Tests:
##### Logic:

#### List last <X> entries in <#>

##### Tests:
##### Logic:

#### List overdue jobs

##### Tests:
##### Logic:

#### Lists jobs assigned to player

##### Tests:
##### Logic:

#### Lists jobs by bucket/mod/pri

##### Tests:
##### Logic:

#### View a job

##### Tests:
##### Logic:

#### View a job's header & summary

##### Tests:
##### Logic:



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
                                                                              
                                                                              
                                                                              
