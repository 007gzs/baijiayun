# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class Room(BaseAPI):
    """
    房间
    """

    def create(
            self,
            title,
            start_time,
            end_time,
            type,
            industry_type=0,
            max_users=0,
            pre_enter_time=None,
            is_long_term=0,
            is_group_live=0,
            template_name=None,
            speak_camera_turnon=None,
            teacher_need_detect_device=None,
            student_need_detect_device=None,
            is_video_main=None,
            m_is_video_main=None,
            is_mock_live=0,
            is_push_live=0,
            is_webrtc_live=None,
            mock_room_id=0,
            mock_session_id=0,
            mock_video_id=0,
            switch_room_role=0,
            enable_share=0,
            enable_group_users_public=0,
            group_admin_permission=0,
            enable_group_chat_public=0,
            new_group_live=0,
            mock_live_record=None,
            enable_weixin_auth=1,
            has_student_raise=0,
            end_delay_time=None,
            class_end_operation=None,
            disable_switch_class=None,
            max_backup_users=0,
            auto_on_stage=0,
            has_foreign_user=None,
            background_attachment=None,
            whiteboard_attachment=None,
            template_type=None,
            enable_cloud_record=None,
    ):
        """
        创建房间

        :param title: 直播课标题，不超过50个字符或汉字，超过部分将进行截取
        :param start_time: 开课时间, unix时间戳（秒）
        :param end_time: 下课时间, unix时间戳（秒）
        :param type: 1:一对一课（老的班型，老账号支持） 2:普通大班课 3:小班课普通版（老的班型，老账号支持）4:小班课 5:双师 6：基础班一对一
        :param industry_type: 0:表示教育 1:表示企业
        :param max_users: 人数限制 大班课/双师班：不传或传0表示不限制。小班课：必传(取值范围1-12)作为台上人数；基础班一对一时，必须传1值
        :param pre_enter_time: 学生可提前进入的时间，单位为秒
        :param is_long_term: 是否是长期房间，0:普通房间(注：普通房间时长小于24小时) 1:长期房间 默认为普通房间（注：需要给账号开通长期房间权限才可以创建长期房间）
        :param is_group_live: 是否是分组直播，0:常规直播 1:分组直播（注：需要给账号开通分组直播权限才可以创建分组直播，必须同时指定参数type为2）2:分组直播-大小班（注：需要权限，参数type须为2）
        :param template_name: 可选值   教育直播：doubleCamera(双摄像头)、classic(经典模板)、triple(三分屏)、single(单视频模板)、liveWall(视频墙)
                                       企业直播：singleVideo（单视频），docAudio（文档加音频），docVideo（文档加视频）
        :param speak_camera_turnon: 学生发言时是否自动开启摄像头 1:开启 2:不开启 默认会开启
        :param teacher_need_detect_device: 老师是否启用设备检测 1:启用 2:不启用 默认不启用
        :param student_need_detect_device: 学生是否启用设备检测 1:启用 2:不启用 默认不启用
        :param is_video_main: 指定PC端是否以视频为主 1:以视频为主 2:以PPT为主 （默认是以ppt为主，该选项只针对三分屏有效）
        :param m_is_video_main: 指定手机H5页面是否以视频为主 1:以视频为主 2:以PPT为主 （默认是以视频为主）
        :param is_mock_live: 是否是伪直播，0:否 1:是（注：需要给账号开通伪直播权限，选择伪直播时，必须要选择mock_video_id或mock_room_id和mock_session_id）
        :param is_push_live: 是否是推流直播，0:常规直播 1:推流直播 默认是常规直播（注：需要给账号开通推流直播的权限）
        :param is_webrtc_live: 是否是webrtc课程,1:是（需要联系百家云配置webrtc类型才可使用）
        :param mock_room_id: 伪直播关联的回放教室号
        :param mock_session_id: 伪直播关联的回放教室session_id（针对长期房间）
        :param mock_video_id: 伪直播关联的点播视频ID
        :param switch_room_role: 分组直播，大小班切换控制角色 1：大班老师控制，2 小班老师控制
        :param enable_share: 是否允许APP分享 1:允许 2:不允许 0或不传则使用默认值，默认是允许
        :param enable_group_users_public: 分组课堂/线上双师 成员名单数据权限 0:成员只看组内权限 1:成员可看全部权限 0或不传则使用默认值，默认是成员只看组内权限
        :param group_admin_permission: 分组/线上双师 助教查看答题数据权限 0:助教查看组内答题数据 1:助教查看全部数据 0或不传则使用默认值，默认是助教查看组内答题数据
        :param enable_group_chat_public: 分组直播/线上双师 成员聊天数据权限 0:成员只看组内权限 1:成员可看全部权限 0或不传则使用默认值，默认是成员只看组内权限
        :param new_group_live: 是否分组，0:常规直播 1:分组课堂（注：需要给账号开通相关权限才可以创建分组直播，必须同时指定参数type为2）2:线上双师（注：需要权限，参数type须为2）
        :param mock_live_record: 伪直播自动录制 1：是，0：否
        :param enable_weixin_auth: 是否启用微信授权 1：启用，2：不启用
        :param has_student_raise: 有无学生上麦，仅在webrtc班型上使用此参数 0：无，1：有
        :param end_delay_time: 课程预设的结束时间后可以拖堂的时间，到时间会强制下课，单位（秒），0不强制，大于0生效,最大不可超过3600秒（一小时），设置后课程不能修改结束时间
        :param class_end_operation: 大班下课后操作，0:回到小班,1:全员下课 默认0
        :param disable_switch_class: 课中是否允许切班，1:不允许,0:允许 默认0，如果不允许，配置该字段需要将switch_room_role设置为1，否则不生效
        :param max_backup_users: 小班课1vNvM班型，台下学生数量限制，最大支持300
        :param auto_on_stage: 小班课1vNvM班型，台下学生是否自动上台； 0：不是，1：是
        :param has_foreign_user: 是否有海外用户，如果有海外用户请传此参数； 1：否，2：是
        :param background_attachment: 小班课教室背景图(文件不参与签名的计算)，图片文件
        :param whiteboard_attachment: 小班课教室白板(文件不参与签名的计算)，图片文件
        :param template_type: 小班课模板类型 可传1,2,3；1为第一套模板；2为第二套模板；3为一对一模板，需申请开通
        :param end_delay_time: 课程预设的结束时间后可以拖堂的时间，到时间会强制下课，单位（秒），0不强制，大于0生效,最大不可超过7200秒（两小时）
        :param enable_cloud_record: 专业小班课教室是否展示云端录制，1展示 2隐藏 ，默认取系统配置
        """
        if isinstance(start_time, datetime.datetime):
            start_time = int(start_time.timestamp())
        if isinstance(end_time, datetime.datetime):
            end_time = int(end_time.timestamp())
        return self._post(
            '/openapi/room/create',
            optionaldict({
                'partner_id': self.partner_id,
                'title': title,
                'start_time': start_time,
                'end_time': end_time,
                'type': type,
                'industry_type': industry_type,
                'max_users': max_users,
                'pre_enter_time': pre_enter_time,
                'is_long_term': is_long_term,
                'is_group_live': is_group_live,
                'template_name': template_name,
                'speak_camera_turnon': speak_camera_turnon,
                'teacher_need_detect_device': teacher_need_detect_device,
                'student_need_detect_device': student_need_detect_device,
                'is_video_main': is_video_main,
                'm_is_video_main': m_is_video_main,
                'is_mock_live': is_mock_live,
                'is_push_live': is_push_live,
                'is_webrtc_live': is_webrtc_live,
                'mock_room_id': mock_room_id,
                'mock_session_id': mock_session_id,
                'mock_video_id': mock_video_id,
                'switch_room_role': switch_room_role,
                'enable_share': enable_share,
                'enable_group_users_public': enable_group_users_public,
                'group_admin_permission': group_admin_permission,
                'enable_group_chat_public': enable_group_chat_public,
                'new_group_live': new_group_live,
                'mock_live_record': mock_live_record,
                'enable_weixin_auth': enable_weixin_auth,
                'has_student_raise': has_student_raise,
                'end_delay_time': end_delay_time,
                'class_end_operation': class_end_operation,
                'disable_switch_class': disable_switch_class,
                'max_backup_users': max_backup_users,
                'auto_on_stage': auto_on_stage,
                'has_foreign_user': has_foreign_user,
                'template_type': template_type,
                'enable_cloud_record': enable_cloud_record,
            }),
            files=optionaldict({
                'background_attachment': background_attachment,
                'whiteboard_attachment': whiteboard_attachment,
            }),
        )

    def update(
            self,
            room_id,
            title=None,
            start_time=None,
            end_time=None,
            max_users=None,
            pre_enter_time=None,
            template_name=None,
            forbidden_end_types=None,
            is_video_main=None,
            m_is_video_main=None,
            mock_room_id=None,
            mock_session_id=None,
            mock_video_id=None,
            switch_room_role=None,
            enable_cloud_record=None,
            class_end_operation=None,
            disable_switch_class=None,
            max_backup_users=None,
            background_attachment=None,
            whiteboard_attachment=None,
            template_type=None
    ):
        """
        更新房间信息

        :param room_id: 房间ID，14位
        :param title: 房间标题
        :param start_time: 开课时间, unix时间戳(秒)
        :param end_time: 结束时间, unix时间戳(秒)
        :param max_users: 人数限制 大班课/双师班：不传或传0表示不限制。小班课：必传(取值范围1-12)作为台上人数；基础班一对一时，必须传1值
        :param pre_enter_time: 学生可提前进入的时间，单位为秒
        :param template_name: 可选值   教育直播：doubleCamera(双摄像头)、classic(经典模板)、triple(三分屏)、single(单视频模板)、liveWall(视频墙)
                               企业直播：singleVideo（单视频），docAudio（文档加音频），docVideo（文档加视频）
        :param forbidden_end_types: 指定屏蔽的端，可选值（web:pc浏览器, h5:手机浏览器）多种以英文逗号分隔
        :param is_video_main: 指定PC端是否以视频为主 1:以视频为主 2:以PPT为主 （默认是以ppt为主，该选项只针对三分屏有效）
        :param m_is_video_main: 指定手机H5页面是否以视频为主 1:以视频为主 2:以PPT为主 （默认是以视频为主）
        :param mock_room_id: 伪直播关联的回放教室号
        :param mock_session_id: 伪直播关联的回放教室session_id（针对长期房间）
        :param mock_video_id: 伪直播关联的点播视频ID
        :param switch_room_role: 分组直播大小班切换，角色控制 1：大班 2：小班
        :param enable_cloud_record: 小班课教室是否展示云端录制，1展示 2隐藏 ，默认取系统配置
        :param class_end_operation: 大班下课后操作，0:回到小班,1:全员下课 默认0
        :param disable_switch_class: 课中是否允许切班，1:不允许,0:允许 默认0，如果不允许，配置该字段需要将switch_room_role设置为1，否则不生效
        :param max_backup_users: 小班课1vNvM班型，台下学生数量限制
        :param background_attachment: 小班课教室背景图(文件不参与签名的计算)，图片文件
        :param whiteboard_attachment: 小班课教室白板(文件不参与签名的计算)，图片文件
        :param template_type: 专业小班课模板类型 可传1,2,3；1为第一套模板；2为第二套模板；3为一对一模板，需申请开通
        """
        if isinstance(start_time, datetime.datetime):
            start_time = int(start_time.timestamp())
        if isinstance(end_time, datetime.datetime):
            end_time = int(end_time.timestamp())
        return self._post(
            '/openapi/room/update',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'title': title,
                'start_time': start_time,
                'end_time': end_time,
                'max_users': max_users,
                'pre_enter_time': pre_enter_time,
                'template_name': template_name,
                'forbidden_end_types': forbidden_end_types,
                'is_video_main': is_video_main,
                'm_is_video_main': m_is_video_main,
                'mock_room_id': mock_room_id,
                'mock_session_id': mock_session_id,
                'mock_video_id': mock_video_id,
                'switch_room_role': switch_room_role,
                'enable_cloud_record': enable_cloud_record,
                'class_end_operation': class_end_operation,
                'disable_switch_class': disable_switch_class,
                'max_backup_users': max_backup_users,
                'template_type': template_type,
            }),
            files=optionaldict({
                'background_attachment': background_attachment,
                'whiteboard_attachment': whiteboard_attachment,
            }),
        )

    def delete(
            self,
    ):
        """
        删除教室
        删除一个教室
        """
        return self._post(
            '/openapi/room/delete',
            optionaldict({
                'partner_id': self.partner_id,
            }),
        )

    def info(
            self,
            room_id,
    ):
        """
        获取教室信息

        :param room_id: 教室id
        """
        return self._post(
            '/openapi/room/info',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def getcode(
            self,
            room_id,
            user_number,
            user_avatar=None,
    ):
        """
        生成用户参加码
        为了方便学生进入教室，我们可以根据学生的user_number生成学生参加码。学生可以凭参加码直接进入教室。

        :param room_id: 教室ID
        :param user_number: 合作方账号体系下的用户ID号，必须是int类型数字
        :param user_avatar: 用户头像，需要完整的url地址
        """
        return self._post(
            '/openapi/room/getcode',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'user_number': user_number,
                'user_avatar': user_avatar,
            }),
            result_processor=lambda x: x['student_code']
        )

    def get_code_info(
            self,
            code,
    ):
        """
        获取用户参加码信息

        :param code: 学生参加码
        """
        return self._post(
            '/openapi/room/getCodeInfo',
            optionaldict({
                'partner_id': self.partner_id,
                'code': code,
            }),
        )

    def listcode(
            self,
            room_id,
            type=0,
            page=1,
            limit=100,
    ):
        """
        获取已生成的参加码列表
        获取已经生成的学生参加码列表

        :param room_id: 教室ID
        :param type: 0表示普通参加码 1表示试听参加码
        :param page: 页数，参加码数量过多时，可以分多页来获取，每页取limit条。默认值为1
        :param limit: 每页获取的条数，默认值100，最大值不能超过1000
        """
        return self._post(
            '/openapi/room/listcode',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'type': type,
                'page': page,
                'limit': limit,
            }),
        )

    def list(
            self,
            page=1,
            limit=100,
            product_type=0,
    ):
        """
        获取教室列表
        获取已经创建的教室列表

        :param page: 页数，参加码数量过多时，可以分多页来获取，每页取limit条。默认值为1
        :param limit: 每页获取的条数，默认值100，最大值不能超过1000
        :param product_type: 1:教育直播 2:小班课 4：企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/room/list',
            optionaldict({
                'partner_id': self.partner_id,
                'page': page,
                'limit': limit,
                'product_type': product_type,
            }),
            result_processor=lambda x: x['list']
        )

    def get_audition_code(
            self,
            room_id,
            user_numbers,
            user_avatar=None,
            audition_length=None,
    ):
        """
        生成用户试听参加码

        :param room_id: 房间ID
        :param user_numbers: 合作方账号体系下的用户ID号，必须是数字且要大于0,多个的话用逗号分隔
        :param user_avatar: 用户头像，需要完整的url地址
        :param audition_length: 必须大于0，且不能超过3600，单位是秒数，值指的是具体试听时长
        """
        return self._post(
            '/openapi/room/getAuditionCode',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'user_numbers': user_numbers,
                'user_avatar': user_avatar,
                'audition_length': audition_length,
            }),
        )

    def create_group_live_codes(
            self,
            room_id,
            number,
    ):
        """
        创建分组直播参加码
        该接口用于创建分组直播参加码

        :param room_id:
        :param number: 创建分组的数量
        """
        return self._post(
            '/openapi/room/createGroupLiveCodes',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'number': number,
            }),
        )

    def get_group_live_codes(
            self,
            room_id,
    ):
        """
        获取分组直播参加码
        该接口用于获取分组直播参加码

        :param room_id:
        """
        return self._post(
            '/openapi/room/getGroupLiveCodes',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def get_push_live_url(
            self,
            room_id,
    ):
        """
        获取推流直播的推流地址
        该接口用于获取推流直播的推流地址

        :param room_id:
        """
        return self._post(
            '/openapi/room/getPushLiveUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def get_group_sub_room_id(
            self,
            room_id,
    ):
        """
        获取支持大小班的分组直播小班教室room_id
        该接口用于获取支持大小班的分组直播小班教室room_id

        :param room_id:
        """
        return self._post(
            '/openapi/room/getGroupSubRoomId',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def get_pull_stream_url(
            self,
            room_id,
    ):
        """
        获取推流直播的拉流地址
        该接口仅用于获取推流直播的拉流地址

        :param room_id:
        """
        return self._post(
            '/openapi/room/getPullStreamUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def set_spot_video(
            self,
            room_id,
            video_ids,
    ):
        """
        直播设置插播回放
        该接口用于设置大班课里插播回放的视频，一个直播间最多只能设置3个插播回放。 注：新选择的插播视频需5小时处理时间，请生效后使用，7天后会过期，将不可使用

        :param room_id:
        :param video_ids: 插播回放对应的视频id，多个以英文逗号分隔
        """
        return self._post(
            '/openapi/room/setSpotVideo',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'video_ids': video_ids,
            }),
        )

    def get_spot_video(
            self,
            room_id,
            video_ids,
    ):
        """
        获取教室设置的插播回放
        该接口用于设置大班课里插播回放的视频，一个直播间最多只能设置3个插播回放。 注：新选择的插播视频需5小时处理时间，请生效后使用，7天后会过期，将不可使用

        :param room_id:
        :param video_ids: 插播回放对应的视频id，多个以英文逗号分隔
        """
        return self._post(
            '/openapi/room/getSpotVideo',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'video_ids': video_ids,
            }),
        )
