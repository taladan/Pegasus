#!/usr/bin/python
# -*- coding utf-8 -*-

# imports go here
import evennia as ev
from evennia.utils.test_resources import EvenniaTest
from mock import MagicMock, patch
from cmdorgs import CmdOrgs

mock = MagicMock()
test_org = 'Twilight guild'

"""
## Patch stuff - @patch('cmdorg.CmdOrgs._get_input.player_input', test_org)
def explanation_of_tests(self):
for each individual test, I need to pass user input to test the return of the method.
mock.patch [example](https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests)

Patch template:

*   @patch('', self.player_input='')

name - The player should input a name here and should print any extant messages inside the method
desc
board
vault
pass
"""
class TestCmdOrg(EvenniaTest):

    def setUp(self):
        super(TestCmdOrg, self).setUp()
        pass

    def tearDown(self):
        super(TestCmdOrg, self).tearDown()
        pass

    @patch('CmdOrgs()._get_input.player_input', test_org)
    def test_cmdorg_name(self):
        """
        Test _start functionality on `cmdorg.CmdOrgs.py`.
        #
        Need instantiation
        To do that we need to be able to simulate player input into the 'Name' field of the dict attribute:
            `self.org_opts["name"] = self.player_input`
        #
        Then we need to retrieve the value of self.org_opts["name"] to test it against the set value.
        #
        Organization name: "Twilight Guild"
        #
        :return:
        """
        expected = test_org
        caller = self.char1
        CmdOrgs._name(caller)
        self.assertEqual(CmdOrgs.org_opts["name"], expected)

    # def test_cmdorg_desc(self,):
    #     caller = self.char1
    #     CmdOrgs._desc1(caller, raw_string)
    #
    # def test_cmdorg_board(self):
    #     caller = self.char1
    #     CmdOrgs._set_desc_prompt_for_board(caller, raw_string)
    #
    # def test_cmdorg_vault(self):
    #     caller = self.char1
    #     CmdOrgs._vault(caller, raw_string)
    #     pass
