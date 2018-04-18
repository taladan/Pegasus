#!/usr/bin/python
#! -*- coding utf-8 -*-

import unittest
from evennia.commands.default.tests import EvenniaTest
from world.utilities.pegasus_utilities import input


# Todo: create tests for pegasus_utilities
class TestPegasusUtils(EvenniaTest):
    def setUp(self):
        super(EvenniaTest, self).setUp()
        pass

    def tearDown(self):
        super(EvenniaTest, self).tearDown()
        pass

    def testInput(self):
        """test getting and returning player input"""
        caller = "Test Caller"
        string = "This is a test string"
        test = input(caller, string)
        self.assertEqual(test, string)
        self.assertNotEqual(test, caller)

    def test_log(self):
        """test the logging facility of pegasus utilities"""
        # Todo - Finish and fix
        msg = "This is a test message."
        exception = "ValueError"
        system = "groups"
        # log(msg, exception, system)
