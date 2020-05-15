# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from .base import BaseAPI


class Notice(BaseAPI):
    """
    公告
    """
    def get_room_notice_list(
            self,
            room_id,
            product_type=0,
    ):
        """
        查看教室公告

        :param room_id: 教室号
        :param product_type: 1大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/notice/getRoomNoticeList',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'product_type': product_type,
            }),
        )

    def assign_room_notice(
            self,
            room_id,
            notice_ids,
            product_type=0,
    ):
        """
        绑定教室公告

        :param room_id: 教室号
        :param notice_ids: 逗号分开的id
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/notice/assignRoomNotice',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'notice_ids': notice_ids,
                'product_type': product_type,
            }),
        )

    def batch_delete_room_notice(
            self,
            room_id,
            notice_ids,
            product_type=0,
    ):
        """
        删除教室公告

        :param room_id: 教室号
        :param notice_ids: 逗号分开的id
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/notice/batchDeleteRoomNotice',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'notice_ids': notice_ids,
                'product_type': product_type,
            }),
        )
