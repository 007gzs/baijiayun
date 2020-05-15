# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
import time

from . import api
from .base import BaseClient
from ..core.utils import Md5Signer, to_text
from ..storage.cache import BaiJiaYunClientCache
from ..storage.memorystorage import MemoryStorage

logger = logging.getLogger(__name__)
default_storage = MemoryStorage()


class BaiJiaYunClient(BaseClient):
    doc = api.Doc()
    evaluation = api.Evaluation()
    hudong = api.HuDong()
    live = api.Live()
    liveaccount = api.LiveAccount()
    livesetting = api.LiveSetting()
    notice = api.Notice()
    playback = api.PlayBack()
    quiz = api.Quiz()
    room = api.Room()
    roomdata = api.RoomData()
    smallcourse = api.SmallCourse()
    subaccount = api.SubAccount()
    video = api.Video()
    videoaccount = api.VideoAccount()
    videodata = api.VideoData()

    def __init__(self, partner_id, secret_key, private_domain, prefix=None, storage=None, timeout=None):
        super(BaiJiaYunClient, self).__init__(timeout)
        self.partner_id = partner_id
        self.secret_key = secret_key
        self.cache = BaiJiaYunClientCache(storage or default_storage, prefix or self.partner_id)
        self.API_BASE_URL = 'https://{private_domain}.at.baijiayun.com/'.format(private_domain=private_domain)

    @property
    def partner_key(self):
        partner_key = self.cache.partner_key.get()
        if partner_key is None:
            partner_key = self.get_partner_key()
            self.cache.partner_key.set(value=partner_key, ttl=7200)
        return partner_key

    def get_partner_key(self, regenerate=0):
        return self._request(
            'POST',
            '/openapi/partner/createkey',
            data={
                'partner_id': self.partner_id,
                'secret_key': self.secret_key,
                'regenerate': regenerate,
                'timestamp': int(time.time())
            },
            result_processor=lambda x: x['partner_key']
        )

    def get_sign(self, data):
        signer = Md5Signer(delimiter=b'&', key="partner_key=" + self.partner_key)
        for k, v in data.items():
            v = to_text(v)
            if v:
                signer.add_data("%s=%s" % (k, v))
        return signer.signature

    def add_sign(self, data, timestamp_key="timestamp", sign_key="sign"):
        if timestamp_key and timestamp_key not in data:
            data[timestamp_key] = int(time.time())
        data[sign_key] = self.get_sign(data)
        return data

    def _handle_pre_request(self, method, uri, kwargs):
        if method == 'POST':
            data = kwargs.setdefault('data', dict())
            data.update(kwargs.pop('params', dict()))
        else:
            data = kwargs.setdefault('params', dict())
        self.add_sign(data)
        return method, uri, kwargs

    def _handle_request_except(self, e, func, *args, **kwargs):
        # if e.errcode in (33001, 40001, 42001, 40014):
        #     self.cache.access_token.delete()
        #     if self.auto_retry:
        #         return func(*args, **kwargs)
        raise e
