#!/usr/bin/python
# -*- coding utf-8 -*-

# imports go here
import evennia as ev
from org import Org
from evennia.utils.test_resources import EvenniaTest
from mock import MagicMock, patch
from cmdorgs import CmdOrg
mock = MagicMock()


class TestCmdOrg(EvenniaTest):
    def __init__(self):
        pass

    def setUp(self):
        super(TestCmdOrg, self).setUp()
        pass

    def tearDown(self):
        super(TestCmdOrg, self).tearDown()
        pass

    def explanation_of_tests(self):
        """test creation of org objects

        for each individual test, I need to pass user input to test the return of the method.
        mock.patch [example](https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests)

        Patch template:

        *   @patch('', self.player_input='')

        name - The player should input a name here and should print any extant messages inside the method
        desc
        board
        vault
        """
        pass

    def fail(self):
        """
        Keep working on nodes - they are not patching correctly when I run them with @patch - need to research
        how to properly run a patch on it if Evennia is going to be blocking that syntax?  Trace output:

            TESTING: Using Evennia's default settings file (evennia.settings_default).
            (use 'evennia --settings settings.py test .' to run tests on the game dir)

        Traceback (most recent call last):
          File "/home/swift/muddev/pyenv/bin/evennia", line 6, in <module>
            exec(compile(open(__file__).read(), __file__, 'exec'))
          File "/home/swift/muddev/evennia/bin/unix/evennia", line 10, in <module>
            main()
          File "/home/swift/muddev/evennia/evennia/server/evennia_launcher.py", line 1338, in main
            django.core.management.call_command(*args, **kwargs)
          File "/home/swift/muddev/pyenv/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 131, in call_command
            return command.execute(*args, **defaults)
          File "/home/swift/muddev/pyenv/local/lib/python2.7/site-packages/django/core/management/base.py", line 330, in execute
            output = self.handle(*args, **options)
          File "/home/swift/muddev/pyenv/local/lib/python2.7/site-packages/django/core/management/commands/test.py", line 62, in handle
            failures = test_runner.run_tests(test_labels)
          File "/home/swift/muddev/pyenv/local/lib/python2.7/site-packages/django/test/runner.py", line 600, in run_tests
            suite = self.build_suite(test_labels, extra_tests)
          File "/home/swift/muddev/evennia/evennia/server/tests.py", line 45, in build_suite
            return super(EvenniaTestSuiteRunner, self).build_suite(test_labels, extra_tests=extra_tests, **kwargs)
          File "/home/swift/muddev/pyenv/local/lib/python2.7/site-packages/django/test/runner.py", line 513, in build_suite
            tests = self.test_loader.discover(start_dir=label, **kwargs)
          File "/usr/lib/python2.7/unittest/loader.py", line 206, in discover
            tests = list(self._find_tests(start_dir, pattern))
          File "/usr/lib/python2.7/unittest/loader.py", line 287, in _find_tests
            for test in self._find_tests(full_path, pattern):
          File "/usr/lib/python2.7/unittest/loader.py", line 287, in _find_tests
            for test in self._find_tests(full_path, pattern):
          File "/usr/lib/python2.7/unittest/loader.py", line 268, in _find_tests
            yield self.loadTestsFromModule(module)
          File "/usr/lib/python2.7/unittest/loader.py", line 65, in loadTestsFromModule
            tests.append(self.loadTestsFromTestCase(obj))
          File "/usr/lib/python2.7/unittest/loader.py", line 56, in loadTestsFromTestCase
            loaded_suite = self.suiteClass(map(testCaseClass, testCaseNames))

        TypeError: __init__() takes exactly 1 argument (2 given)

        :return:
        """
        assert FAIL

    # Todo: Finish configuring test data for node tests
    @patch('CmdOrg._get_input, self.player_input="Test Org"')
    def test_cmdorg_name(self):
        expected = "Test Org"
        caller = self.char1
        CmdOrg._name(self, caller)
        self.assertEqual(CmdOrg.org_opts["name"], expected)

    @patch('CmdOrg._get_input, self.player_input="This is a test org"')
    def test_cmdorg_desc(self,):
        caller = self.char1
        CmdOrg._name(self, caller, raw_string)

    @patch('CmdOrg._get_input, self.player_input=0')
    def test_cmdorg_board(self):
        caller = self.char1
        CmdOrg._board(self, caller, raw_string)

    @patch('CmdOrg._get_input, self.player_input=0')
    def test_cmdorg_vault(self):
        caller = self.char1
        CmdOrg._vault(self, caller, raw_string)

