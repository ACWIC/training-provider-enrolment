import datetime
from typing import Any

import boto3

from app.config import settings
from app.domain.entities.enrolment_authorisation import EnrolmentAuthorisation
from app.repositories.enrolment_repo import EnrolmentRepo
from app.utils.error_handling import handle_s3_errors
from app.utils.random import Random


class S3EnrolmentRepo(EnrolmentRepo):
    s3: Any

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with handle_s3_errors():
            self.s3 = boto3.client("s3", **settings.s3_configuration)

    def create_enrolment_authorisation(self, enrolment_authorisation: dict):
        enrolment_authorisation["enrolment_auth_id"] = Random.get_uuid()
        enrolment_authorisation["created"] = datetime.datetime.now()
        enrolment_authorisation = EnrolmentAuthorisation(**enrolment_authorisation)
        with handle_s3_errors():
            self.s3.put_object(
                Body=bytes(enrolment_authorisation.json(), "utf-8"),
                Key="enrolment_authorisations/"
                + enrolment_authorisation.enrolment_auth_id
                + ".json",
                Bucket=settings.ENROLMENT_AUTHORISATION_BUCKET,
            )
        return enrolment_authorisation

    def student_exists(self, student_id: str) -> bool:
        try:
            self.s3.get_object(
                Key=f"students/{student_id}.json",
                Bucket=settings.STUDENT_BUCKET,
            )
            return True
        except Exception:
            return False

    def course_exists(self, course_id: str) -> bool:
        try:
            self.s3.get_object(
                Key=f"courses/{course_id}.json",
                Bucket=settings.COURSE_BUCKET,
            )
            return True
        except Exception:
            return False
