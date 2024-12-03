from Services.subjectService import SubjectService

class SubjectManagementFacade:
    def __init__(self):
        self.subject_service = SubjectService()

    def create_subject(self, subject_data):
        # Crear la asignatura a través del servicio correspondiente
        return self.subject_service.create_subject(subject_data)

    def get_all_subjects(self):
        # Obtener todas las asignaturas del servicio
        return self.subject_service.get_all_subjects_camps()