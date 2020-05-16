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

    def __init__(self, partner_id, secret_key, private_domain=None, cache_prefix=None, storage=None, timeout=None):
        super(BaiJiaYunClient, self).__init__(timeout)
        self.partner_id = partner_id
        self.secret_key = secret_key
        self.private_domain = private_domain
        self.cache = BaiJiaYunClientCache(storage or default_storage, cache_prefix or self.partner_id)
        if private_domain is not None:
            self.API_BASE_URL = 'https://%s.at.baijiayun.com/' % private_domain

    @property
    def partner_key(self):
        return self.get_partner_key()

    def get_partner_key(self, regenerate=0, force=False):
        partner_key = self.cache.partner_key.get()
        if partner_key is None or force:
            partner_key = self._request(
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
            self.cache.partner_key.set(value=partner_key, ttl=7200)
        return partner_key

    def get_sign(self, data):
        signer = Md5Signer(delimiter=b'&', key="partner_key=" + self.partner_key)
        for k, v in data.items():
            v = to_text(v)
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
        raise e

    def get_web_sign(self, room_id, user_number, user_name, user_role, user_avatar='', group_id=None):
        """
        直播进教室签名的计算

        :param room_id: 教室号
        :param user_number: 用户number号，必须为数字,不带符号的正整数，最大支持19位
        :param user_name: 用户昵称
        :param user_role: 用户角色 0:学生 1:老师 2:助教
        :param user_avatar: 用户头像url ，必须传http/https开头的绝对路径
        :param group_id: 分组号
        """
        data = {
            'room_id': room_id,
            'user_number': user_number,
            'user_name': user_name,
            'user_role': user_role,
            'user_avatar': user_avatar
        }
        if group_id is not None:
            data['group_id'] = group_id
        return self.get_sign(data)

    def check_sign(self, data, check_timestamp_second=300):
        """
        回调接口签名验证

        :param data: 请求全部数据
        :param check_timestamp_second: 时间戳与服务器时间误差范围，传0不验证时间戳
        """
        assert isinstance(data, dict)
        if 'sign' not in data:
            return False
        if check_timestamp_second > 0:
            if 'timestamp' not in data or abs(data['timestamp'] - time.time()) > check_timestamp_second:
                return False
        data = data.copy()
        sign = data.pop('sign', None)
        return sign == self.get_sign(data)
