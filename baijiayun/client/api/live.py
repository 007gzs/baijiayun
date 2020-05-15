# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from .base import BaseAPI


class Live(BaseAPI):
    """
    直播
    """

    def get_live_status(
            self,
            room_id,
    ):
        """
        获取直播教室当前的上下课状态

        :param room_id: 教室号
        """
        return self._post(
            '/openapi/live/getLiveStatus',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
            result_processor=lambda x: x['status']
        )

    def get_teacher_online_status(
            self,
            room_id,
    ):
        """
        获取当前老师是否在教室的状态

        :param room_id: 教室号
        """
        return self._post(
            '/openapi/live/getTeacherOnlineStatus',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
            result_processor=lambda x: x['status']
        )

    def get_user_count(
            self,
            room_id,
    ):
        """
        获取当前时间教室人数

        :param room_id: 教室号
        """
        return self._post(
            '/openapi/live/getUserCount',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def set_notify(
            self,
            room_id,
            content,
    ):
        """
        设置教室公告

        :param room_id: 教室号
        :param content: 公告信息
        """
        return self._post(
            '/openapi/live/setNotify',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'content': content,
            }),
        )

    def send_chat_message(
            self,
            message_list,
    ):
        """
        发送聊天消息接口
        该接口用于发送聊天消息

        :param message_list: json字符串
        """
        return self._post(
            '/openapi/live/sendChatMessage',
            optionaldict({
                'partner_id': self.partner_id,
                'message_list': message_list,
            }),
        )

    def stop_cloud_record(
            self,
            room_id,
    ):
        """
        停止直播教室的云端录制
        该接口用于操作停止直播教室的云端录制

        :param room_id:
        """
        return self._post(
            '/openapi/live/stopCloudRecord',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def trans_cloud_record(
            self,
            room_id,
    ):
        """
        直播教室的云端录制生成回放
        该接口用于操作直播教室的云端录制生成回放

        :param room_id:
        """
        return self._post(
            '/openapi/live/transCloudRecord',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )
