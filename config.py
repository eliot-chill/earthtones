import json

def loadConfig():
    data = {}
    with open('config.json') as config_file:
        data.update(json.load(config_file))
        config_file.close()
    return data


def getPassword():
    return loadConfig()["dbPass"]


if __name__ == "__main__":
    print(getPassword())


