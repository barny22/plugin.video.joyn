def get_etags_data(request_hash):

    etags_data = cache.get_json('ETAGS').get('data')
    if etags_data is None:
        etags_data = {}

    etag_data = etags_data.get(request_hash, None)
    if etag_data is not None:
        etags_data[request_hash].update({'access': int(time())})
        cache.set_json('ETAGS', etags_data)
        cache_data = cache._get('ETAGS', request_hash + '.etag')
        data = cache_data.get('data', None) if cache_data else None
        if data is not None:
            etag_data.update({'data': data})
            return etag_data
    return None
