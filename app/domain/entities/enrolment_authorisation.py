from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class State(str, Enum):
    NEW = "new"
    INFO_REQUESTED = "info_requested"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    CANCELLED = "cancelled"
    WITHDRAWN = "withdrawn"
    COMPLETED = "completed"


VALID_STATE_CHANGES = (
    (State.NEW, State.ACCEPTED),
    (State.NEW, State.REJECTED),
    (State.NEW, State.INFO_REQUESTED),
    (State.INFO_REQUESTED, State.ACCEPTED),
    (State.INFO_REQUESTED, State.REJECTED),
    (State.INFO_REQUESTED, State.INFO_REQUESTED),
    (State.ACCEPTED, State.CANCELLED),
    (State.ACCEPTED, State.WITHDRAWN),
    (State.ACCEPTED, State.COMPLETED),
)


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
    state: State = State.NEW
