# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiOamMegRef(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, meg_uuid=None):  # noqa: E501
        """TapiOamMegRef - a model defined in OpenAPI

        :param meg_uuid: The meg_uuid of this TapiOamMegRef.  # noqa: E501
        :type meg_uuid: str
        """
        self.openapi_types = {
            'meg_uuid': str
        }

        self.attribute_map = {
            'meg_uuid': 'meg-uuid'
        }

        self._meg_uuid = meg_uuid

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamMegRef':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.MegRef of this TapiOamMegRef.  # noqa: E501
        :rtype: TapiOamMegRef
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meg_uuid(self):
        """Gets the meg_uuid of this TapiOamMegRef.

        none  # noqa: E501

        :return: The meg_uuid of this TapiOamMegRef.
        :rtype: str
        """
        return self._meg_uuid

    @meg_uuid.setter
    def meg_uuid(self, meg_uuid):
        """Sets the meg_uuid of this TapiOamMegRef.

        none  # noqa: E501

        :param meg_uuid: The meg_uuid of this TapiOamMegRef.
        :type meg_uuid: str
        """

        self._meg_uuid = meg_uuid
