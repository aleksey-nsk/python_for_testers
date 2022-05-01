# -*- coding: utf-8 -*-

import pytest
import requests

from test_rest_api_DataEast.get_token import get_arcgis_token


@pytest.mark.skip(reason="временно")
def test_get_enrich():
    print("\n\n************** Test get enrich ***************")

    # Arrange
    url = "https://geoenrich.arcgis.com/arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/enrich"
    params = {
        "StudyAreas": "[{'geometry':{'x': -117.1956, 'y': 34.0572}}]",
        "token": get_arcgis_token(),
        "f": "pjson",
        "returnGeometry": "false"
    }
    expected_spatial_reference = {
        "wkid": 4326,
        "latestWkid": 4326
    }

    # Act
    response = requests.get(url=url, params=params)
    response_json = response.json()
    print(response_json)

    # Assert
    assert response.status_code == 200
    assert response_json.get("results")[0].get("paramName") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("dataType") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("value").get("version") == "2.0"

    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("TOTPOP") == "Total Population"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("TOTHH") == "Total Households"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("AVGHHSZ") == "Average Household Size"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("TOTMALES") == "Male Population"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("TOTFEMALES") == "Female Population"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("spatialReference") == expected_spatial_reference

    tot_males = response_json.get("results")[0].get("value").get("FeatureSet")[0] \
        .get("features")[0].get("attributes").get("TOTMALES")
    tot_females = response_json.get("results")[0].get("value").get("FeatureSet")[0] \
        .get("features")[0].get("attributes").get("TOTFEMALES")
    tot_pop = tot_males + tot_females
    print("tot_males: " + str(tot_males) + ", tot_females: " + str(tot_females) + ", tot_pop: " + str(tot_pop))
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("features")[0].get("attributes").get("TOTPOP") == tot_pop


@pytest.mark.skip(reason="временно")
def test_post_enrich():
    print("\n\n************** Test post enrich **************")

    # Arrange
    url = "https://geoenrich.arcgis.com/arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/enrich"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    study_areas = '[{"attributes":{"SITE_INDEX":0},"geometry":{"x":-13046064.348570734,"y":4036493.910258787,"spatialReference":{"wkid":102100}}}]'
    f = "pjson"
    return_geometry = "false"
    params = {
        "studyAreas": study_areas,
        "token": get_arcgis_token(),
        "f": f,
        "returnGeometry": return_geometry
    }

    # Act
    response = requests.post(url=url, headers=headers, params=params)
    response_json = response.json()
    print(response_json)

    # Assert
    assert response.status_code == 200
    assert response_json.get("results")[0].get("paramName") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("dataType") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("value").get("version") == "2.0"

    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("TOTPOP") == "Total Population"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("TOTHH") == "Total Households"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("AVGHHSZ") == "Average Household Size"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("TOTMALES") == "Male Population"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("fieldAliases").get("TOTFEMALES") == "Female Population"

    tot_males = response_json.get("results")[0].get("value").get("FeatureSet")[0] \
        .get("features")[0].get("attributes").get("TOTMALES")
    tot_females = response_json.get("results")[0].get("value").get("FeatureSet")[0] \
        .get("features")[0].get("attributes").get("TOTFEMALES")
    tot_pop = tot_males + tot_females
    print("tot_males: " + str(tot_males) + ", tot_females: " + str(tot_females) + ", tot_pop: " + str(tot_pop))
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("features")[0].get("attributes").get("TOTPOP") == tot_pop


@pytest.mark.skip(reason="временно")
def test_post_enrich_fail():
    print("\n\n*********** Test post enrich fail ************")
    print("Required parameter 'studyAreas' is missed")

    # Arrange
    url = "https://geoenrich.arcgis.com/arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/enrich"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    f = "pjson"
    return_geometry = "false"
    params = {
        "token": get_arcgis_token(),
        "f": f,
        "returnGeometry": return_geometry
    }
    error_expected = {
        "code": 10010017,
        "message": "Required parameter 'studyareas' is not specified or empty.",
        "details": []
    }

    # Act
    response = requests.post(url=url, headers=headers, params=params)
    response_json = response.json()
    print(response_json)

    # Assert
    assert response.status_code == 200
    assert response_json.get("results")[0].get("paramName") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("dataType") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("value").get("version") == "2.0"
    assert response_json.get("results")[0].get("value").get("FeatureSet") == []
    assert response_json.get("error") == error_expected
