# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.connectivity_service import ConnectivityService  # noqa: F401,E501
from tapi_server import util


class GetConnectivityServiceListRPCOutputSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, service: List[ConnectivityService]=None):  # noqa: E501
        """GetConnectivityServiceListRPCOutputSchema - a model defined in Swagger

        :param service: The service of this GetConnectivityServiceListRPCOutputSchema.  # noqa: E501
        :type service: List[ConnectivityService]
        """
        self.swagger_types = {
            'service': List[ConnectivityService]
        }

        self.attribute_map = {
            'service': 'service'
        }

        self._service = service

    @classmethod
    def from_dict(cls, dikt) -> 'GetConnectivityServiceListRPCOutputSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get-connectivity-service-listRPC_output_schema of this GetConnectivityServiceListRPCOutputSchema.  # noqa: E501
        :rtype: GetConnectivityServiceListRPCOutputSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service(self) -> List[ConnectivityService]:
        """Gets the service of this GetConnectivityServiceListRPCOutputSchema.


        :return: The service of this GetConnectivityServiceListRPCOutputSchema.
        :rtype: List[ConnectivityService]
        """
        return self._service

    @service.setter
    def service(self, service: List[ConnectivityService]):
        """Sets the service of this GetConnectivityServiceListRPCOutputSchema.


        :param service: The service of this GetConnectivityServiceListRPCOutputSchema.
        :type service: List[ConnectivityService]
        """

        self._service = service