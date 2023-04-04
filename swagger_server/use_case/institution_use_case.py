from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData

class InstitutionUseCase:
    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def get_institution(self):
        """
            Lista de instituciones
        """

        data_response = []
        institutions = self.institution_repository.get_institution()

        for i in institutions:
            data_response.append(ResponseInstitutionData(id = i.id, name = i.name, description = i.description, address = i.address))

        response = ResponseInstitution(code = 0, message = 'proceso exitoso', data = data_response)

        return response
    
    def get_institution_by_id(self, institution_id):
        data_response = []
        institution = self.institution_repository.get_institution_by_id(institution_id)
        
        for i in institution:
            data_response.append(ResponseInstitutionData(id = i.id, name = i.name, description = i.description, address = i.address))

        response = ResponseInstitution(code = 0, message = 'proceso exitoso', data = data_response)

        return response

    def add_institution(self, body):
        data_response = []
        institution = self.institution_repository.add_institution(body)

        for i in institution:
            data_response.append(ResponseInstitutionData(id = i.id, name = i.name, description = i.description, address = i.address))
        
        response = ResponseInstitution(code = 0, message = 'proceso exitoso', data = data_response)

        return response

    def update_institution(self, body):
        data_response = []
        institution = self.institution_repository.update_institution(body)

        for i in institution:
            data_response.append(ResponseInstitutionData(id = i.id, name = i.name, description = i.description, address = i.address, updated_user = i.updated_user, updated_at = i.updated_at))
        
        response = ResponseInstitution(code = 0, message = 'proceso exitoso', data = data_response)

        return response
    
    def delete_institution(self, institution_id):
        self.institution_repository.delete_institution(institution_id)
        
        response = ResponseInstitution(code = 0, message = 'proceso exitoso', data = [])

        return response