from app.requests import ValidRequest


class EnrolmentAuthorisationRequest(ValidRequest):
    student_id: str
    course_id: str
    enrolment_id: str
    shared_secret: str
