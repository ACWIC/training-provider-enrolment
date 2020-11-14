import abc


class EnrolmentRepo(abc.ABC):
    @abc.abstractmethod
    def create_enrolment_authorisation(self, enrolment_authorisation: dict):
        pass

    @abc.abstractmethod
    def student_exists(self, enrolment_id: str) -> bool:
        pass

    @abc.abstractmethod
    def course_exists(self, enrolment_id: str) -> bool:
        pass
