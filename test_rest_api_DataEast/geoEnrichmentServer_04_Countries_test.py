# -*- coding: utf-8 -*-

import requests

from test_rest_api_DataEast.get_token import get_arcgis_token


def test_geoenrichment_countries():
    print("\n\n******** Test: GeoEnrichment Countries *******")

    # Arrange
    domen = "https://geoenrich.arcgis.com/"
    url = domen + "arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/Countries"
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
    default_extent_expected = {
        "xmin": 19.2627565462,
        "ymin": 39.6444975717,
        "xmax": 21.0578285374,
        "ymax": 42.6610482403,
        "spatialReference": {
            "wkid": 4326,
            "latestWkid": 4326
        }
    }

    # Act
    response = requests.post(url=url, headers=headers, params=params)
    response_json = response.json()
    print(response_json)

    # Assert
    assert response.status_code == 200
    assert response_json.get("countries")[0].get("id") == "AL"
    assert response_json.get("countries")[0].get("name") == "Albania"
    assert response_json.get("countries")[0].get("abbr3") == "ALB"
    assert response_json.get("countries")[0].get("altName") == "ALBANIA"
    assert response_json.get("countries")[0].get("continent") == "Europe"
    assert response_json.get("countries")[0].get("distanceUnits") == "Kilometers"
    assert response_json.get("countries")[0].get("esriUnits") == "esriKilometers"
    assert response_json.get("countries")[0].get("defaultExtent") == default_extent_expected
