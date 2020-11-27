from fastapi import APIRouter, HTTPException

from app.repositories.s3_enrolment_repo import S3EnrolmentRepo
from app.requests.enrolment_authorisation_request import EnrolmentAuthorisationRequest
from app.use_cases import post_enrolment_authorisation as pea

router = APIRouter()
enrolment_repo = S3EnrolmentRepo()


@router.post("/enrolment")
def post_enrolment_request(inputs: EnrolmentAuthorisationRequest):
    """
    Authenticated and Authorised employers use this API
    to POST an enrolment authorisation to the training provider.
    """
    use_case = pea.EnrolmentAuthorisation(enrolment_repo=enrolment_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response.build()
