
import unittest
from evennia.commands.default.tests import EvenniaTest
from evennia.utils import create
from cmdjobs import CmdJobs
from cmdbuckets import CmdBuckets
import jobutils as ju
from jobs_settings import ERROR_PRE, SUCC_PRE, TEST_PRE, SYSTEM
from world.jobs.job import Job
from world.jobs.bucket import Bucket


class TestSuite(unittest.TestSuite):
    """This will run all the tests"""
    def run(self, result, debug=False):
        pass

class TestJgroup(EvenniaTest):
    """Test the Jgroup portion of the system"""

    def setUp(self):
        super(EvenniaTest, self).setUp()
        pass

    def tearDown(self):
        pass

class TestBucket(EvenniaTest):
    """Test the Bucket portion of the system"""

    def setUp(self):
        super(EvenniaTest, self).setUp()
        self.bucket = Bucket()
        self.buckets = []
        self.bucket.create(bucket="Code", desc="Test bucket")
        self.buckets.append(self.bucket)

    def tearDown(self):
        for bucket in Bucket.objects.all():
            del bucket

    def test_bucket_create_pass(self):
        bucket, desc = "Jamie", "Test bucket."
        self.Bucket = Bucket()
        x_exit_status = SUCC_PRE
        x_sysmsg = "Bucket: {0} created".format(ju.decorate(bucket))
        expected = x_exit_status + x_sysmsg
        res = self.Bucket.create(bucket=bucket, desc=desc)
        a_exit_status = res.pop("code")
        a_sysmsg = res.pop("sysmsg")
        actual = a_exit_status + a_sysmsg
        self.assertEqual(expected,actual)

    def test_bucket_create_fail_exists(self):
        self.Bucket = Bucket()
        bucket, desc = "Code", "Test bucket"
        bucket = bucket.capitalize()
        x_exit_status = ERROR_PRE
        x_sysmsg = "Bucket: {0} already exists".format(ju.decorate(bucket))
        expected = x_exit_status + x_sysmsg
        res = self.Bucket.create(bucket=bucket, desc=desc)
        a_exit_status = res.pop("code")
        a_sysmsg = res.pop("sysmsg")
        actual = a_exit_status + a_sysmsg
        self.assertEqual(expected,actual)

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

        for job in self.jobs:
            job.delete()
        for bucket in self.buckets:
            bucket.delete()

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
        # Testing _creation
        # Import and load vars
        from cmdjobs import CmdJobs
        bucket, title, msgtext = "Code", "Test message", "This is a test of the job creation system."
        job = CmdJobs()
        job.lhs_obj = bucket
        job.lhs_act = title
        job.rhs = msgtext

        # Expected output
        x_exit_status = SUCC_PRE
        x_msg = "Job: {0} created".format(ju.decorate(title))
        expected = x_exit_status + x_msg

        # Actual output
        res = job._create()
        a_exit_status = res.pop("exit_status")
        a_msg = res.pop("msg")
        actual = a_exit_status + a_msg
        self.assertEqual(expected,actual)

    def test_create_CmdJobs_fail(self):
        pass


    def test_assign_job(self):
        """test assigning a job"""
        pass

