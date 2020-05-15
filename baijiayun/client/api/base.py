# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class BaseAPI(object):

    API_BASE_URL = None

    def __init__(self, client=None):
        self._client = client

    def _request(self, url, data=None, **kwargs):
        if self.API_BASE_URL and 'api_base_url' not in kwargs:
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.request(url, data, **kwargs)

    @property
    def partner_id(self):
        return self._client.partner_id

    def _get(self, uri, params=None, **kwargs):
        return self._client.get(uri, params=params, **kwargs)

    def _post(self, uri, data=None, params=None, **kwargs):
        return self._client.post(uri, data=data, params=params, **kwargs)
