from kivy.network.urlrequest import UrlRequest
from functools import wraps
from kivy.storage.jsonstore import JsonStore

cache_global = JsonStore('swr_cache.json')
def RemoteData(url, memory_only=False, *global_args, **global_kwargs):
    def swr(func):

        if memory_only:
            cache = dict()
        else:
            cache = cache_global


        @wraps(func)
        def memoized_func(*args, **kw):

            def callback():

                params = func.__code__.co_varnames
                if isinstance(cache[url], dict):
                    desided_keys = dict(filter(lambda e: e[0] in params, cache[url].items()))
                    func(*args, **kw, **desided_keys)
                else:
                    raise ValueError('Only JSON dict object {} are accepted in swr remote_data.')
                
            def save_cache(req, res):

                if (url not in cache) or res != cache[url]:
                    cache[url] = res
                    callback()

            if url in cache:
                callback()

            UrlRequest(url, save_cache, *global_args, **global_kwargs)

        return memoized_func
    return swr