from app.domain.entities.enrolment_authorisation import EnrolmentAuthorisation
from tests.test_data.data_provider import DataProvider

test_data = DataProvider()


def test_enrolment_authorisation_init():
    """
    Ensure the enrolment_authorisation data matches constructor values
    and the status is appropriately set.
    """
    enrolment_auth = EnrolmentAuthorisation(
        enrolment_auth_id=test_data.sample_enrolment_auth_id,
        student_id=test_data.sample_student_id,
        course_id=test_data.sample_course_id,
        status=test_data.sample_status,
        enrolment_id=test_data.sample_enrolment_id,
        shared_secret=test_data.sample_shared_secret,
        created=test_data.sample_created,
    )

    assert enrolment_auth.enrolment_auth_id == test_data.sample_enrolment_auth_id
    assert enrolment_auth.student_id == test_data.sample_student_id
    assert enrolment_auth.course_id == test_data.sample_course_id
    assert enrolment_auth.status == test_data.sample_status
    assert enrolment_auth.created == test_data.sample_created
    assert enrolment_auth.enrolment_id == test_data.sample_enrolment_id
    assert enrolment_auth.shared_secret == test_data.sample_shared_secret
