
import unittest
from evennia.commands.default.tests import EvenniaTest
from evennia.utils import create
from cmdjobs import CmdJobs
from cmdbuckets import CmdBuckets
import jobutils as ju
from jobs_settings import ERROR_PRE, SUCC_PRE, TEST_PRE, SYSTEM
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
        """set up test buckets"""
        super(EvenniaTest, self).setUp()
        self.bucket = Bucket()
        self.buckets = []
        self.bucket.create(bucket="Code", desc="Test bucket")
        self.buckets.append(self.bucket)

    def tearDown(self):
        """remove buckets"""
        super(EvenniaTest, self).tearDown()
        for bucket in Bucket.objects.all():
            del bucket

    def test_bucket_create_pass(self):
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

        #Load variables for testing
        correct = bucket, desc = "Jamie", "Test bucket."
        attributes =(db.approval_board, db.completion_board, db.createdby,
                     db.denial_board, db.due_timeout, db.group, db.hash,
                     db.locked, db.num_completed_jobs, db.num_approved_jobs,
                     db.num_denied_jobs, db.num_of_jobs, db.resolution_time,
                     db.percent_complete, db.total_jobs, db.valid_actions,
                     db.valid_settings, db.default_notification, Bucket)
        types = (string, string, DefaultCharacter, string, int,
                 string, string, bool, int, int, int, int, int,
                 float, int, list, dict, string)

        # Parameters for bucket creation - test again after creation for exists failure
        x_exit_status, x_sysmsg = SUCC_PRE, "Bucket: {0} created".format(ju.decorate(bucket))
        bucket_created_pass = x_exit_status + x_sysmsg
        # Incorrect parameters for bucket creation
        x_exit_status, x_sysmsg = ERROR_PRE, "Bucket: {0} already exists".format(ju.decorate(bucket))
        bucket_exists_failure = x_exit_status + x_sysmsg

        # Bucket creation and loading of responses
        buckets = correct, correct
        msgs = ppass, fail

        for bucket in buckets:
            res = self.Bucket.create(bucket=bucket, desc=desc)
            a_exit_status = res.pop("code")
            a_sysmsg = res.pop("sysmsg")
            actual = a_exit_status + a_sysmsg
            expected = msgs[buckets.index(bucket)]
            assertEqual(expected, actual)


    def test_jobids(self):
        print(Bucket.jobids())



class TestJob(EvenniaTest):
    """Test the Job portion of the system"""
    # Job = Job()
    # Bucket = Bucket()

    def setUp(self):
        """create bucket objects to write to and a job object to test against"""
        super(EvenniaTest, self).setUp()
        self.bucket_names = ["Code", "Build", "RP"]
        self.buckets = []
        self.jobs=[]

        # create Buckets
        for bucket in self.bucket_names:
            b = create.create_channel(
                 bucket,
                 desc="Test {0} Bucket".format(bucket),
                 typeclass=Bucket
            )
            self.buckets.append(b)
        bucket = "Code"
        title = "Test job"
        msg = "This is a test job that will be held on the {0} bucket.".format(bucket)
        # Create the Job
        self.test_job = Job().create(bucket, title, msg)["job"]
        self.jobs.append(self.test_job)

    def tearDown(self):
        """Delete all jobs and buckets"""
        super(EvenniaTest, self).tearDown()

        for job in Job.objects.all():
            del job
        for bucket in Bucket.objects.all():
            del bucket

    def test_create_job_pass(self):
        """test creation of job with correct parameters"""
        # Expected output
        bucket, title, msgtext = "Code", "Test message", "This is a test of the job creation system."

        x_exit_status = SUCC_PRE
        x_msg = "Job: {0} created".format(ju.decorate(title))
        expected = x_exit_status + x_msg

        # Actual output
        res = Job().create(bucket, title, msgtext)
        a_exit_status = res.pop("exit_status")
        a_msg = res.pop("msg")
        actual = a_exit_status + a_msg
        self.assertEqual(expected,actual)

    def test_create_job_fail(self):
        """test creation of job with incorrect parameters"""
        bucket, title, msgtext = "Non-existant Bucket", "Test message", "This is a test of the job creation system."

        x_exit_status = ERROR_PRE
        x_msg = "{0} is not a valid bucket".format(bucket.capitalize())
        expected = x_exit_status + x_msg

        # Actual output
        res = Job().create(bucket.capitalize(), title, msgtext)
        a_exit_status = res.pop("exit_status")
        a_msg = res.pop("msg")
        actual = a_exit_status + a_msg
        self.assertEqual(expected,actual)
        pass

    def test_create_CmdJobs_pass(self):
        """test creation of job with correct parameters"""
        # Expected output
        expected = SUCC_PRE + "Job: {0} created".format(ju.decorate(title))
        # Actual output
        strings = "Code", "Test message", "This is a test of the job creation system."
        actual = cmdjobs_create_job(strings)
        self.assertEqual(expected,actual)

    def test_create_CmdJobs_fail_bad_bucket(self):
        """test creation of job with bad bucket"""
        # Expected output
        expected = ERROR_PRE  + "Bucket: {0} already exists".format(ju.decorate(strings[0]))
        # Actual output
        strings = ("Flump", "Whizbang", "Floobar")
        actual = cmdjobs_create_job(strings)
        self.assertEqual(expected,actual)

    def test_create_CmdJobs_fail_(self):
        # Todo: Fix create_CmdJobs_Fail_bad_syntax
        """test creation of job with incorrect parameters"""
        strings = ("Flump", "Whizbang", "Floobar")
        # Expected output
        expected = ERROR_PRE  + "Bucket: {0} already exists".format(ju.decorate(strings[0]))
        # Actual output
        actual = cmdjobs_create_job(strings)
        self.assertEqual(expected,actual)

    # Todo: def test_per_player_actions
    def test_assign_job(self):
        """test assigning a job"""
        pass

    def cmdjobs_create_job(self, strings=(None, None, None)):
        """test creation of job with incorrect parameters"""
        # Testing _creation
        # Import and load vars
        from cmdjobs import CmdJobs
        bucket, title, msgtext = strings
        job = CmdJobs()
        job.lhs_obj = bucket
        job.lhs_act = title
        job.rhs = msgtext

        res = job._create()
        status = res.pop("exit_status")
        msg = res.pop("msg")
        ret = exit_status, msg
        return ret
