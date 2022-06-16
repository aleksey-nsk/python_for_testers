import configparser
import logging.config

import requests

logging.config.fileConfig('../log.conf')
log = logging.getLogger('simple')


def get_arcgis_token():
    path = "../token/config.ini"

    # Читаем из конфиг-файла
    config = configparser.ConfigParser()
    config.read(path)
    token = config.get("Settings", "token")

    return token


def test_get_example():
    log.debug("************** Test get example **************")

    # Arrange
    url = "https://postman-echo.com/get"
    parameters = {
        "foo1": "bar1",
        "foo2": "bar2"
    }

    # Act
    response = requests.get(url=url, params=parameters)
    response_json = response.json()

    # Assert
    assert response.status_code == 200
    assert response_json.get("url") == "https://postman-echo.com/get?foo1=bar1&foo2=bar2"
    assert response_json.get("args").get("foo1") == "bar1"
    assert response_json.get("args").get("foo2") == "bar2"
    assert response_json.get("args") == parameters


def test_post_example():
    log.debug("************** Test post example *************")

    # Arrange
    url = "https://jsonplaceholder.typicode.com/posts"
    body = {
        "title": "First POST request",
        "body": "I hope, it’s gonna be work",
        "userId": 12345
    }
    headers = {
        "Content-Type": "application/json"
    }

    # Act
    response = requests.post(url=url, json=body, headers=headers)
    response_json = response.json()

    # Assert
    assert response.status_code == 201
    assert response_json.get("title") == "First POST request"
    assert response_json.get("body") == "I hope, it’s gonna be work"
    assert response_json.get("userId") == 12345
    assert response_json.get("id") is not None


def test_get_enrich():
    log.debug("************** Test get enrich ***************")

    # Arrange
    url = "https://geoenrich.arcgis.com/arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/enrich"
    parameters = {
        "StudyAreas": "[{'geometry':{'x': -117.1956, 'y': 34.0572}}]",
        "token": get_arcgis_token(),
        "f": "pjson",
        "returnGeometry": "false"
    }

    # Act
    response = requests.get(url=url, params=parameters)
    response_json = response.json()

    # Assert
    assert response.status_code == 200
    assert response_json.get("results")[0].get("paramName") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("dataType") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("value").get("version") == "2.0"

    assert response_json.get("results")[0].get("value").get("FeatureSet")[0].get("fieldAliases").get(
        "TOTPOP") == "Total Population"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0].get("fieldAliases").get(
        "TOTHH") == "Total Households"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0].get("fieldAliases").get(
        "AVGHHSZ") == "Average Household Size"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0].get("fieldAliases").get(
        "TOTMALES") == "Male Population"
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0].get("fieldAliases").get(
        "TOTFEMALES") == "Female Population"

    tot_males = response_json.get("results")[0].get("value").get("FeatureSet")[0].get("features")[0].get(
        "attributes").get("TOTMALES")
    tot_females = response_json.get("results")[0].get("value").get("FeatureSet")[0].get("features")[0].get(
        "attributes").get("TOTFEMALES")
    tot_pop = tot_males + tot_females
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0].get("features")[0].get("attributes").get(
        "TOTPOP") == tot_pop


def test_post_enrich():
    log.debug("************** Test post enrich **************")

    # Arrange
    url = "https://geoenrich.arcgis.com/arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/enrich"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    study_areas = '[{"attributes":{"SITE_INDEX":0},"geometry":{"x":-13046064.348570734,"y":4036493.910258787, "spatialReference":{"wkid":102100}}}]'
    parameters = {
        "studyAreas": study_areas,
        "token": get_arcgis_token(),
        "f": "pjson",
        "returnGeometry": "false"
    }

    # Act
    response = requests.post(url=url, headers=headers, params=parameters)
    response_json = response.json()
    log.debug(response_json)

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
    assert response_json.get("results")[0].get("value").get("FeatureSet")[0] \
               .get("features")[0].get("attributes").get("TOTPOP") == tot_pop


def test_post_enrich_fail():
    log.debug("*********** Test post enrich fail ************")
    log.debug("Required parameter 'studyAreas' is missed")

    # Arrange
    url = "https://geoenrich.arcgis.com/arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/enrich"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    parameters = {
        "token": get_arcgis_token(),
        "f": "pjson",
        "returnGeometry": "false"
    }
    error_expected = {
        "code": 10010017,
        "message": "Required parameter 'studyareas' is not specified or empty.",
        "details": []
    }

    # Act
    response = requests.post(url=url, headers=headers, params=parameters)
    response_json = response.json()
    log.debug(response_json)

    # Assert
    assert response.status_code == 200
    assert response_json.get("results")[0].get("paramName") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("dataType") == "GeoEnrichmentResult"
    assert response_json.get("results")[0].get("value").get("version") == "2.0"
    assert response_json.get("results")[0].get("value").get("FeatureSet") == []
    assert response_json.get("error") == error_expected


def test_geography_levels_us():
    log.debug("********** Test geography levels US **********")

    # Arrange
    domen = "https://geoenrich.arcgis.com/"
    url = domen + "arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/StandardGeographyLevels/US/census"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    parameters = {
        "appID": "busanalystonline",
        "langCode": "en-us",
        "addServicesInfo": "true",
        "token": get_arcgis_token(),
        "f": "pjson"
    }

    # Act
    response = requests.post(url=url, headers=headers, params=parameters)
    response_json = response.json()

    # Assert
    assert response.status_code == 200
    assert response_json.get("geographyLevels")[0].get("countryID") == "US"
    assert response_json.get("geographyLevels")[0].get("countryName") == "United States"
    assert response_json.get("geographyLevels")[0].get("hierarchies")[0].get("wholeCountryLevel") == "US.WholeUSA"
    assert response_json.get("geographyLevels")[0].get("hierarchies")[0].get("wholeCountryGeographyId") == "01"


def test_data_layers_naics():
    log.debug("********** Test: Data Layers (NAICS) *********")

    # Arrange
    domen = "https://geoenrich.arcgis.com/"
    url = domen + "arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/DataLayers/US/US.DB_BUS/Fields/NAICS"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    parameters = {
        "appID": "busanalystonline",
        "langCode": "en-us",
        "token": get_arcgis_token(),
        "f": "pjson"
    }
    description_expected = "North American Industry Classification System code. Standard codes are 6 characters " \
                           "and Data Axle adds 2 characters to create a proprietary 8 character code. This field " \
                           "is associated with the primary SIC code only."

    # Act
    response = requests.post(url=url, headers=headers, params=parameters)
    response_json = response.json()

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


def test_geoenrichment_countries():
    log.debug("******** Test: GeoEnrichment Countries *******")

    # Arrange
    domen = "https://geoenrich.arcgis.com/"
    url = domen + "arcgis/rest/services/World/geoenrichmentserver/Geoenrichment/Countries"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    parameters = {
        "appID": "busanalystonline",
        "langCode": "en-us",
        "token": get_arcgis_token(),
        "f": "pjson"
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
    response = requests.post(url=url, headers=headers, params=parameters)
    response_json = response.json()

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
