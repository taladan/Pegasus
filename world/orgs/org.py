#!/usr/bin/python
# -*- coding utf-8 -*-

import evennia as ev
from evennia import DefaultScript
from evennia.utils import lazy_property
from evennia.utils.logger import EvenniaLogFile
from world.utilities.pegasus_utilities import hash

SYSTEM = "orgs"


class Org(DefaultScript):
    """Groups are scripts that handle factioning/organizing characters within the database into
    logical orderings.  Examples might include:

    OOC Groups:
    -----------
    * player helpers
    * GMs
    * Board moderators

    IC Groups:
    ----------
    * Thieve's guild
    * Adventerur's Guild
    * Player made factions


    # Todo: Functionality to add to orgs as the systems are developed
    * Mailing lists - should be able to easily mail members of a org
    * BBoard integration - Group bulletin board management
    * Jobs integration - Bucket for org jobs
    * Administrative functionality - Creation, deletion, renaming, redescribing, adding and removing players
    * events - Group scheduled events should only be open/visible to members of the org
    * inventory - Group vaults/inventory
    * logsys - logging and posting of scenes to a org wiki
    """

    def __init__(self):
        pass

    def at_script_creation(self):
        """set up org variables

        :return:Nothing
        """
        # Todo: fix and delete dummy
        dummy = "some_value"
        self.db.character_list = lambda: self._return_characters()
        self.tags.add("Group", category="Groups")
        self.ndb.log = EvenniaLogFile()
        self.ndb.logfile = "orgs.log"
        self.db.admins = []
        self.db.mailsender=self.key
        self.db.bboard = 0
        self.db.bucket = self.key
        self.db.vault = dummy
        self.db.log_conf = dummy
        """
        Todo: Clean this up
        Admins:
            add members
            create mailers
            modify bbsys settings
            jobs handling
            event scheduling
            inventory management
            logsys configuration
        """

    @lazy_property
    def _return_characters(self):
        """query and return a list of all players in org

        :return:chars - a list object containing django query objects that are evennia Characters
        """
        objs = ev.search_tag(self.db.gid)
        chars = []
        for obj in obj:
            if pu.ischaracter(obj):
                chars.append(obj)
        return chars

    # Public methods
    def add(self, character):
        """add a character to the org listing

        :return:Nothing
        """
        character.tags.add(self.db.gid)

    def create(self, name=None, desc=None):
        """create a org

        :return: Group object
        """
        hashobj = name + desc
        org = ev.create_script(key=name, typeclass=Org, persistent=True)
        org.db.gid = hash(name, hashobj)
        org.db.description = desc
        org.db.mailsender=org.key
        org.db.bboard = 0 # Todo: fix
        org.db.bucket = org.key
        org.db.vault = "some value" # Todo: fix
        org.db.log_conf = "Some value" # Todo: fix
        return org

    def is_member(self, character):
        """determing org membership

        :return:Boolean for character membership in a particular org
        """
        return character in self.db.character_list

    @staticmethod
    def list():
        """:return: query object of orgs"""
        return ev.search_tag("Group", category="Groups")

    def remove(self, character):
        """remove character from the org listing

        :parameter:character - must be an evennia character object
        """
        try:
            character.tags.remove(self.db.gid)
        except Exception as e:
            msg = "Removal of character {0} from org {1} failed.".format(character, self.key) + e
            self.ndb.log.log_file(msg, self.ndb.logfile)
            raise e
