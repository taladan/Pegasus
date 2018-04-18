
import unittest
import evennia as ev
from evennia.commands.default.tests import EvenniaTest
from evennia.utils import create
import jobutils as ju
from jobs_settings import ERROR_PRE, SUCC_PRE, TEST_PRE, SYSTEM
from evennia.objects.objects import DefaultObject, DefaultCharacter, DefaultRoom, DefaultExit
from world.jobs.job import Job
from world.jobs.bucket import Bucket

sep = " == > "


class TestSuite(unittest.TestSuite):
    """This will run all the tests"""
    def run(self, result, debug=False):
        pass


class TestUtilties(EvenniaTest):
    """tests for evaluating methods in `world.utilities.pegasus_utilities`"""

    # Todo - parsing switches? string1 = "+cmd_noun/cmd_verb lhs_noun/lhs_verb=rhs_noun/rhs_verb"
    def test_hash(self):
        """hash returns unique hash, even if given identical strings"""
        from world.utilities import pegasus_utilities as pegasus
        hash_a = pegasus.hash(key="test", string="test")
        hash_b = pegasus.hash(key="test", string="test")
        self.assertNotEqual(hash_a, hash_b)

    def test_parse_args(self):
        """test that parse args returns correct information
        :expected: { stringN: outN, . . .}
        :stringN: test pattern to pass through `world.utilities.pegasus_utilities.StringTools.parse_args`
        """
        from world.utilities.pegasus_utilities import StringTools as st

        st = st()
        parse = st.parse_args

        # Test strings
        string0 = "lhs_noun/lhs_verb=rhs_noun/rhs_verb"
        string1 = "lhs_noun=rhs_noun/rhs_verb"
        string2 = "lhs_noun/lhs_verb=rhs_noun"
        string3 = "lhs_noun=rhs_noun"
        string4 = "lhs_noun"

        # output patterns
        out0 = "lhs_noun", "lhs_verb", "rhs_noun", "rhs_verb"
        out1 = "lhs_noun", False , "rhs_noun", "rhs_verb"
        out2 = "lhs_noun", "lhs_verb", "rhs_noun", False
        out3 = "lhs_noun", False, "rhs_noun", False
        out4 = "lhs_noun", False, False, False

        patterns = [out0, out1, out2, out3, out4]
        expected = patterns

        strings = [string0, string1, string2, string3, string4]
        actual = []
        for string in strings:
            actual.append(parse(string))
        self.assertEqual(expected, actual)


class TestBucket(EvenniaTest):
    """Test the Bucket portion of the system"""

    def setUp(self):
        """perform set up objects required for testing buckets"""
        # Run super
        super(TestBucket, self).setUp()
        pass

    def tearDown(self):
        """perform teardown of objects created for testing buckets"""
        # Run super
        super(TestBucket, self).tearDown()
        pass

    def test_bucket_set_attributes(self):
        pass

        def setUp(self):"""test setting of bucket attributes"""
        # Todo: create
        pass

    def attrstuff(self):
        """do something with the attribute dictionary

        Attribute map:
        
            0 - string digit
            1 - string digit
            2 - DefaultCharacter
            3 - string digit
            4 - int
            5 - string
            6 - string
            7 - Bool
            8 - int
            9 - int
            10 - int
            11 - int
            12 - int
            13 - float
            14 - int
            15 - list
            16 - dict
            17 - string
        """
        attrs={"db.approval_board": "42",
               "db.completion_board": "3",
               "db.createdby": "repl",
               "db.denial_board": "repl",
               "db.due_timeout": "repl",
               "db.group": "repl",
               "db.hash": "repl",
               "db.locked": "repl",
               "db.num_completed_jobs": "repl",
               "db.num_approved_jobs": "repl",
               "db.num_denied_jobs": "repl",
               "db.num_of_jobs": "repl",
               "db.resolution_time": "repl",
               "db.percent_complete": "repl",
               "db.total_jobs": "repl",
               "db.valid_actions": "repl",
               "db.valid_settings": "repl",
               "db.default_notification": "repl"}

        digits_lst = [0, 1, 3]
        strings_lst = [5, 6, 17]
        int_lst = [4, 8, 9, 19, 11, 12, 14]
        float_lst = 13
        list_lst = 15
        dict_lst = 16

        for attr in attrs:
            pass

        # TODO - come back and fix all this mess
        pass


    def test_bucket_create(self):
        """Test bucket creation with correct parameters

            This is what we need to test in bucket creation:

            Test correct message is returned to the user
            Test any attributes that are supposed to be automatically set on a bucket are set
            Test duplicate buckets cannot be created
            Test all attributes that belong on a bucket can be added correctly and be retrieved when called

            ### Bucket methods to test:

                * at_channel_creation
                * associated
                * per_player_actions
                * create
                * grant_access
                * has_jobs
                * has_access
                * info
                * monitoring
                * _pct_complete
                * remove_access
                * my_jobs
                * jobids
                * set
                * _total_jobs

            ### Bucket attributes

            |attribute|expected value|type|
            |---------|:------------:|----|
            db.approval_board|digit|string
            db.completion_board|digit|string
            db.createdby|Character Object|evennia character object
            db.denial_board|digit|string
            db.due_timeout|integer|int
            db.group|string|string
            db.hash|unique md5().hexdigest hash object|string
            db.locked|boolean|bool
            db.num_completed_jobs|integer|int
            db.num_approved_jobs|integer|int
            db.num_denied_jobs|integer|int
            db.num_of_jobs|integer|int
            db.resolution_time|integer|int
            db.percent_complete|percentage float|float
            db.total_jobs|integer|int
            db.valid_actions|action list|list
            db.valid_settings|settings list|dictionary of strings
            db.default_notification|code + string|string


            To test I need to create a bucket
            try to create a bucket that already exists
            try to set all attributes on a bucket
            try to retrieve all attributes on a bucket
            try to delete buckets
        """
        pass
