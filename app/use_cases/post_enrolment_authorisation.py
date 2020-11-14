from pydantic import BaseModel

from app.repositories.enrolment_repo import EnrolmentRepo
from app.requests.enrolment_authorisation_request import EnrolmentAuthorisationRequest
from app.responses import ResponseFailure, ResponseSuccess, SuccessType


class PostEnrolmentAuthorisationRequest(BaseModel):
    enrolment_repo: EnrolmentRepo

    class Config:
        # Pydantic will complain if something (enrolment_repo) is defined
        # as having a non-BaseModel type (e.g. an ABC). Setting this ensures
        # that it will just check that the value isinstance of this class.
        arbitrary_types_allowed = True

    def execute(self, request: EnrolmentAuthorisationRequest):
        try:
            # if not self.enrolment_repo.student_exists(request.student_id):
            #     return ResponseFailure.build_from_validation_error(
            #         message="student_id=" + request.student_id + " is not valid."
            #     )
            # if not self.enrolment_repo.course_exists(request.course_id):
            #     return ResponseFailure.build_from_validation_error(
            #         message="course_id=" + request.course_id + " is not valid."
            #     )
            enrolment_authorisation = (
                self.enrolment_repo.create_enrolment_authorisation(request.dict())
            )
            code = SuccessType.CREATED
            message = "The Enrolment Authorisation Request has been created."
        except Exception as e:
            return ResponseFailure.build_from_resource_error(message=e)

        return ResponseSuccess(
            value=enrolment_authorisation, message=message, type=code
        )
