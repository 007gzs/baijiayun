# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class HuDong(BaseAPI):
    """
    互动
    """
    API_BASE_URL = 'https://hudong.baijiayun.com'

    def interact_info_get_interact_list(
            self,
            room_id,
            type,
            page=1,
            page_size=20,
            begin_time=None,
            end_time=None,
    ):
        """
        签到汇总数据

        :param room_id: 教室id
        :param type: 类型
        :param page: 页数
        :param page_size: 每页数据条数
        :param begin_time: 开始时间
        :param end_time: 结束时间
        """
        if isinstance(begin_time, datetime.datetime):
            begin_time = begin_time.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(end_time, datetime.datetime):
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
        return self._post(
            '/openapi/interact_info/getInteractList',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'type': type,
                'page': page,
                'page_size': page_size,
                'begin_time': begin_time,
                'end_time': end_time,
            }),
        )

    def interact_info_get_interact_detail(
            self,
            room_id,
            type,
            page=1,
            page_size=20,
            begin_time=None,
            end_time=None,
    ):
        """
        签到明细数据

        :param room_id: 教室id
        :param type: 类型
        :param page: 页数
        :param page_size: 每页数据条数
        :param begin_time: 开始时间
        :param end_time: 结束时间
        """
        if isinstance(begin_time, datetime.datetime):
            begin_time = begin_time.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(end_time, datetime.datetime):
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
        return self._post(
            '/openapi/interact_info/getInteractDetail',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'type': type,
                'page': page,
                'page_size': page_size,
                'begin_time': begin_time,
                'end_time': end_time,
            }),
        )

    def interact_data_get_class_vote_data(
            self,
            room_id,
            type=None,
            sub_type=None,
            date=None,
            page=1,
            page_size=20,
    ):
        """
        获取班级投票数据

        :param room_id: 教室id
        :param type: 题型
        :param sub_type: 题目类型
        :param date: 日期，格式类似于：2019-10-10
        :param page: 页数
        :param page_size: 每页数据条数
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/interact_data/getClassVoteData',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'type': type,
                'sub_type': sub_type,
                'date': date,
                'page': page,
                'page_size': page_size,
            }),
        )

    def interact_data_get_red_package_data(
            self,
            room_id,
            type=None,
            date=None,
            page=1,
            page_size=20,
    ):
        """
        获取班级红包数据

        :param room_id: 教室id
        :param type: 红包类型
        :param date: 日期 格式类似于：2019-10-10
        :param page: 页数
        :param page_size: 每页数据条数
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/interact_data/getRedPackageData',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'type': type,
                'date': date,
                'page': page,
                'page_size': page_size,
            }),
        )

    def interact_data_get_random_ask_data(
            self,
            room_id,
            type=None,
            date=None,
            page=1,
            page_size=20,
    ):
        """
        获取班级随机点名数据

        :param room_id: 教室id
        :param type: 类型
        :param date: 日期 格式类似于：2019-10-10
        :param page: 页数
        :param page_size: 每页数据条数
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/interact_data/getRandomAskData',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'type': type,
                'date': date,
                'page': page,
                'page_size': page_size,
            }),
        )

    def interact_data_get_ai_user_count_data(
            self,
            room_id,
            date=None,
            page=1,
            page_size=20,
    ):
        """
        获取AI班级数人数列表

        :param room_id: 教室id
        :param date: 日期 格式类似于：2019-10-10
        :param page: 页数
        :param page_size: 每页数据条数
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/interact_data/getAiUserCountData',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'date': date,
                'page': page,
                'page_size': page_size,
            }),
        )

    def interact_data_save(
            self,
            assist_teacher_id,
            assist_teacher_name,
            assist_teacher_mobile,
            class_id,
            class_name,
            student_list,
            origin,
    ):
        """
        双师人员数据保存
        客户使用的新排课系统，数据接入到双师系统中

        :param assist_teacher_id: 客户助教id
        :param assist_teacher_name: 助教姓名
        :param assist_teacher_mobile: 助教电话
        :param class_id: 客户班级 id
        :param class_name: 班级名称
        :param student_list: 学生明细内容
        :param origin: huatu
        """
        return self._post(
            '/openapi/interact_data/save',
            optionaldict({
                'partner_id': self.partner_id,
                'assist_teacher_id': assist_teacher_id,
                'assist_teacher_name': assist_teacher_name,
                'assist_teacher_mobile': assist_teacher_mobile,
                'class_id': class_id,
                'class_name': class_name,
                'student_list': student_list,
                'origin': origin,
            }),
        )

    def interact_data_get_checkin_data(
            self,
            checkin_id,
    ):
        """
        根据签到id,获取签到信息
        根据checkin_id，获取签到明细数据

        :param checkin_id: 签到id
        """
        return self._post(
            '/openapi/interact_data/getCheckinData',
            optionaldict({
                'partner_id': self.partner_id,
                'checkin_id': checkin_id,
            }),
        )

    def interact_data_delete(
            self,
            class_ids,
    ):
        """
        删除班级、助教、学生信息
        根据 class_id，可以删除跟班级关联的学生、老师和班级信息

        :param class_ids: 班级 id
        """
        return self._post(
            '/openapi/interact_data/delete',
            optionaldict({
                'partner_id': self.partner_id,
                'class_ids': class_ids,
            }),
            result_processor=lambda x: x['result']
        )

    def interact_data_list(
            self,
            class_id,
    ):
        """
        获取班级、助教、学生信息列表
        根据class_id， 获取班级,和关联班级的学生、老师

        :param class_id: 班级 id
        """
        return self._post(
            '/openapi/interact_data/list',
            optionaldict({
                'partner_id': self.partner_id,
                'class_id': class_id,
            }),
        )

    def teacher_save(
            self,
            teacher_id,
            teacher_name,
            teacher_mobile,
            role,
    ):
        """
        老师添加、修改接口
        增加和修改老师信息

        :param teacher_id: 客户老师id
        :param teacher_name: 老师姓名
        :param teacher_mobile: 老师电话
        :param role: 老师角色
        """
        return self._post(
            '/openapi/teacher/save',
            optionaldict({
                'partner_id': self.partner_id,
                'teacher_id': teacher_id,
                'teacher_name': teacher_name,
                'teacher_mobile': teacher_mobile,
                'role': role,
            }),
        )

    def teacher_delete(
            self,
            teacher_id,
            role,
    ):
        """
        老师删除接口
        根据teacher_id，删除老师信息

        :param teacher_id: 第三方老师id
        :param role: 老师角色
        """
        return self._post(
            '/openapi/teacher/delete',
            optionaldict({
                'partner_id': self.partner_id,
                'teacher_id': teacher_id,
                'role': role,
            }),
        )

    def teacher_list(
            self,
            role,
            page,
            page_size,
    ):
        """
        获取老师信息接口
        获取老师列表

        :param role: 老师角色
        :param page: 页码
        :param page_size: 每页条数
        """
        return self._post(
            '/openapi/teacher/list',
            optionaldict({
                'partner_id': self.partner_id,
                'role': role,
                'page': page,
                'page_size': page_size,
            }),
        )

    def interact_data_update_callback_url(
            self,
            callback_url,
    ):
        """
        修改回调地址

        :param callback_url: 回调地址
        """
        return self._post(
            '/openapi/interact_data/updateCallbackUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'callback_url': callback_url,
            }),
        )
