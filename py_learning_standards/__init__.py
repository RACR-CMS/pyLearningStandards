#
# This software is Copyright ©️ 2020 The University of Southern California. All Rights Reserved. 
# Permission to use, copy, modify, and distribute this software and its documentation for educational, research and non-profit purposes, without fee, and without a written agreement is hereby granted, provided that the above copyright notice and subject to the full license file found in the root of this software deliverable. Permission to make commercial use of this software may be obtained by contacting:  USC Stevens Center for Innovation University of Southern California 1150 S. Olive Street, Suite 2300, Los Angeles, CA 90115, USA Email: accounting@stevens.usc.edu
#
# The full terms of this copyright and license should always be found in the root directory of this software deliverable as "license.txt" and if these terms are not found with this software, please contact the USC Stevens Center for the full license.
#
from dataclasses import dataclass
from typing import Dict, Any, Optional, Type

NAMESPACE_ASN = "asn"
NAMESPACE_CETERMS = "ceterms"
NAMESPACE_CEASN = "ceasn"
NAMESPACE_DCT = "dct"
NAMESPACE_IFLA = "ifla"
NAMESPACE_LMT = "lmt"
NAMESPACE_LRMI = "lrmi"
NAMESPACE_RDFS = "rdfs"
NAMESPACE_SCD = "scd"
NAMESPACE_SDO = "sdo"
NAMESPACE_SKOS = "skos"


@dataclass
class BaseJSONLDObject:

    id: Optional[str] = None
    type: Optional[str] = None

    ID_FIELD_NAME = "id"
    TYPE_FIELD_NAME = "@type"

    @classmethod
    def from_json_ld_dict(cls, json_ld_dict: Dict[str, Any], object_type: Type) -> Any:
        if not issubclass(object_type, BaseJSONLDObject):
            raise RuntimeError("attempting to parse into a non Base JSON Object")
        result = object_type()

        if cls.ID_FIELD_NAME in json_ld_dict.keys():
            result.id = json_ld_dict[cls.ID_FIELD_NAME]
        if cls.TYPE_FIELD_NAME in json_ld_dict.keys():
            result.type = json_ld_dict[cls.TYPE_FIELD_NAME]
        return result

    def to_json_ld_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.id is not None:
            result[self.ID_FIELD_NAME] = self.id
        if self.type is not None:
            result[self.TYPE_FIELD_NAME] = self.type
        return result


@dataclass
class LearningResource(BaseJSONLDObject):

    @classmethod
    def from_json_ld_dict(cls, json_ld_dict: Dict[str, Any], object_type: Type) -> Any:
        result = BaseJSONLDObject.from_json_ld_dict(json_ld_dict, object_type)
        return result

    def to_json_ld_dict(self) -> Dict[str, Any]:
        result = super().to_json_ld_dict()
        return result
