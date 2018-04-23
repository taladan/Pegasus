## Bucket Menu Pseudocode:

### Bucket Creation Mockup

```
╔═════════════════════════════════════════════════════════════════════════════╗
║1 $System.......................Bucket Creation...................$Gamename  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║A 1. Name............................ F  6. Bucket Manager.................. ║
║B 2. Description..................... G  7. Grant access.................... ║
║C 3. Approval Board.................. H  8. Set Options..................... ║
║D 4. Denial Board.................... I  9. ................................ ║
║E 5. Completion Board................ J 10. ................................ ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ....................................................................... │ ║
║ │ ....Welcome to Bucket creation.  Help is available for each option. ... │ ║
║ │ ....................................................................... │ ║
║2│ ....................................................................... │ ║
║ │ ...Please note: Each menu option must be completed for bucket.......... │ ║
║ │ ................creation to complete. ................................. │ ║
║ │ ....................................................................... │ ║
║ │ ....................................................................... │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

### Creation menu choices:<sup>1</sup>

1. Name ~:> if bucket doesn't exist: if name isn't too long: dbsave else: reprompt too long else: reprompt exists
2. Description ~:> if desc exists, if it is too long: trunc and dbsave, else dbsave, else error
3. Approval board ~:> if board exists and bucket can post, dbsave
4. Denial Board ~:>  if board exists and bucket can post, dbsave
5. Completion Board ~:> if board exists and bucket can post, dbsave
6. Bucket manager (test if it's a player, default is admin perms) ~:>  if player exists: dbsave else: dbsave; set admin perms
7. Grant Access ~:> if player exists and doesn't have access, dbsave
8. Set options ~:> submenu


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
║1 $System......................Bucket Options.....................$Gamename  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║A 1. Timeout......................... F  6. ................................ ║
║B 2. Privacy......................... G  7. ................................ ║
║C 3. Visibility...................... H  8. ................................ ║
║D 4. Act Codes....................... I  9. ................................ ║
║E 5. Permissions..................... J 10. ................................ ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ....................................................................... │ ║
║ │ ....Defaults for a new bucket are below. Help for each option is....... │ ║
║ │ ....available. ........................................................ │ ║
║2│ ..................Default:...........Value:............................ │ ║
║ │ ...................Permissions.........Admin........................... │ ║
║ │ ...................Timeout.............30 days......................... │ ║
║ │ ...................Visibility..........Public.......................... │ ║
║ │ ...................Privacy.............Unhidden........................ │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

### Set options menu choices:<sup>1</sup>
1. Timeout ~:> if input exists and in 'digit str' format: dbsave else: default, reprompt
2. Privacy  ~:> toggle boolean for public/private; notify
3. Visibility (hidden) ~:> toggle boolean for hidden; notify
4. Act Codes ~:> review act codes and exit
5. Permissions ~:> submenu

|Opt    | DB Attr                |
|-------|------------------------|
|act    | `ndb._menutree.act`    |
|hidden | `ndb._menutree.hidden` |
|perm   | `ndb._menutree.perm`   |
|privacy| `ndb._menutree.privacy`|
|timeout| `ndb._menutree.timeout`|

<sup>1</sup> - Each choice in a menu needs to have an attendant help file.

---

### Bucket Permission Mockup
```
╔═════════════════════════════════════════════════════════════════════════════╗
║1 $System....................Bucket Permissions...................$Gamename  ║
╠═════════════════════════════════════════════════════════════════════════════╣
║A 1. Completion...................... F  6. Grant*.......................... ║
║B 2. Approval........................ G  7. Edit............................ ║
║C 3. Denial.......................... H  8. Stats........................... ║
║D 4. Creation........................ I  9. Log............................. ║
║E 5. Add............................. J 10. Mail............................ ║
╠═════════════════════════════════════════════════════════════════════════════╣
║ ╭─────────────────────────────────────────────────────────────────────────╮ ║
║ │ ....................................................................... │ ║
║ │ ...Be aware that you are granting bucket level access for each option.  │ ║
║ │ ....................................................................... │ ║
║2│ ...Help is available for each option. ................................. │ ║
║ │ ....................................................................... │ ║
║ │ ....................................................................... │ ║
║ │ ...* - Makes person a Bucket SuperUser................................. │ ║
║ │ ....................................................................... │ ║
║ ╰─────────────────────────────────────────────────────────────────────────╯ ║
╚═════════════════════════════════════════════════════════════════════════════╝
```
#### Access Permissions

1. Completion ~:> If player can /complete jobs
2. Approval ~:> If player can /approve jobs
3. Denial ~:> If player can /deny jobs
4. Creation ~:> If player can use the /create command
5. Add ~:> If player can use the /add command
6. Grant ~:> If player can use +bucket/access
7. Edit ~:> If player can use the /edit command
8. Stats ~:> If player can use the /edit command
9. Log ~:>  If player can /log a job
10. Mail ~:> If player can /query and /mail

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

#### AJ Action codes
_(these may or may not all make it into the system, they are simply here for reference)_

|CODE|Description
|----|:--------:|
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

## The bucket creation process

1. +bucket
2. Option 3 (Create Bucket)
3. prompt for bucket name (test if valid name, if not reprompt)
4. prompt for bucket description (test if description is too long, if so, truncate)
5. prompt for bboard to post to

Limits and legend
---

header_char_limit = 72
node_name_char_limit = 34
node_text_char_limit = 70 * 5

header_section = 1
node_options = [A-J]
body_section = 2

---

