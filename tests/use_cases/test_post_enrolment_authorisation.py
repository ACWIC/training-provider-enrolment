"""
These tests evaluate (and document) the business logic.
"""
from unittest import mock

from app.repositories.enrolment_repo import EnrolmentRepo
from app.requests.enrolment_authorisation_request import EnrolmentAuthorisationRequest
from app.responses import FailureType, SuccessType
from app.use_cases.post_enrolment_authorisation import PostEnrolmentAuthorisationRequest
from tests.test_data.data_provider import DataProvider

test_data = DataProvider()


def test_create_new_enrolment_authorisation_success():
    """
    When creating a new enrollment authorisation,
    if everything goes according to plan,
    the response type should be "Success".
    """
    repo = mock.Mock(spec=EnrolmentRepo)
    enrolment_auth = test_data.sample_enrolment_auth

    repo.create_enrolment_authorisation.return_value = enrolment_auth

    request = EnrolmentAuthorisationRequest(course_id="123", student_id="abc")
    use_case = PostEnrolmentAuthorisationRequest(enrolment_repo=repo)
    response = use_case.execute(request)

    assert response.type == SuccessType.CREATED


def test_create_new_enrolment_authorisation_failure():
    """
    When creating a new enrollment authorisation,
    if there is some kind of error,
    the response type should be "ResourceError".
    """
    repo = mock.Mock(spec=EnrolmentRepo)

    repo.create_enrolment_authorisation.side_effect = Exception()

    request = test_data.sample_enrolment_auth_req
    use_case = PostEnrolmentAuthorisationRequest(enrolment_repo=repo)
    response = use_case.execute(request)

    assert response.type == FailureType.RESOURCE_ERROR
