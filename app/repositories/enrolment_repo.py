import abc


class EnrolmentRepo(abc.ABC):
    @abc.abstractmethod
    def create_enrolment_authorisation(self, enrolment_authorisation: dict):
        """"""

    @abc.abstractmethod
    def student_exists(self, enrolment_id: str) -> bool:
        """"""

    @abc.abstractmethod
    def course_exists(self, enrolment_id: str) -> bool:
        """"""
