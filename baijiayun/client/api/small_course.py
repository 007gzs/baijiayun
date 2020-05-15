# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class SmallCourse(BaseAPI):
    """
    小班课
    """

    def get_daily_cost(
            self,
            product_type,
            start_date,
            end_date,
    ):
        """
        获取小班课账号每天消费记录
        获取一段时间内小班课账号每天消费记录

        :param product_type: 产品线类型（老账号填0 新账号填2）
        :param start_date: 开始日期
        :param end_date: 结束日期
        """
        if isinstance(start_date, datetime.date):
            start_date = start_date.strftime('%Y-%m-%d')
        if isinstance(end_date, datetime.date):
            end_date = end_date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/small_course/getDailyCost',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'start_date': start_date,
                'end_date': end_date,
            }),
            result_processor=lambda x: x['cost']
        )

    def get_room_cost(
            self,
            product_type,
            date,
    ):
        """
        获取小班课指定日期各教室消费记录

        :param product_type: 产品线类型（老账号填0 新账号填2）
        :param date: 日期
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/small_course/getRoomCost',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'date': date,
            }),
            result_processor=lambda x: x['room_cost']
        )

    def get_user_cost(
            self,
            product_type,
            date,
            room_id,
    ):
        """
        获取小班课指定教室各学员消费详情

        :param product_type: 产品线类型（老账号填0 新账号填2）
        :param date: 日期
        :param room_id: 直播间 id
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/small_course/getUserCost',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'date': date,
                'room_id': room_id,
            }),
        )
