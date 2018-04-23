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


More will be added as I get it written up.

--Tal

