import configparser


def get_arcgis_token():
    path = "../token/config.ini"
    print("Method get_arcgis_token(). Path: '" + path + "'")

    config = configparser.ConfigParser()
    config.read(path)

    token = config.get("Settings", "token")
    # print("  token: " + token)

    return token
