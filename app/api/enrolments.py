from fastapi import APIRouter, HTTPException

from app.repositories.s3_enrolment_repo import S3EnrolmentRepo
from app.requests.enrolment_authorisation_request import EnrolmentAuthorisationRequest
from app.use_cases import post_enrolment_authorisation as pea

router = APIRouter()
enrolment_repo = S3EnrolmentRepo()


@router.post("/enrolment")
def post_enrolment_request(inputs: EnrolmentAuthorisationRequest):
    """
    This API is used to post a request for Enrolment Authorization which is already
    pre-registered using create enrolment API on the employers end.
    This API requires the enrolment id of the pre-registered enrolment
    so that it can send callbacks against it.
    It also requires the course id to know in which course
    the student should be enrolled and a student id so that
    it can enrol that student in the relevent course.
    It also requires a shared secret which will allow only
    authorised employers to post an authorization request
    Authenticated and Authorised employers use this API
    to POST an enrolment authorisation to the training provider.
    """
    use_case = pea.EnrolmentAuthorisation(enrolment_repo=enrolment_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response.build()
