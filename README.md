# What is the Pegasus Project?

The Pegasus project is an opensource (GPLv3) suite of tools that facilitate the creation, administration and enjoyment of a text based gaming environment.  Below you'll find a list of things on the roadmap, but suffice it to say that with any mu* server base that's available, there's always a need for good, dependable, standardized tooling that allows administrators and players to customize their experience.  As Pegasus develops, more of the ideology behind it will be explored - watch for updates!

# How do I contribute?

I've been getting this question lately and the answer to that is in [The Code Contributor's Manifesto](https://github.com/taladan/Pegasus/wiki/Contribute)<sup>_(Queue the scary music, Dave)_</sup>.


#### Info coming soon

I will be migrating this stuff to the project board_settings as I get time.
Some of this may not make the cut.


# Pegasus
Server Base             - Evennia: http://www.evennia.com/
RPG System base         - Pathfinder: 

Doc Definitions
---
- [ ] OOC:     Out of Character (this is all server/RL information) 
- [ ] IC:      In character (pertaining to the people/places/things in
         the game environment.)
- [ ] USER:    A person who connects to the game - account level in Evennia
- [ ] PLAYER:  Character being enacted (puppeted) by the User
- [ ] BUILDER: User with building/story creating permissions
- [ ] ADMIN:   User with administrative permissions for dealing with
         OOC & IC situations
- [ ] OWNER:   the person that owns the game (taladan@gmail.com)

- Priority system is ranked by stars (*).  The higher the stars,
the higher the priority



Table of Contents
===
##### BASE OOC SYSTEMS:(*****)
- [ ] Jobs (****)        - akin to the functionality of anomaly jobs - Buckets are in, working on jobs
- [ ] BBS (****)        - Handles users to post public/semi-public
                    info for other users to see/comment on
- [ ] Mail (***)         - Allow Users to @mail one another
- [ ] Weather (**)       - Weather systems for zones
- [ ] Calendar (**)      - Handles day/night/month/year cycles
- [ ] Game Info (*****)  - Gives general info about the game/players
- [ ] Events (***)       - Allows Users to schedule events/rp/plots
- [ ] Faction/Group (**) - This will handle factions and groups.  God help us all
- [ ] Notepad (*)        - Allows Users to keep lists/notes/journals

#####  BASE CHARACTER SYSTEMS:(****)
- [ ] Chargen (*****)     - Allow User to generate a character
- [ ] Languages (**)      - Allow Characters to speak in different
                       languages/understand different languages
- [ ] Mapping (***)       - Allow Characters to access map ingame (and website)
- [ ] +Sheet (*****)      - Allow Characters to see/use +sheet
- [ ] Combat (****)       - Handles combat functionality for Characters

##### BASE AGMIN (GM) SYSTEMS:(****)
- [ ] NPC System (***)   - Allow Admin (GM's) To create & puppet NPC characters
- [ ] +Sheet (*****)     - Allow Admin (GM's) to manipulate sheets
- [ ] Combat (****)      - Handles combat functionality for Admin
- [ ] GM Ambience (**)   - Handle GM info ambience in rooms/objects
  


# Project Details

BASE OOC SYSTEMS (*****)
===
These systems are for general utility purpose within the game,
 handling communications and passing information to the Users.

Jobs:(****)
----------
  Description: This system is designed to handle the creation and organization
               of different IC/OOC tasks, requests, feature requests, admin
               issues/discussions (such as theme development, plot development,
               and other tasks that require a collaborative environment. This
               should be similar enough to the BBS that it should feel like a
               discussion that can be closed/archived.  The idea and inspiration
               for this system is Anomaly Jobs:

               Code:    (https://tinyurl.com/ycs3b5za)
               Howto:   (https://tinyurl.com/yd46volk)

The following commands do not yet exist:
```
+jobs <#>                               : Review job #

+jobs                                   : List jobs.
............................................................................
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
    /edit <#>/<entry#>=<old>/<new>      : Edits a job
    /esc <#>=<green|yellow|red>         : Escalate a job's priority
    /help <#>                           : Display help for a job's bucket
    /last <#>=<X>                       : List last <X> entries in <#>
    /lock <#>                           : Locks a job and prevents changes
    /log <#>                            : Logs a job
    /mail <#>=<message>                 : Mails opener with <message>
    /merge <source>=<destination>       : Merge <source> into <destination>
    /name <#>=<name>                    : Rename a job
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
```

The following commands exist (and function!) for buckets:
```
+buckets
    /info <bucket>
    /monitor <bucket>
    /create <bucket>=<description>
    /delete <bucket>
    /access <player>=<bucket>
    /check <player>
    /set <bucket>/<setting>=<value>
```

These commands do not yet exist:
```
+jgroups

    /info <jgroup>
    /create <jgroup>=<description>
    /delete <jgroup>
    /member <player>=<jgroup>
```

BBS:(****)
----------
  Description: The Bulletin Board System operates as a static forum that allows
               group discussion, questions, advertisements, etc. between all 
               Users.

               Inspiration: Myrrdin's BBS (https://tinyurl.com/y92b4x6n)

               Flaskbb - Potential inspiration.  A Python based bbs for websites
                         (https://tinyurl.com/y7hu2mjm)

Mail:(***)
----------
  Description: The mail system coordinates the sending and recieving of in-game
               mail.  This is modeled after the standard email system (SMTP) in
               spirit.  In practicality it is based off the MUX mail system and
               other similar mailers like BrandyMail, etc. that are widely known
               by players of mu*'s.

  Example: /evennia/contrib/mail.py

  * Archival            - Allow Characters to archive mail messages

  * Delete              - Allow Characters to delete their own mail

  * Retract             - Allow Characters to retract sent messages
                          that haven't been read

  * Sending             - Allow Characters to send mail to other characters
                          Commands/Switches:
                            CC       - Carbon Copy
                            BCC      - Blind Carbon Copy
                            Proof    - Proofread draft before sending
                            Edit     - change text in message before sending
                            Abort    - Abandon (and delete) current message
                            Reply    - Reply to message sender
                            Replyall - Reply to all recipients
                            Quote    - Quote text of message to reply
                            Forward  - Forward message to another Character
                            Clear    - Clear messages for deletion
                            Purge    - Purge messages marked as Clear
                            Tag      - Tag messages belonging to same/similar
                                       category
                            Safe     - Set mail to be safe from expiration
                            Expire   - Set expiration duration for folders

  * Folders             - Allow Characters to organize mail into
                          folders/categories

Weather:(**)
----------
  Description: Handles weather emits, storing a bank of appropriate emits
               configured by zone - think of this more as an Ambiance system
               not only a weather system (should handle interior rooms as well).

  * 

Calendar:(**)
----------
  Description: Handles the passage of time, day/night cycle, as well as the 
               seasonal cycle.  Should display events from the +events system
               in calendar format as well.
  
  * 

Game Info:(*****)
----------
  Description: This system handles allowing Users to query the game, staff and
               other Users for OOC Game information.

  * +finger/+profile    - Allowing players to share info 
                          (offline accessible) with others

  * +who                - Shows who is currently connected
                          with idle times and loc if jumpok

  * +where              - Show the locations of characters
                          grouped if they're together in the 
                          same location.

  * +idle               - Show who sorted by idle times

  * +staff              - Show all staffers along with connected
                          staff, busy/free/offduty

  * +watch              - Allow users to add Characters to a
                          watchlist for when they (dis)connect

Events:(***)
----------
  Description: Handles allowing Users to schedule and run events - (rp, plots,
               festivals, other gatherings of Users).  Should tie in with the
               calendar for displaying upcoming events IC'ly.

  * +event <#>          - View details about a specific event
  * +events             - Lists all events in the system. The red ones have
                          already happened

    Player Switches:
    ---

        /view ##          View details about a specific event

        /signup ##        Places you on a waitlist for the event
                          The event creator will then confirm you
                          if you are going to be attending. If the
                          event is an all-come event then you
                          probably do not have to wait for a
                          confirmation

        /leave ##         This command allows you to leave an
                          event you've signed up for. If you were
                          already confirmed, then it will notify
                          the creator by @mail

        /add              This command adds an event to the
                          system. It will ask you to give details
                          about your event, and then it will
                          populate it in the list as well as
                          announce it on a bboard

    Organizer Switches:
    ---

        /desc #=<desc>    This command lets you reset the
                          description of your event

        /loc #=<loc>      This command lets you reset the location
                          of your event

        /time #=<time>    This command lets you reset the time you
                          will run your event

        /levels #=<lev>   This command lets you change the level
                          range posted for your event

        /rename #=<name>  This command lets you rename your event

        /delete #         This command deletes your event

        /conf #=<Name>    This command lets you confirm someone
                          from the waitlist

        /unconf #=<name>  This command lets you send someone back
                          to the waitlist

Faction/Group:(**)
----------
  Description: This will handle factions and groups.  God help us all.

  *

Notepad:(*)
----------
  Description: A notepad system for Users to be able to keep track of notes, lists, etc

  *

********************************************************************************
BASE CHARACTER SYSTEMS  - These systems handle the Character level information
(****)                    including all IC stating information, combat
                          resolution character generation, setting, handling
                          and display of sheet information as well as RP
                          commands to enhance the roleplay experience.
********************************************************************************

Chargen:(*****)
----------
  Description: Handles the creation and recording of each Character object
               within the game.  This system handles setting up the +sheet info
               as well as any other necessary character creation steps such as
               setting +finger/+profile information, etc.

  * 

Language System:(**)
----------
  Description: Allows Characters to speak in different languages and translates
               languages into non-sensible series of appropriate syllables for
               non-speakers of the language.  Should be blind-toggleable so that
               people with screenreaders don't have to listen to the
               gobbledygook.

  Lang system for evennia -  https://tinyurl.com/y6uwmnhl
  * Blind capable: (Ex: Taladan says a lengthy sentence in Elvish
                        Taladan says something in Elvish
                        Taladan says a few words in Elvish)

Mapping System:(***)
----------
  Description: Allows Characters/Users to display any pertinent mapping info
               that is available to them.

  * 

+Sheet System:(*****)
----------
  Description: Displays Character information to the User so they may track 
               Character progress within the game.

  * 

Combat System:(****)
----------
  Description: Handles combat resolution (fighting/spellcasting/healing/etc) as
               well as information about opponents.

  * 

********************************************************************************
BASE AGMIN (GM) SYSTEMS - These systems handle administrative commands as they
(****)                    pertain to managing RP scenes, character needs, plot
                          running.
********************************************************************************

NPC System:(***)
----------
  Description: Allows Admin (GM's) to create & puppet NPC characters for the 
               purposes of roleplay, scenes, plot, etc.  This system should
               handle and track all pertinent NPC information so as to allow
               any Admin to be able to use any NPC that is available should the
               need arise. Also should keep a roster of NPC's available for use.

  * +Roster             - Maintains a roster of available NPCs with details of
                          who created the NPC, the plots it was used in, and a
                          brief writeup of the NPC for RP purposes.


+Sheet System:(*****)
----------
  Description: Allows Admin (GM's) to manipulate sheets of npcs and Characters,
               viewing them, fixing them, and using them to resolve RP/Combat
               questions.

  * 

Combat System:(****)
----------
  Description: Allows Admin (GM's) to run combat within an RP scene in a manner
               that allows the Admin to puppet the NPC's and handle combat
               resolution in a sensible manner (no automated bots in scenes).

  * Queueing            - A system of aggregating groups of npcs/monsters to use
                          in a RP scene/plot.  Inspiration:
                               https://improved-initiative.com

GM Ambience:(**)
----------
  Description: Each room should be able to have information set on it to notify
               access to any GM/Admin commands available in the room.  This system
               will be settable with a +runplot command or similar to change active
               status of the GM to 'Plotting', reveal the ambience notifiers in the 
               room, temporarily remove non-admin channels and give access to any
               other tools.
________________________________________________________________________________
________________________________________________________________________________

GENERAL IDEA CRUFT:
________________________________________________________________________________
________________________________________________________________________________

Plot system     - The ability to 'snapshot' pc's so that they can resume an event
                  that paused with the same +sheet info they've been using so that
                  it merges together with any changes in their current sheet by the
                  end of the adventure

Character class - Concentration Wizard/Magic User.  Allow a pool of points (PoP)
                  to draw from as per level.  PoP could be drawn from Intelligence
                  and constitution type scores - a synergy type of system.  These
                  magic users can pop a point for an ingame hour's worth of a somehow
                  limited access to their level of spells. (Maybe spells/day? type
                  effect?)  Within that hour they can simulate the effect of any
                  spell in their list (maybe that they've trained/learned?) 

                  Int: 19 - 4
                  Con: 19 - 4


                  
GM Stuff        - I'd like to allow players to become GM's in their own right - as per
                  the FATE ruleset.  Allowing them to run as they wish will free up the
                  need to hire/recruit GM's.  This system should have a voting/reward 
                  for people who GM and are voted up by the other players.  This will
                  urge more people to GM who are able to and eventually lend them to 
                  perhaps wanting to staff/contribute.

		  Perhaps a system of 'reward' pools for GMs who level their GM status
		  so that they open up over time as the person GMs, allowing more powerful
		  ingame rewards available to give the players, as well as aspects they can
		  access in a scene.  

Rumors network  - NPC's spread public rumors, guild/faction npcs and players in factions/groups
		  can spread rumors within a group.  Perception style check to 'overhear' rumor
		  between NPC/PC or PC/PC.

Lore system     - maybe similar to rumors but for more esoteric world lore.  Could have different levels
                  of lore that need to be unlocked before the higher levels can be accessed.  Tiered.
