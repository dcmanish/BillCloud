import configparser

config=configparser.RawConfigParser()
print(config)
config.read(".\\Configurations\\config.ini")



class Readconfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserid():
        username = config.get('common info', 'userid')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
