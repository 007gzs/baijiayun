# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class PlayBack(BaseAPI):
    """
    回放
    """

    def get_basic_info(
            self,
            room_id,
            session_id=None,
    ):
        """
        查询直播回放信息

        :param room_id: 教室号
        :param session_id: 序列号（针对长期房间才会用到）
        """
        return self._post(
            '/openapi/playback/getBasicInfo',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'session_id': session_id,
            }),
        )

    def get_list(
            self,
            product_type,
            page,
            page_size,
            crop_video=0,
            room_id=123456,
    ):
        """
        获取回放列表
        获取回放列表，列表按回放的生成时间倒序排列。

        :param product_type: 1:教育直播，2，小班课，3：双师，4，企业直播
        :param page: 页码，从1开始
        :param page_size: 每一页返回的条数，不得超过1000
        :param crop_video: 是否返回 裁剪视频的回放，0：否 1：是
        :param room_id: 教室号
        """
        return self._post(
            '/openapi/playback/getList',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'page': page,
                'page_size': page_size,
                'crop_video': crop_video,
                'room_id': room_id,
            }),
        )

    def get_player_token(
            self,
            room_id,
            expires_in,
            session_id=None,
    ):
        """
        获取回放token
        获取回放的播放token，服务端获取token后传给客户端，客户端就可以使用该token播放视频

        :param room_id: 房间号
        :param expires_in: 过期时间，以秒为单位。如果传0则表示不过期
        :param session_id: 序列号（针对长期房间才会用到）
        """
        return self._post(
            '/openapi/playback/getPlayerToken',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'session_id': session_id,
                'expires_in': expires_in,
            }),
        )

    def get_player_token_batch(
            self,
            room_ids,
            expires_in,
    ):
        """
        批量获取回放token

        :param room_ids: 短期房间传{room_id}，长期房间传{room_id}-{session_id}，多个回放用英文逗号分隔，如：17110879095169,1711087909231-201711281
        :param expires_in: 过期时间，以秒为单位。如果传0则表示不过期
        """
        return self._post(
            '/openapi/playback/getPlayerTokenBatch',
            optionaldict({
                'partner_id': self.partner_id,
                'room_ids': room_ids,
                'expires_in': expires_in,
            }),
        )

    def get_session_list(
            self,
            room_id,
    ):
        """
        获取长期房间云录制的序列号列表
        该接口用于获取一个长期直播间云录制里所有的序列号。 对于长期房间，云录制功能可以将一个直播间录制成多个回放。每个回放对应的房间号相同，但有不同的序列号。 播放回放时，可通过教室号+序列号来播放。

        :param room_id: 房间号
        """
        return self._post(
            '/openapi/playback/getSessionList',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def set_publish_status(
            self,
            room_id,
            status,
            session_id=None,
    ):
        """
        设置回放发布状态
        该接口用于设置回放的发布状态。默认情况下，回放转码成功后会自动发布。

        :param room_id: 回放教室号
        :param status: 发布状态 1:发布 2:屏蔽
        :param session_id: 长期房间的序列号，普通房间不需要传
        """
        return self._post(
            '/openapi/playback/setPublishStatus',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'session_id': session_id,
                'status': status,
            }),
            result_processor=lambda x: x['status']
        )

    def delete(
            self,
            room_id,
            session_id=None,
            version=None,
    ):
        """
        删除回放

        :param room_id: 教室号
        :param session_id: 序列号（针对长期房间才会用到）
        :param version: 版本号（针对裁剪回放才会用到）
        """
        return self._post(
            '/openapi/playback/delete',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'session_id': session_id,
                'version': version,
            }),
        )

    def update(
            self,
            room_id,
            name,
            session_id=None,
    ):
        """
        更新回放名称
        更新回放视频名称

        :param room_id: 教室号
        :param name: 回放名称
        :param session_id: 序列号（针对长期房间才会用到）
        """
        return self._post(
            '/openapi/playback/update',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'session_id': session_id,
                'name': name,
            }),
        )

    def get_crop_list(
            self,
            room_id,
            product_type=0,
            session_id=None,
            page=1,
            page_size=100,
    ):
        """
        获取裁剪回放列表
        返回包含裁剪链接的回放列表

        :param room_id: 教室号
        :param product_type: 1:教育直播，2，小班课，3：双师，4，企业直播
        :param session_id: 序列号（默认0，长期房间必须传此值）
        :param page: 页码，从1开始，默认值是1
        :param page_size: 每页获取的记录条数，默认100，最大值不能超过1000
        """
        return self._post(
            '/openapi/playback/getCropList',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'room_id': room_id,
                'session_id': session_id,
                'page': page,
                'page_size': page_size,
            }),
        )

    def set_main_version(
            self,
            room_id,
            version,
            session_id=None,
    ):
        """
        设置回放主版本
        设置回放的主版本，一般在有裁剪回放的时候设置

        :param room_id: 教室号
        :param version: 版本号
        :param session_id: 序列号（默认0，长期房间必须传此值）
        """
        return self._post(
            '/openapi/playback/setMainVersion',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'session_id': session_id,
                'version': version,
            }),
        )

    def get_playback_ppt_url_list(
            self,
            room_id,
            date=None,
    ):
        """
        获取ppt转成的pdf的路径列表
        该接口用于获取ppt转成的pdf的路径（备注：仅支持在pro环境的账号）

        :param room_id:
        :param date:
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/playback/getPlaybackPptUrlList',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'date': date,
            }),
        )

    def get_playback_ppt_url(
            self,
            room_id,
            session_id=None,
    ):
        """
        获取ppt转成的pdf具体路径
        该接口用于获取ppt转成的pdf的具体路径（备注：仅支持在pro环境的账号）

        :param room_id:
        :param session_id: session_id
        """
        return self._post(
            '/openapi/playback/getPlaybackPptUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'session_id': session_id,
            }),
        )

    def replace_playback(
            self,
            type,
            source_room_id,
            target_room_id,
            source_session_id=None,
            source_version=None,
            is_replace_main=None,
            target_session_id=None,
            target_version=None,
    ):
        """
        替换回放
        该接口用于替换掉有问题的回放或新增一个回放 源回放(source) 替换 目标回放(target)

        :param type: 类型 1:替换 2:新增
        :param source_room_id: 源回放 room_id
        :param target_room_id: 目标回放 room_id
        :param source_session_id: 源回放 session_id （长期教室传）
        :param source_version: 源回放版本
        :param is_replace_main: 是否替换成主版本 0:否 1:是
        :param target_session_id: 目标回放 session_id （长期教室传）
        :param target_version: 目标回放版本
        """
        return self._post(
            '/openapi/playback/replacePlayback',
            optionaldict({
                'partner_id': self.partner_id,
                'type': type,
                'source_room_id': source_room_id,
                'source_session_id': source_session_id,
                'source_version': source_version,
                'is_replace_main': is_replace_main,
                'target_room_id': target_room_id,
                'target_session_id': target_session_id,
                'target_version': target_version,
            }),
        )
