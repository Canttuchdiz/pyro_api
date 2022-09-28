from imports import *

class Commands:

    @staticmethod
    def usernameCheck(username):
        jsonData = Http.get_request(url=endpoints['username'] + str(username))
        return jsonData
