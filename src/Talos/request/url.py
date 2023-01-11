from typing import Optional, Iterable


class Url:

    def __init__(self,
                 protocol=None,
                 host=None,
                 port=None,
                 path=None,
                 path_params=None,
                 query_params=None,
                 fragment=None):

        self.__url = None
        self.__protocol: Optional[str] = protocol
        self.__host: Optional[str] = host
        self.__port: Optional[str] = port
        self.__path: Optional[str] = path
        self.__path_params: Optional[dict] = path_params
        self.__query_params: Optional[dict] = query_params
        self.__fragment: Optional[str] = fragment

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @url.deleter
    def url(self):
        del self.__url

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, value):
        self.__protocol = value

    @protocol.deleter
    def protocol(self):
        del self.__protocol

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @host.deleter
    def host(self):
        del self.__host

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = value

    @port.deleter
    def port(self):
        del self.__port

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @path.deleter
    def path(self):
        del self.__path

    @property
    def path_params(self):
        return self.__path_params

    @path_params.setter
    def path_params(self, value):
        self.__path_params = value

    @path_params.deleter
    def path_params(self):
        del self.__path_params

    @property
    def query_params(self):
        return self.__query_params

    @query_params.setter
    def query_params(self, value):
        self.__query_params = value

    @query_params.deleter
    def query_params(self):
        del self.__query_params

    @property
    def fragment(self):
        return self.__fragment

    @fragment.setter
    def fragment(self, value):
        self.__fragment = value

    @fragment.deleter
    def fragment(self):
        del self.__fragment

    def _add_protocol(self):
        self.url = "".join(filter(lambda x: x if x is not None else "", [self.url, self.protocol]))

    def _add_host(self):
        self.url = "://".join(filter(lambda x: x if x is not None else "", [self.url, self.host]))

    def _add_port(self):
        self.url = ":".join(filter(lambda x: x if x is not None else "", [self.url, self.port]))

    def _add_path_params(self):
        if self.path_params:
            path_with_params = [self.path.replace(f"{{{key}}}", value) for key, value in self.path_params.items()][0]
        else:
            path_with_params = self.path
        self.url = "/".join([self.url, path_with_params])

    def _add_query_params(self):
        if self.query_params:
            query_with_params = '&'.join(
                list(map(lambda x: x[0] + "=" + x[1], list(zip(self.query_params.keys(), self.query_params.values())))))
            self.url = self.url + "?" + query_with_params

    def _add_fragment(self):
        self.url = "#".join(filter(lambda x: x if x is not None else "", [self.url, self.fragment]))

    def build(self):
        self._add_protocol()
        self._add_host()
        self._add_port()
        self._add_path_params()
        self._add_query_params()
        self._add_fragment()
        return self.url
