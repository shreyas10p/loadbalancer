import requests


class Server(object):
    """docstring for Server"""
    def __init__(self, url,path="/healthcheck",timeout=1):
        self._url = url
        self._path = path
        self._health = True
        self._requestCount = 0
        self._timeout = timeout

    def checkHealth(self):
        try:
            res = requests.get('http://'+self._url+self._path,timeout=self._timeout)
            if(res.status == "ok"):
                self._health = True
            else:
                self._health = False

        except:
            self._health = False

    def __repr__(self):
        return "<Server: {} {} {}>".format(self._url, self._health, self._timeout)
