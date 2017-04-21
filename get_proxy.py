import requests


class Client:

    def __init__(self):
        self._session = requests.Session()
        self.proxies = None

    def set_proxy_pool(self, proxies, auth=None, https=True):
        """Randomly choose a proxy for every GET/POST request        
        :param proxies: list of proxies, like ["ip1:port1", "ip2:port2"]
        :param auth: if proxy needs auth
        :param https: default is True, pass False if you don't need https proxy
        """
        from random import choice

        if https:
            self.proxies = [{'http': 'http://' + p, 'https': 'https://' + p} for p in proxies]
        else:
            self.proxies = [{'http': 'http://' + p} for p in proxies]

        def get_with_random_proxy(url, **kwargs):
            proxy = choice(self.proxies)
            kwargs['proxies'] = proxy
            if auth:
                kwargs['auth'] = auth
            return self._session.original_get(url, **kwargs)

        def post_with_random_proxy(url, *args, **kwargs):
            proxy = choice(self.proxies)
            kwargs['proxies'] = proxy
            if auth:
                kwargs['auth'] = auth
            return self._session.original_post(url, *args, **kwargs)

        self._session.original_get = self._session.get
        self._session.get = get_with_random_proxy
        self._session.original_post = self._session.post
        self._session.post = post_with_random_proxy

    def remove_proxy_pool(self):
        self.proxies = None
        self._session.get = self._session.original_get
        self._session.post = self._session.original_post
        del self._session.original_get
        del self._session.original_post

    # You can define whatever operations using self._session