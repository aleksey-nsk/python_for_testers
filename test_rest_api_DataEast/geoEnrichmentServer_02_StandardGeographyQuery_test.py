# -*- coding: utf-8 -*-

import pytest
import requests

from test_rest_api_DataEast.get_token import get_arcgis_token


@pytest.mark.skip(reason="временно")
def test_geography_levels_us():
    print("\n\n********** Test geography levels US **********")

    # Arrange
    domen = "https://geoenrich.arcgis.com/"
    url = domen + "arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/StandardGeographyLevels/US/census"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    app_id = "busanalystonline"
    lang_code = "en-us"
    add_services_info = "true"
    f = "pjson"
    params = {
        "appID": app_id,
        "langCode": lang_code,
        "addServicesInfo": add_services_info,
        "token": get_arcgis_token(),
        "f": f
    }

    # Act
    response = requests.post(url=url, headers=headers, params=params)
    response_json = response.json()
    print(response_json)

    # Assert
    assert response.status_code == 200
    assert response_json.get("geographyLevels")[0].get("countryID") == "US"
    assert response_json.get("geographyLevels")[0].get("countryName") == "United States"
    assert response_json.get("geographyLevels")[0].get("hierarchies")[0].get("wholeCountryLevel") == "US.WholeUSA"
    assert response_json.get("geographyLevels")[0].get("hierarchies")[0].get("wholeCountryGeographyId") == "01"
