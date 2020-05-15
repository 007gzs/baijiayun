# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class LiveAccount(BaseAPI):
    """
    直播账号
    """

    def get_hour_peak_user(
            self,
            date,
            product_type=0,
    ):
        """
        获取账号一天中每小时最高并发量
        该接口用于获取账号一天中每小时的并发量

        :param date: 查询日期，格式如：2017-12-12
        :param product_type: 1:教育直播 2：小班课 4：企业直播
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/live_account/getHourPeakUser',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'date': date,
            }),
            result_processor=lambda x: x['peak_user']
        )

    def get_day_peak_user(
            self,
            start_date,
            end_date,
            product_type=0,
    ):
        """
        查询账号一段时间内每天的最高并发量
        该接口用于获取账号一段时间内每天的最高并发量

        :param start_date: 查询起始日期，格式如：2017-12-12
        :param end_date: 查询结束日期，格式如：2017-12-28
        :param product_type: 1:教育直播 2：小班课 4：企业直播
        """
        if isinstance(start_date, datetime.date):
            start_date = start_date.strftime('%Y-%m-%d')
        if isinstance(end_date, datetime.date):
            end_date = end_date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/live_account/getDayPeakUser',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'start_date': start_date,
                'end_date': end_date,
            }),
            result_processor=lambda x: x['peak_user']
        )

    def set_class_callback_url(
            self,
            url,
    ):
        """
        1. 设置直播上下课事件回调地址
        该接口用于设置直播中上下课事件的回调地址。 并不是直播生成回放的回调，直播生成回放的回调请参考 回放服务端API接口文档

        :param url: 回调地址，必须是http(s)://开头
        """
        return self._post(
            '/openapi/live_account/setClassCallbackUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'url': url,
            }),
            result_processor=lambda x: x['url']
        )

    def get_class_callback_url(
            self,
    ):
        """
        2. 查询直播上下课回调地址
        该接口用于查询直播上下课的回调地址
        """
        return self._post(
            '/openapi/live_account/getClassCallbackUrl',
            optionaldict({
                'partner_id': self.partner_id,
            }),
            result_processor=lambda x: x['url']
        )

    def get_partner_daily_cost(
            self,
            start_date,
            end_date,
            product_type=0,
    ):
        """
        查询直播账号每天使用的人次
        该接口用于获取按人次/时长计费的账号，每天消耗的人次

        :param start_date: 开始日期，格式如：2018-02-01
        :param end_date: 结束日期，格式如：2018-02-15
        :param product_type: 1:教育直播 4：企业直播
        """
        if isinstance(start_date, datetime.date):
            start_date = start_date.strftime('%Y-%m-%d')
        if isinstance(end_date, datetime.date):
            end_date = end_date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/live_account/getPartnerDailyCost',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'start_date': start_date,
                'end_date': end_date,
            }),
            result_processor=lambda x: x['cost']
        )

    def get_all_room_cost(
            self,
            date,
            product_type=0,
    ):
        """
        查询直播账号指定日期中各教室使用的人次
        该接口用于获取指定日期内每个教室使用的人次明细

        :param date: 查询日期，格式如：2018-02-01
        :param product_type: 1:教育直播 4：企业直播
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/live_account/getAllRoomCost',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'date': date,
            }),
            result_processor=lambda x: x['room_cost']
        )
