# -*- coding: utf-8 -*-

import requests

from test_rest_api_DataEast.get_token import get_arcgis_token


def test_data_layers_naics():
    print("\n\n********** Test: Data Layers (NAICS) *********")

    # Arrange
    domen = "https://geoenrich.arcgis.com/"
    url = domen + "arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/DataLayers/US/US.DB_BUS/Fields/NAICS"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    app_id = "busanalystonline"
    lang_code = "en-us"
    f = "pjson"
    params = {
        "appID": app_id,
        "langCode": lang_code,
        "token": get_arcgis_token(),
        "f": f
    }
    description_expected = "North American Industry Classification System code. Standard codes are 6 characters " \
                           "and Data Axle adds 2 characters to create a proprietary 8 character code. This field " \
                           "is associated with the primary SIC code only."

    # Act
    response = requests.post(url=url, headers=headers, params=params)
    response_json = response.json()
    print(response_json)

    # Assert
    assert response.status_code == 200
    assert response_json.get("field").get("name") == "NAICS"
    assert response_json.get("field").get("alias") == "NAICS Code"
    assert response_json.get("field").get("type") == "esriFieldTypeString"
    assert response_json.get("field").get("length") == 8
    assert response_json.get("field").get("role") == "Industry"
    assert response_json.get("field").get("description") == description_expected
    assert response_json.get("field").get("searchable") == True
    assert response_json.get("field").get("filtering") == True
