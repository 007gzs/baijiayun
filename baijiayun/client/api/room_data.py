# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class RoomData(BaseAPI):
    """
    房间数据
    """

    def export_answer_stat(
            self,
            room_id,
            date=None,
    ):
        """
        获取教室答题器数据
        该接口用于获取教室内学生答题器数据

        :param room_id:
        :param date:
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/room_data/exportAnswerStat',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'date': date,
            }),
        )

    def export_chat_msg(
            self,
            room_id,
            date,
    ):
        """
        导出教室聊天记录
        导出教室内的聊天记录。只能导出最近2周的直播的聊天记录。

        :param room_id: 教室号
        :param date: 导出日期
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/room_data/exportChatMsg',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'date': date,
            }),
            result_processor=lambda x: x['list']
        )

    def export_live_report(
            self,
            room_id,
            type=None,
            page=1,
            page_size=0,
            date=None,
    ):
        """
        导出直播教室学员观看记录
        导出直播教室学员观看记录。

        :param room_id: 教室号
        :param type: 可选值 all:所有用户 student:学员 teacher:老师 admin:助教，默认只导出学员观看记录
        :param page: 分页参数
        :param page_size: 每页返回条数，如果不传则返回所有的
        :param date: 查询日期，格式如：2018-03-02
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/room_data/exportLiveReport',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'type': type,
                'page': page,
                'page_size': page_size,
                'date': date,
            }),
        )

    def get_all_room_user_stat(
            self,
            product_type,
            date,
    ):
        """
        获取指定日期所有的直播间人次和最高并发量

        :param product_type: 1:教育直播 2：小班课 4：企业直播
        :param date: 格式如：2017-11-23
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/room_data/getAllRoomUserStat',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'date': date,
            }),
            result_processor=lambda x: x['room_user_stat']
        )

    def get_room_peak_user(
            self,
            room_id,
            start_time,
            end_time,
    ):
        """
        获取指定教室一段时间内的并发量
        该接口用于获取一段时间内教室的并发人数变化图。由于数据量较大，本接口每10分钟取一个最大值。 如果：15:10:00 => 3 表示的是 15:10:00~15:19:59 这段时间内的最高并发数为3。

        :param room_id: 教室号
        :param start_time: 格式如：2017-11-23 10:00:00
        :param end_time: 格式如：2017-11-23 15:00:00，查询时间范围不能跨天
        """
        if isinstance(start_time, datetime.datetime):
            start_time = start_time.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(end_time, datetime.datetime):
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
        return self._post(
            '/openapi/room_data/getRoomPeakUser',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'start_time': start_time,
                'end_time': end_time,
            }),
        )

    def export_room_praise_stat(
            self,
            room_id,
    ):
        """
        获取直播教室的点赞数据
        该接口用于获取直播教室的点赞数据

        :param room_id:
        """
        return self._post(
            '/openapi/room_data/exportRoomPraiseStat',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def get_room_quiz(
            self,
            room_id,
    ):
        """
        获取直播教室测验的试题信息
        该接口用于获取直播教室测验的试题信息

        :param room_id: 教室号
        """
        return self._post(
            '/openapi/room_data/getRoomQuiz',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
            result_processor=lambda x: x['quiz_list']
        )

    def get_quiz_user_answer(
            self,
            room_id,
            quiz_id,
    ):
        """
        获取直播教室测验题目的学员答案信息
        该接口用于获取某个教室测验试题学员答案信息

        :param room_id:
        :param quiz_id: 试卷的id
        """
        return self._post(
            '/openapi/room_data/getQuizUserAnswer',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'quiz_id': quiz_id,
            }),
        )

    def get_exp_report_list(
            self,
            room_id,
    ):
        """
        获取表情报告截取的表情图片

        :param room_id:
        """
        return self._post(
            '/openapi/room_data/getExpReportList',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def get_user_checkin_info(
            self,
            room_id,
    ):
        """
        获取教室学员签到信息
        该接口用于获取某个教室学员签到信息

        :param room_id:
        """
        return self._post(
            '/openapi/room_data/getUserCheckinInfo',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def get_room_raise_data(
            self,
            room_id,
            start_time,
            end_time,
    ):
        """
        获取教室举手连麦数据
        该接口用于获取教室内学生举手连麦数据（备注：仅支持在pro环境的账号）

        :param room_id:
        :param start_time:
        :param end_time:
        """
        if isinstance(start_time, datetime.datetime):
            start_time = start_time.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(end_time, datetime.datetime):
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
        return self._post(
            '/openapi/room_data/getRoomRaiseData',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'start_time': start_time,
                'end_time': end_time,
            }),
        )

    def get_room_red_package(
            self,
            room_id,
    ):
        """
        第三方教室中学生抢红包统计
        该接口仅用于第三方红包雨抢红包统计

        :param room_id:
        """
        return self._post(
            '/openapi/room-data/getRoomRedPackage',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def export_award_stat(
            self,
            room_id,
            date=None,
    ):
        """
        获取教室抽奖数据
        该接口用于获取教室内学生抽奖数据（备注：仅支持在pro环境的账号）

        :param room_id:
        :param date:
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/room_data/exportAwardStat',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'date': date,
            }),
        )

    def export_qa_stat(
            self,
            room_id,
            date=None,
    ):
        """
        获取教室问答数据
        该接口用于获取教室内学生问答数据（备注：仅支持在pro环境的账号）

        :param room_id:
        :param date:
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/room_data/exportQaStat',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'date': date,
            }),
        )

    def export_questionnaire_stat(
            self,
            room_id,
            date=None,
    ):
        """
        获取教室邀请函数据
        该接口用于获取教室内学生邀请函数据（备注：仅支持在pro环境的账号）

        :param room_id:
        :param date:
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/room_data/exportQuestionnaireStat',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'date': date,
            }),
        )

    def get_evaluation_stat(
            self,
            room_id,
            page,
            page_size,
            date=None,
    ):
        """
        获取教室课后评价数据
        该接口用于获取教室内课后评价数据（备注：仅支持在pro环境的账号）

        :param room_id:
        :param page:
        :param page_size:
        :param date:
        """
        if isinstance(date, datetime.date):
            date = date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/room_data/getEvaluationStat',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'date': date,
                'page': page,
                'page_size': page_size,
            }),
        )

    def get_checkin_info(
            self,
            room_id,
            session_id,
    ):
        """
        获取单次签到记录
        通过room_id和session_id获取单次签到记录

        :param room_id: 教室ID
        :param session_id: session_id
        """
        return self._post(
            '/openapi/room_data/getCheckinInfo',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'session_id': session_id,
            }),
        )

    def export_answer_by_question_id(
            self,
            room_id,
            question_id,
    ):
        """
        获取单次答题器记录
        通过room_id和question_id获取单次签到记录

        :param room_id: 教室ID
        :param question_id: question_id
        """
        return self._post(
            '/openapi/room_data/exportAnswerByQuestionId',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'question_id': question_id,
            }),
        )

    def get_red_package_record_info(
            self,
            room_id,
            red_package_id,
    ):
        """
        获取单次红包记录
        通过room_id和record_id获取单次红包记录

        :param room_id: 教室ID
        :param red_package_id: red_package_id
        """
        return self._post(
            '/openapi/room_data/getRedPackageRecordInfo',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'red_package_id': red_package_id,
            }),
        )
