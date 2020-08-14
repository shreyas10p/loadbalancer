import requests


#By default server is allowed 10 requests at a time.
class Server(object):
    """docstring for Server"""
    PRIORITY_ALLOTED = []
    def __init__(self, url,priority,path="/healthcheck",timeout=2,allowedRequests =2):
        self._url = url
        self._priority = self.checkAvailablePriority(priority)
        self._path = path
        self._health = True
        self._allowedRequests = allowedRequests
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

    def checkAvailablePriority(self,priority):
        assert priority not in Server.PRIORITY_ALLOTED,"PRIORITY ALREAY ALLOTED"
        return priority

    def __repr__(self):
        return "<Server: {} {} {}>".format(self._url, self._health, self._timeout)
