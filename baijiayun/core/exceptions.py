# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import six

from .utils import to_binary, to_text


class ApiException(Exception):

    def __init__(self, code, message):
        """
        :param code: Error code
        :param message: Error message
        """
        self.code = code
        self.message = message

    def __str__(self):
        _repr = 'Error code: {code}, message: {message}'.format(code=self.code, message=self.message)
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)

    def __repr__(self):
        _repr = '{klass}({code}, {message})'.format(klass=self.__class__.__name__, code=self.code, message=self.message)
        if six.PY2:
            return to_binary(_repr)
        else:
            return to_text(_repr)


class ClientException(ApiException):
    def __init__(self, code, msg, client=None, request=None, response=None):
        super(ClientException, self).__init__(code, msg)
        self.client = client
        self.request = request
        self.response = response


class ProcessException(ClientException):
    def __init__(self, result, exc, client=None, request=None, response=None):
        super(ProcessException, self).__init__(
            code=-10, msg='结果result_processor处理错误', client=client, request=request, response=response
        )
        self.result = result
        self.exc = exc
