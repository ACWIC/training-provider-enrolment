from app.requests.enrolment_authorisation_request import EnrolmentAuthorisationRequest
from tests.test_data.data_provider import DataProvider

test_data = DataProvider()


def test_enrolment_auth_request():
    """
    When a enrolment_auth_request is instantiated,
    the resulting object should have correct attribute values.
    """
    enrolment_auth_req = EnrolmentAuthorisationRequest(
        student_id=test_data.sample_student_id,
        course_id=test_data.sample_course_id,
    )

    assert enrolment_auth_req.student_id == test_data.sample_student_id
    assert enrolment_auth_req.course_id == test_data.sample_course_id
