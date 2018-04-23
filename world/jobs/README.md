## Jobs

Jobs is a task management system based on the Bucket Class.  It gives the players and staff of a game a way to have a static communication that can be accessed whether the sender is offline/online, however it is not /as/ static as mail.  Jobs allows players and staff to reply to comments put on the job, as well as perform actions against a job, such as adding players to access it, mailing the senders/players who are attached to the job, assigning of jobs to different people, approving/completing/denying jobs and posting to relevant bboards.  Jobs is also able to be hooked into by any other system so that communication can be automated and not segregated from the actions performed.

For example:

1. Cleric Bob adds a job requesting that his +3 mace be enchanted to have disruption on it.
2. Staffer Josephine replies to cleric bob that, though there's an issue with the magic code right now, they'll have it done as soon as possible.
3. Staffer Wheel lets Cleric Bob know that the mace can't be enchanted because Cleric Bob forgot that the mace was crafted out of forgettium, and it quickly becomes disenchanted if someone tries to put a new enchantment on it.
4. Staffer Josephine adds Ranger Flip to the job
5. Ranger Flip replies that he's got a scroll of unforgettium and is willing to give it to Cleric Bob if Cleric Bob will go on an adventure with him.
6. Staffer Wheel says that's cool and enchants the mace, approving the job
7. The job gets archived and posted to a bboard


This is the flow of responses.  They can happen over a period of minutes or days if that's what it takes - the data is stored on the job channel and then retrieved as necessary.

Jobs belong to buckets for organization.  Buckets are a type of communications channel (inherits from the Evennia Channel class) and it acts as a notification hub as well as organizing jobs into groupings categorized by the bucket creators.  This will allow control over what types of jobs are sent to specific buckets.


The structure of bucket and job creation
----------------------------------------

bucket system options:

|option|action|
|:-----|:-----|
1. bucket info|retrieve information about a bucket
2. check access|check a player's access
3. create bucket|bucket creation process
4. delete bucket|deleting a bucket
5. grant access|grant access to a player
6. rename bucket|rename a bucket
7. set options|change an option on a bucket
8. toggle monitor|toggle monitoring on a bucket

This is a template of the form that I cobbled together as a generic template:

```
Proposed Standard Form:

header_char_limit = 72
node_name_char_limit = 34
node_text_char_limit = 70 * 5

header_section = 1
node_options = [A-J]
body_section = 2
╔═════════════════════════════════════════════════════════════════════════════╗
║  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║  ccccccccccccccccAcccccccccccccccccc   cccccccccccccccccFccccccccccccccccc  ║
║  ccccccccccccccccBcccccccccccccccccc   cccccccccccccccccGccccccccccccccccc  ║
║  ccccccccccccccccCcccccccccccccccccc   cccccccccccccccccHccccccccccccccccc  ║
║  ccccccccccccccccDcccccccccccccccccc   cccccccccccccccccIccccccccccccccccc  ║
║  ccccccccccccccccEcccccccccccccccccc   cccccccccccccccccJccccccccccccccccc  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX2XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ │ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝

Proposed Mobile Form:

header_char_limit = 34
node_name_char_limit = 15
node_text_char_limit = 34 * 5

header_section = 1
node_options = [A-J]
body_section = 2
.-------------------------------------.
| XXXXXXXXXXXXXXXX1XXXXXXXXXXXXXXXXXX |
.-------------------------------------.
| cccccccAccccccc     cccccccFccccccc |
| cccccccBccccccc     cccccccGccccccc |
| cccccccCccccccc     cccccccHccccccc |
| cccccccDccccccc     cccccccIccccccc |
| cccccccEccccccc     cccccccJccccccc |
.-------------------------------------.
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXX2XXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
| XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX |
.-------------------------------------.
```

Check out [Evennia's Forms](https://github.com/evennia/evennia/wiki/evennia.utils.evform) for more information on using forms for output.


### Creation menu choices:<sup>1</sup>

1. Name
2. Description
3. Approval board
4. Denial Board
5. Completion Board
6. Bucket manager (test if it's a player, default is admin perms)
7. Grant Access
8. Set options

#### Set options menu choices:<sup>1</sup>
1. Timeout
2. Public/Private
3. Hidden
4. Action codes 
5. Access permissions

<sup>1</sup> - Each choice in a menu needs to have an attendant help file.

#### AJ Action codes
_(these may or may not all make it into the system, they are simply here for reference)_

|CODE|Description
|----|---------:|
ADD|Player comment. Generated with +job/add.
APR|+job/approve closing action.
ASN|Assignment to a user.
AUT|Automatic hook. If set, will run daily.
CKI|Checked In.
CKO|Checked Out.
CLN|Clone action. Only appears on the newly created job.
COM|+job/complete generates this closing action.
CRE|Can only be first comment. Generated with +job/create.
DEL|+job/delete closing action.
DNY|+job/deny closing action.
DUE|Due date change.
EDT|Indicates when a comment has been edited.
LOK|Indicates when a job has been locked.
MRG|Indicates a job that has been merged from two jobs.
NAM|Indicates a title change.
OTH|A job created by any means other than /create triggers the OTH hook.
PUB|Indicates a job/comment has been published.
SRC|Indicates when a job's OPENED_BY (source) has changed.
STA|A +job/set status change.
SUM|Indicates a change in the summary settings.
TAG|Indicates a job has been tagged or untagged.
TRN|Indicates a job has been transferred.
UNL|Job unlocking action.
UNP|Indicates a job/comment has been unpublished.


#### Access Permissions

|Permission|Boolean test
COMPLETE_ACCESS|If player can /complete jobs.
APPROVE_ACCESS|If player can /approve jobs.
DENY_ACCESS|If player can /deny jobs.
CREATE_ACCESS|If player can use the /create command.
ADD_ACCESS|If player can use the /add command.
GIVE_ACCESS|If player can use +bucket/access.
EDIT_ACCCESS|If player can use the /edit command.
STATS_ACCESS|If player can pull reports on the system.
LOG_ACCESS|If player can /log a job.
MAIL_ACCESS|If player can /query and /mail.

## The bucket creation process

1. +bucket
2. Option 3 (Create Bucket)
3. prompt for bucket name (test if valid name, if not reprompt)
4. prompt for bucket description (test if description is too long, if so, truncate)
5. prompt for bboard to post to


More will be added as I get it written up.

--Tal

