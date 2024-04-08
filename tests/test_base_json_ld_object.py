#
# This software is Copyright ©️ 2020 The University of Southern California. All Rights Reserved.
# Permission to use, copy, modify, and distribute this software and its documentation for educational, research and non-profit purposes, without fee, and without a written agreement is hereby granted, provided that the above copyright notice and subject to the full license file found in the root of this software deliverable. Permission to make commercial use of this software may be obtained by contacting:  USC Stevens Center for Innovation University of Southern California 1150 S. Olive Street, Suite 2300, Los Angeles, CA 90115, USA Email: accounting@stevens.usc.edu
#
# The full terms of this copyright and license should always be found in the root directory of this software deliverable as "license.txt" and if these terms are not found with this software, please contact the USC Stevens Center for the full license.
#
from py_learning_standards import (
    BaseJSONLDObject,
    Competency,
    LearningResource,
    NAMESPACE_CEASN,
    NAMESPACE_DCT,
    NAMESPACE_LRMI,
    NAMESPACE_SDO,
    create_en_us_lang_string,
)
import pytest


@pytest.mark.parametrize(
    "dictionary,expected_object,object_type",
    [
        ({}, BaseJSONLDObject(), BaseJSONLDObject),
        (
            {"id": "penguins", "@type": "testType"},
            BaseJSONLDObject(id="penguins", type="testType"),
            BaseJSONLDObject,
        ),
        (
            {"@type": "ceasn:Competency", "ceasn:ctid": "testId"},
            Competency(type="ceasn:Competency", ctid="testId"),
            Competency,
        ),
        (
            {
                "@type": "ceasn:Competency",
                "ceasn:ctid": "testId",
                "ceasn:competencyText": create_en_us_lang_string("testText"),
            },
            Competency(
                type="ceasn:Competency",
                ctid="testId",
                competency_text=create_en_us_lang_string("testText"),
            ),
            Competency,
        ),
        (
            {
                "@type": "LearningResource",
                f"{NAMESPACE_DCT}:description": "penguins",
                f"{NAMESPACE_DCT}:title": "test title",
                f"{NAMESPACE_LRMI}:teaches": [
                    {
                        f"{NAMESPACE_CEASN}:ctid": "testctid",
                        f"{NAMESPACE_CEASN}:competencyText": create_en_us_lang_string(
                            "test text"
                        ),
                        "relevance": 0.5,
                    },
                ],
                f"{NAMESPACE_SDO}:duration": "PT60S",
                "complexity": 0.75,
            },
            LearningResource(
                type="LearningResource",
                description="penguins",
                title="test title",
                teaches=[
                    Competency(
                        ctid="testctid",
                        competency_text=create_en_us_lang_string("test text"),
                        relevance=0.5,
                    )
                ],
                duration="PT60S",
                complexity=0.75,
            ),
            LearningResource,
        ),
    ],
)
def test_serialization(dictionary, expected_object, object_type):
    result = object_type.from_dict(dictionary)
    assert result == expected_object
    copy = result.to_dict_no_nones()
    assert copy == dictionary
