# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class VideoAccount(BaseAPI):
    """
    视频账户
    """

    def get_account_info(
            self,
    ):
        """
        获取账号套餐使用量
        获取当前账号使用的总存储空间及流量。流量使用情况非实时的，每天统计一次。
        """
        return self._post(
            '/openapi/video_account/getAccountInfo',
            optionaldict({
                'partner_id': self.partner_id,
            }),
        )

    def get_used_flow(
            self,
            start_date,
            end_date,
    ):
        """
        查询账号一段时间内使用的流量
        查询整体账号一段时间内使用的总流量。 注：流量的统计不是实时的，每天统计一次。

        :param start_date: 查询起始日期，时间格式为yyyy-mm-dd，如：2017-08-01
        :param end_date: 查询结束日期，时间格式为yyyy-mm-dd，如：2017-08-01
        """
        if isinstance(start_date, datetime.date):
            start_date = start_date.strftime('%Y-%m-%d')
        if isinstance(end_date, datetime.date):
            end_date = end_date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/video_account/getUsedFlow',
            optionaldict({
                'partner_id': self.partner_id,
                'start_date': start_date,
                'end_date': end_date,
            }),
            result_processor=lambda x: x['flow']
        )

    def set_transcode_callback_url(
            self,
            url,
    ):
        """
        1. 设置转码回调地址（点播和回放）
        该接口用户于设置点播和回放转码回调地址

        :param url: 回调地址，必须是http(s)://开头
        """
        return self._post(
            '/openapi/video_account/setTranscodeCallbackUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'url': url,
            }),
            result_processor=lambda x: x['url']
        )

    def get_transcode_callback_url(
            self,
    ):
        """
        2. 查询转码回调地址（点播和回放）
        该接口用户于查询点播和回放的转码回调地址
        """
        return self._post(
            '/openapi/video_account/getTranscodeCallbackUrl',
            optionaldict({
                'partner_id': self.partner_id,
            }),
            result_processor=lambda x: x['url']
        )
