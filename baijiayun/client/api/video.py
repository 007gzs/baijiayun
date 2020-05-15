# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class Video(BaseAPI):
    """
    视频
    """

    def get_upload_url(
            self,
            file_name,
            definition,
            audio_with_view=0,
            format=None,
            encrypt=None,
            use_https=0,
    ):
        """
        获取视频/音频上传地址
        通过此接口，可以初始化一个视频/音频，并获取上传地址。

        :param file_name: 文件名
        :param definition: 目标清晰度(16:标清 1:高清 2:超清 4:720p 8:1080p 多种清晰度用英文逗号分隔)
        :param audio_with_view: 是否作为音频处理 0：否 1：是
        :param format: 转码格式（1:mp4 2:flv 4:m3u8 多种格式用英文逗号分隔）默认是3种格式都转
        :param encrypt: 是否生成加密格式视频/音频1:是 2:否（该功能需要申请加密视频/音频的权限，开通加密视频/音频权限后，默认都会加密）
        :param use_https: 是否使用https上传地址，默认不使用
        """
        return self._post(
            '/openapi/video/getUploadUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'file_name': file_name,
                'definition': definition,
                'audio_with_view': audio_with_view,
                'format': format,
                'encrypt': encrypt,
                'use_https': use_https,
            }),
        )

    def get_resume_upload_url(
            self,
            video_id,
            use_https=0,
    ):
        """
        获取断点续传地址
        视频分片上传时，如果只上传了一部分中止了，可以通过此接口获取续传的地址，已上传的那部分不用再上传。

        :param video_id: 视频id
        :param use_https: 是否使用https上传地址，默认不使用
        """
        return self._post(
            '/openapi/video/getResumeUploadUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'use_https': use_https,
            }),
        )

    def get_status(
            self,
            video_id,
    ):
        """
        查询视频转码状态

        :param video_id: 视频id
        """
        return self._post(
            '/openapi/video/getStatus',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
            }),
        )

    def get_info(
            self,
            video_id,
    ):
        """
        获取指定ID视频信息
        获取指定ID的视频信息（不包括已删除的视频）

        :param video_id: 视频id
        """
        return self._post(
            '/openapi/video/getInfo',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
            }),
        )

    def get_image(
            self,
            video_id,
    ):
        """
        获取指定ID视频截图
        获取指定ID的视频截图（不包括已删除的视频）

        :param video_id: 视频id
        """
        return self._post(
            '/openapi/video/getImage',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
            }),
        )

    def remove_definition(
            self,
            video_id,
            definition,
            type="1",
    ):
        """
        清除指定清晰度的转码文件
        该接口可以清除指定清晰度的视频文件，以减少占用的存储空间

        :param video_id: 视频id
        :param definition: 目标清晰度(16:标清 1:高清 2:超清 4:720p 8:1080p 多种清晰度用英文逗号分隔)
        :param type: 目标类型(1:mp4 2:flv 4:m3u8 8:encrypt 多种类型用英文逗号分隔)
        """
        return self._post(
            '/openapi/video/removeDefinition',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'definition': definition,
                'type': type,
            }),
        )

    def transcode_again(
            self,
            video_id,
            definition,
            format=None,
    ):
        """
        视频二次转码
        如果视频初始化时只指了某几种清晰度，后面需要转其它清晰度，则可以调用此接口

        :param video_id: 视频id
        :param definition: 目标清晰度(16:标清 1:高清 2:超清 4:720p 8:1080p 多种清晰度用英文逗号分隔)
        :param format: 转码格式（1:mp4 2:flv 4:m3u8 多种格式用英文逗号分隔）默认是3种格式都转
        """
        return self._post(
            '/openapi/video/transcodeAgain',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'definition': definition,
                'format': format,
            }),
        )

    def update(
            self,
            video_id,
            name,
    ):
        """
        更新视频信息
        该接口可以更新视频信息，目前只有名称可以更新

        :param video_id: 视频id
        :param name: 视频名称
        """
        return self._post(
            '/openapi/video/update',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'name': name,
            }),
            result_processor=lambda x: x['video_id']
        )

    def delete(
            self,
            video_id,
    ):
        """
        删除视频

        :param video_id: 视频id
        """
        return self._post(
            '/openapi/video/delete',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
            }),
            result_processor=lambda x: x['video_id']
        )

    def get_category_list(
            self,
    ):
        """
        获取所有分类
        该接口用于获取所有的分类信息
        """
        return self._post(
            '/openapi/video/getCategoryList',
            optionaldict({
                'partner_id': self.partner_id,
            }),
            result_processor=lambda x: x['list']
        )

    def get_category_info(
            self,
            category_id=0,
    ):
        """
        获取指定ID分类信息
        该接口用于获取分类信息

        :param category_id: 分类ID
        """
        return self._post(
            '/openapi/video/getCategoryInfo',
            optionaldict({
                'partner_id': self.partner_id,
                'category_id': category_id,
            }),
        )

    def add_category(
            self,
            name,
            parent_id=0,
    ):
        """
        添加分类
        该接口用于添加分类

        :param name: 分类名称
        :param parent_id: 父分类ID，如果添加的是一级分类，则可以填0或不传
        """
        return self._post(
            '/openapi/video/addCategory',
            optionaldict({
                'partner_id': self.partner_id,
                'name': name,
                'parent_id': parent_id,
            }),
        )

    def delete_category(
            self,
            category_id,
    ):
        """
        删除分类
        该接口用于删除分类，若该分类下有视频，则不可删除

        :param category_id: 分类ID
        """
        return self._post(
            '/openapi/video/deleteCategory',
            optionaldict({
                'partner_id': self.partner_id,
                'category_id': category_id,
            }),
            result_processor=lambda x: x['category_id']
        )

    def get_category_video(
            self,
            category_id,
            page_size=20,
            page=1,
    ):
        """
        获取指定分类下的视频
        获取指定分类下的视频，如果是一级分类ID，则返回挂在该分类下的视频及挂在该分类下的二级分类里的视频

        :param category_id: 分类ID
        :param page_size: 每页条数，不得超过100，默认值20
        :param page: 页码，默认1
        """
        return self._post(
            '/openapi/video/getCategoryVideo',
            optionaldict({
                'partner_id': self.partner_id,
                'category_id': category_id,
                'page_size': page_size,
                'page': page,
            }),
        )

    def set_video_category(
            self,
            video_id,
            category_id,
    ):
        """
        设置视频分类
        设置一个视频的分类

        :param video_id: 视频ID
        :param category_id: 分类ID
        """
        return self._post(
            '/openapi/video/setVideoCategory',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'category_id': category_id,
            }),
        )

    def get_player_token(
            self,
            video_id,
            expires_in,
    ):
        """
        获取播放器token
        获取视频播放token，服务端获取token后传给客户端，客户端就可以使用该token播放视频

        :param video_id: 视频ID
        :param expires_in: 过期时间，以秒为单位。如果传0则表示不过期
        """
        return self._post(
            '/openapi/video/getPlayerToken',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'expires_in': expires_in,
            }),
            result_processor=lambda x: x['token']
        )

    def get_player_token_batch(
            self,
            video_ids,
            expires_in,
    ):
        """
        批量获取播放器token
        获取视频播放token，服务端获取token后传给客户端，客户端就可以使用该token播放视频

        :param video_ids: 多个视频ID以英文逗号分隔
        :param expires_in: 过期时间，以秒为单位。如果传0则表示不过期
        """
        return self._post(
            '/openapi/video/getPlayerTokenBatch',
            optionaldict({
                'partner_id': self.partner_id,
                'video_ids': video_ids,
                'expires_in': expires_in,
            }),
        )

    def get_url(
            self,
            video_id,
            format=None,
            expires_in=None,
    ):
        """
        获取转码后视频/音频地址
        该接口用于获取转码后视频的不同清晰度播放地址，以及视频宽高等信息。

        :param video_id: 视频ID
        :param format: 视频格式，可选值有：mp4/m3u8/flv/encrypt，默认是mp4，encrypt表示加密格式，账号开启了点播加密功能才会有该格式的视频
        :param expires_in: 视频失效时间，单位为秒，默认是12小时
        """
        return self._post(
            '/openapi/video/getUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'format': format,
                'expires_in': expires_in,
            }),
        )

    def set_publish_status(
            self,
            video_id,
            status,
    ):
        """
        设置视频发布状态
        该接口用于设置视频的发布状态。默认情况下，视频转码成功后会自动发布。

        :param video_id: 视频ID
        :param status: 发布状态 1:发布 2:屏蔽
        """
        return self._post(
            '/openapi/video/setPublishStatus',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'status': status,
            }),
            result_processor=lambda x: x['status']
        )

    def get_share_url(
            self,
            video_id,
    ):
        """
        获取视频分享地址
        该接口用于获取视频的分享地址，包含iframe方式、js方式、flash方式

        :param video_id: 视频ID
        """
        return self._post(
            '/openapi/video/getShareUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
            }),
        )

    def get_video_list(
            self,
            page_size=20,
            page=1,
            create_time=None,
    ):
        """
        获取点播视频列表
        获取点播的视频列表

        :param page_size: 每页条数，不得超过1000，默认值20
        :param page: 页码，默认1
        :param create_time: 默认不加上时间筛选
        """
        if isinstance(create_time, datetime.datetime):
            create_time = create_time.strftime('%Y-%m-%d %H:%M:%S')
        return self._post(
            '/openapi/video/getVideoList',
            optionaldict({
                'partner_id': self.partner_id,
                'page_size': page_size,
                'page': page,
                'create_time': create_time,
            }),
        )
