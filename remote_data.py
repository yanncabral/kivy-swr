from kivy.network.urlrequest import UrlRequest
from functools import wraps

def remote_data(url):
    def swr(func):
        cache = dict()

        @wraps(func)
        def memoized_func(*args, **kw):

            def record(req, res):
                if (url not in cache) or res != cache[url][1]:
                    cache[url] = (req, res)
                    func(req = cache[url][0], res=cache[url][1], cached = False, *args, **kw)

            if url in cache:
                func(req = cache[url][0], res=cache[url][1], cached = True,*args, **kw)

            UrlRequest(url, record)

        return memoized_func
    return swr