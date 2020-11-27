from unittest import mock

from fastapi.testclient import TestClient

from app.domain.entities.enrolment_authorisation import EnrolmentAuthorisation
from app.main import app
from app.responses import FailureType, ResponseFailure, ResponseSuccess, SuccessType
from tests.test_data.data_provider import DataProvider

test_data = DataProvider()
client = TestClient(app)


@mock.patch("app.use_cases.post_enrolment_authorisation.EnrolmentAuthorisation")
def test_post_enrolment_success_created(use_case):
    code = SuccessType.CREATED
    message = "The enrolment has been created."
    use_case().execute.return_value = ResponseSuccess(
        value=test_data.sample_enrolment_auth,
        type=code,
        message=message,
    )

    data = test_data.sample_enrolment_auth_req
    response = client.post("/enrolment", data=data.json())
    json_result = response.json()
    enrolment_auth = EnrolmentAuthorisation(**json_result.get("value"))

    use_case().execute.assert_called_with(data)
    assert response.status_code == SuccessType.CREATED.value
    assert enrolment_auth == test_data.sample_enrolment_auth
    assert json_result.get("message") == message


@mock.patch("app.use_cases.post_enrolment_authorisation.EnrolmentAuthorisation")
def test_post_enrolment_failure(use_case):
    message = "Error"
    use_case().execute.return_value = ResponseFailure.build_from_resource_error(
        message=message,
    )

    data = test_data.sample_enrolment_auth_req
    response = client.post("/enrolment", data=data.json())

    assert response.status_code == FailureType.RESOURCE_ERROR.value
    assert response.json() == {"detail": "RESOURCE_ERROR: " + message}
