from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class EnrolmentStatus(str, Enum):
    lodged = "Lodged"


class EnrolmentAuthorisation(BaseModel):
    enrolment_auth_id: str
    student_id: str
    course_id: str
    status: EnrolmentStatus = EnrolmentStatus.lodged
    enrolment_id: str
    shared_secret: str
    created: datetime
