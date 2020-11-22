import datetime

from app.domain.entities.enrolment_authorisation import EnrolmentAuthorisation
from app.requests.enrolment_authorisation_request import EnrolmentAuthorisationRequest


class DataProvider:
    sample_enrolment_auth: EnrolmentAuthorisation

    sample_uuid = "1dad3dd8-af28-4e61-ae23-4c93a456d10e"
    sample_enrolment_auth_id = "2dad3dd8-af28-4e61-ae23-4c93a456d10e"
    sample_course_id = "3dad3dd8-af28-4e61-ae23-4c93a456d10f"
    sample_student_id = "4dad3dd8-af28-4e61-ae23-4c93a456d10e"
    sample_status = "Lodged"
    sample_enrolment_id = "5dad3dd8-af28-4e61-ae23-4c93a456d10j"
    sample_shared_secret = "6dad3dd8-af28-4e61-ae23-4c93a456d10j"
    date_time_str = "2018-05-29 08:15:27.243860"
    sample_created = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S.%f")

    def __init__(self):
        self.sample_enrolment_auth = EnrolmentAuthorisation(
            enrolment_auth_id=self.sample_enrolment_auth_id,
            student_id=self.sample_student_id,
            course_id=self.sample_course_id,
            enrolment_id=self.sample_enrolment_id,
            shared_secret=self.sample_shared_secret,
            status=self.sample_status,
            created=self.sample_created,
        )

        self.sample_enrolment_auth_req = EnrolmentAuthorisationRequest(
            student_id=self.sample_student_id,
            course_id=self.sample_course_id,
            enrolment_id=self.sample_enrolment_id,
            shared_secret=self.sample_shared_secret,
        )
