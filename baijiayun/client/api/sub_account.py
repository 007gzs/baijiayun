# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class SubAccount(BaseAPI):
    """
    子账号
    """

    def get_sub_account_list(
            self,
            status=None,
            page=1,
            page_size=10,
    ):
        """
        查询子账号列表

        :param status: 账号状态 0:全部 1:使用中 2:停用或未开通的
        :param page: 页码，默认第一页
        :param page_size: 每页条数，默认10条
        """
        return self._post(
            '/openapi/sub_account/getSubAccountList',
            optionaldict({
                'partner_id': self.partner_id,
                'status': status,
                'page': page,
                'page_size': page_size,
            }),
        )

    def create_sub_account(
            self,
            mobile,
            email,
            password,
            contacts,
            company,
            live_on,
            video_on,
            effect_time,
            expire_time,
            user_limit=None,
            max_user_limit=None,
            user_count=None,
            max_user_count=None,
            live_max_speakers=None,
            storage_limit=None,
            max_storage_limit=None,
            flow_limit=None,
            max_flow_limit=None,
    ):
        """
        创建子账号

        :param mobile: 手机号必须是未注册过的
        :param email: 邮箱必须是未注册过的
        :param password: 密码必须为6-18位之间
        :param contacts: 联系人
        :param company: 公司名
        :param live_on: 是否开通直播 0:不开通 1:开通
        :param video_on: 是否开通点播 0:不开通 1:开通
        :param effect_time: 账号生效日期，格式如：2017-11-24
        :param expire_time: 账号失效日期，格式如：2018-11-24
        :param user_limit: 直播套餐并发值，如开通直播，且为并发计费，则该值为必传值。必须是正整数。
        :param max_user_limit: 直播可超额使用到的并发值，如开通直播，且为并发计费，则该值为必传值。该值必须不小于user_limit。必须是正整数。
        :param user_count: 直播套餐人次/时长点数值，如开通直播，且为人次/时长点数计费，则该值为必传值
        :param max_user_count: 直播可超额使用到的人次/时长点数值，如开通直播，且为人次/时长点数计费，则该值为必传值，且不能小于user_count
        :param live_max_speakers: 最大上麦路数
        :param storage_limit: 点播存储空间容量，如开通点播播，则该值为必传值。 必须是正整数。
        :param max_storage_limit: 点播可超额使用到的容量，如开通点播，则该值为必传值。该值必须不小于storage_limit。必须是正整数。
        :param flow_limit: 点播套餐月流量，如开通点播，则该值为必传值。必须是正整数。
        :param max_flow_limit: 点播可超额使用到的月流量，如开通点播，则该值为必传值。该值必须不小于flow_limit。必须是正整数。
        """
        if isinstance(effect_time, datetime.datetime):
            effect_time = effect_time.strftime('%Y-%m-%d')
        if isinstance(expire_time, datetime.datetime):
            expire_time = expire_time.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/sub_account/createSubAccount',
            optionaldict({
                'partner_id': self.partner_id,
                'mobile': mobile,
                'email': email,
                'password': password,
                'contacts': contacts,
                'company': company,
                'live_on': live_on,
                'video_on': video_on,
                'effect_time': effect_time,
                'expire_time': expire_time,
                'user_limit': user_limit,
                'max_user_limit': max_user_limit,
                'user_count': user_count,
                'max_user_count': max_user_count,
                'live_max_speakers': live_max_speakers,
                'storage_limit': storage_limit,
                'max_storage_limit': max_storage_limit,
                'flow_limit': flow_limit,
                'max_flow_limit': max_flow_limit,
            }),
        )

    def stop_sub_account(
            self,
            sub_partner_id,
    ):
        """
        停用子账号

        :param sub_partner_id: 要停用的子账号ID
        """
        return self._post(
            '/openapi/sub_account/stopSubAccount',
            optionaldict({
                'partner_id': self.partner_id,
                'sub_partner_id': sub_partner_id,
            }),
            result_processor=lambda x: x['partner_id']
        )

    def get_sub_account_info(
            self,
            sub_partner_id,
    ):
        """
        获取子账号信息

        :param sub_partner_id: 子账号ID
        """
        return self._post(
            '/openapi/sub_account/getSubAccountInfo',
            optionaldict({
                'partner_id': self.partner_id,
                'sub_partner_id': sub_partner_id,
            }),
        )

    def modify_sub_account(
            self,
            sub_partner_id,
            live_on=None,
            video_on=None,
            storage_limit=None,
            max_storage_limit=None,
            flow_limit=None,
            max_flow_limit=None,
            live_max_speakers=None,
            effect_time=None,
            expire_time=None,
            user_limit=None,
            max_user_limit=None,
            user_count=None,
            max_user_count=None,
    ):
        """
        修改子账号配置

        :param sub_partner_id: 子账号ID
        :param live_on: 直播账号状态 1:服务正常 2:服务已停止
        :param video_on: 点播账号状态 0:未开通 1:服务正常 2:服务已停止
        :param storage_limit: 点播存储空间容量，如开通点播播，则该值为必传值。
        :param max_storage_limit: 点播可超额使用到的容量，该值必须不小于storage_limit。必须是正整数。
        :param flow_limit: 点播套餐月流量
        :param max_flow_limit: 点播可超额使用到的月流量，该值必须不小于flow_limit。必须是正整数。
        :param live_max_speakers: 最大上麦路数
        :param effect_time: 生效时间
        :param expire_time: 失效时间
        :param user_limit: 并发人数上限，并发计费可设置
        :param max_user_limit: 直播可超额使用到的并发值，直播并发计费有效。该值必须不小于user_limit。必须是正整数。
        :param user_count: 人次/时长上限，人次/时长计费可设置
        :param max_user_count: 直播可超额使用到的人次/时长点数值，直播人次/时长点数计费有效，且不能小于user_count
        """
        if isinstance(effect_time, datetime.datetime):
            effect_time = effect_time.strftime('%Y-%m-%d')
        if isinstance(expire_time, datetime.datetime):
            expire_time = expire_time.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/sub_account/modifySubAccount',
            optionaldict({
                'partner_id': self.partner_id,
                'sub_partner_id': sub_partner_id,
                'live_on': live_on,
                'video_on': video_on,
                'storage_limit': storage_limit,
                'max_storage_limit': max_storage_limit,
                'flow_limit': flow_limit,
                'max_flow_limit': max_flow_limit,
                'live_max_speakers': live_max_speakers,
                'effect_time': effect_time,
                'expire_time': expire_time,
                'user_limit': user_limit,
                'max_user_limit': max_user_limit,
                'user_count': user_count,
                'max_user_count': max_user_count,
            }),
        )
