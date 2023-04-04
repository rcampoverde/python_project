import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.request_institution_add import RequestInstitutionAdd  # noqa: E501
from swagger_server.models.request_institution_upd import RequestInstitutionUpd  # noqa: E501
from swagger_server import util
from swagger_server.frameworks.db.sqlalchemy import SQLAlchemyClient
from swagger_server.repository.institution_repository import InstitutionRepository
from swagger_server.use_case.institution_use_case import InstitutionUseCase
from flask.views import MethodView

class InstitutionView(MethodView): 
    def __init__(self):
        sqlalchemy_client = SQLAlchemyClient()
        institution_repository = InstitutionRepository(sqlalchemy_client)
        institution_use_case = InstitutionUseCase(institution_repository)
        self.institution_use_case = institution_use_case

    def add_institution(self, body):  # noqa: E501
        """Agrega una nueva institución

        Agrega una nueva institución # noqa: E501

        :param body: Crea una nueva institución
        :type body: dict | bytes

        :rtype: InlineResponse200
        """
        if connexion.request.is_json:
            body = RequestInstitutionAdd.from_dict(connexion.request.get_json())  # noqa: E501

        return self.institution_use_case.add_institution(body)


    def delete_institution(self, institution_id):  # noqa: E501
        """Elimina una institución

        Elimina una institución # noqa: E501

        :param institution_id: Institution id to delete
        :type institution_id: int

        :rtype: InlineResponse200
        """
        return self.institution_use_case.delete_institution(institution_id)


    def get_institution(self):  # noqa: E501
        """Lista instituciones

        Lista instituciones # noqa: E501


        :rtype: InlineResponse200
        """
        return self.institution_use_case.get_institution()

    def get_institution_by_id(self, institution_id):  # noqa: E501
        """Busca una institución por ID

        Busca una institución por ID # noqa: E501

        :param institution_id: Busca una institución por ID
        :type institution_id: int

        :rtype: InlineResponse200
        """
        return self.institution_use_case.get_institution_by_id(institution_id)


    def update_institution(self, body):  # noqa: E501
        """Actualiza una institución existente

        Actualiza una institución existente # noqa: E501

        :param body: Actualiza una institución existente
        :type body: dict | bytes

        :rtype: InlineResponse200
        """
        if connexion.request.is_json:
            body = RequestInstitutionUpd.from_dict(connexion.request.get_json())  # noqa: E501
        
        return self.institution_use_case.update_institution(body)
