"""
These tests evaluate the interaction with the backing PaaS.
The are testing the encapsulation of the "impure" code
(in a functional sense),
the repos should return pure domain objects
of the appropriate type.
"""
import datetime
from unittest import mock

from app.config import settings
from app.repositories.s3_enrolment_repo import S3EnrolmentRepo
from tests.test_data.data_provider import DataProvider

test_data = DataProvider()


@mock.patch("boto3.client")
def test_s3_initialisation(boto_client):
    """
    Ensure the S3Enrolmentrepo makes a boto3 connection.
    """
    S3EnrolmentRepo()
    boto_client.assert_called_once()


@mock.patch("app.utils.random.Random.get_uuid")
@mock.patch("boto3.client")
def test_create_enrolment_authorisation(boto_client, get_uuid):
    """
    Ensure the create_enrolment_authorisation returns an object with OK data
    and that an appropriate boto3 put call was made.
    """
    repo = S3EnrolmentRepo()
    settings.ENROLMENT_AUTHORISATION_BUCKET = "some-bucket"
    enrolment_authorisation_req = test_data.sample_enrolment_auth_req

    get_uuid.return_value = test_data.sample_enrolment_auth_id
    with mock_datetime_now(test_data.sample_created, datetime):
        enrolment_auth = repo.create_enrolment_authorisation(
            enrolment_authorisation_req.dict()
        )

    assert enrolment_auth.enrolment_auth_id == test_data.sample_enrolment_auth_id
    assert enrolment_auth.student_id == test_data.sample_student_id
    assert enrolment_auth.course_id == test_data.sample_course_id
    assert enrolment_auth.status == test_data.sample_status
    assert enrolment_auth.shared_secret == test_data.sample_shared_secret
    assert enrolment_auth.enrolment_id == test_data.sample_enrolment_id

    boto_client.return_value.put_object.assert_called_once_with(
        Body=bytes(enrolment_auth.json(), "utf-8"),
        Key=f"enrolment_authorisations/{test_data.sample_enrolment_auth_id}.json",
        Bucket="some-bucket",
    )


def mock_datetime_now(target, datetime_module):
    """Override ``datetime.datetime.now()`` with a custom target value.
    This creates a new datetime.datetime class, and alters its now()/utcnow()
    methods.
    Returns:
        A mock.mock.mock.patch context, can be used as a decorator or in a with.
    """
    real_datetime_class = datetime.datetime

    class DatetimeSubclassMeta(type):
        """We need to customize the __instancecheck__ method for isinstance().
        This must be performed at a metaclass level.
        """

        @classmethod
        def __instancecheck__(mcs, obj):
            return isinstance(obj, real_datetime_class)

    class BaseMockedDatetime(real_datetime_class):
        @classmethod
        def now(cls, tz=None):
            return target.replace(tzinfo=tz)

        @classmethod
        def utcnow(cls):
            return target

    # Python2 & Python3-compatible metaclass
    MockedDatetime = DatetimeSubclassMeta("datetime", (BaseMockedDatetime,), {})

    return mock.patch.object(datetime_module, "datetime", MockedDatetime)
