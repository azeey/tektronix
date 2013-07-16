import requests

class TDS3000Socket(object):
    """Docstring for TDS3000Socket """

    def __init__(self,ip,port=80):
        """Initialize socket

        :ip: IP address
        :port: Port (default=80)

        """
        self.ip = ip
        self.port = port
        self.url = "http://{}:{}/?COMMAND=".format(self.ip, self.port)
        self.r = None

    def request_url(self, data):
        """Prepare request url

        :data: @todo
        :returns: @todo

        """
        return self.url + data

    def write(self, data):
        """@todo: Docstring for write

        :arg1: @todo
        :returns: @todo

        """
        self.r = requests.get(self.request_url(data), stream=True)

    def read(self, size=1):
        """@todo: Docstring for read

        :size: @todo
        :returns: @todo

        """
        return self.r.raw.read(size)

    def ask(self, query):
        """@todo: Docstring for ask

        :cmd: @todo
        :returns: @todo

        """
        r = requests.get(self.request_url(query), stream=True)
        return r.raw.read()

