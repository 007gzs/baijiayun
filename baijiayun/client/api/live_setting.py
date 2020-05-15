# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from .base import BaseAPI


class LiveSetting(BaseAPI):
    """
    直播配置
    """

    def set_watermark(
            self,
            pos,
            attachment=None,
            product_type=0,
    ):
        """
        设置水印
        设置水印配置

        :param pos: 位置（左上、右上、右下、左下依次是1、2、3、4，0为不启用）
        :param attachment: 水印图片（限制1M，文件不参与签名的计算）
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/setWatermark',
            optionaldict({
                'partner_id': self.partner_id,
                'pos': pos,
                'product_type': product_type,
            }),
            files=optionaldict({
                'attachment': attachment,
            }),
        )

    def get_watermark(
            self,
            product_type=0,
    ):
        """
        获取水印配置

        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/getWatermark',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
            }),
        )

    def get_sensitive_word(
            self,
            page=1,
            page_size=20,
            product_type=0,
    ):
        """
        查看当前敏感词列表

        :param page: 分页参数
        :param page_size: 每页返回条数
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/getSensitiveWord',
            optionaldict({
                'partner_id': self.partner_id,
                'page': page,
                'page_size': page_size,
                'product_type': product_type,
            }),
        )

    def add_sensitive_word_batch(
            self,
            words,
            product_type=0,
    ):
        """
        添加敏感词

        :param words: 用逗号,分开的敏感词
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/addSensitiveWordBatch',
            optionaldict({
                'partner_id': self.partner_id,
                'words': words,
                'product_type': product_type,
            }),
        )

    def delete_sensitive_word_batch(
            self,
            ids,
            product_type=0,
    ):
        """
        删除敏感词

        :param ids: 用逗号,分开的敏感词id
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/deleteSensitiveWordBatch',
            optionaldict({
                'partner_id': self.partner_id,
                'ids': ids,
                'product_type': product_type,
            }),
        )

    def get_live_horse_lamp(
            self,
            product_type=0,
    ):
        """
        获取跑马灯设置

        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/getLiveHorseLamp',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
            }),
        )

    def set_live_horse_lamp(
            self,
            product_type=0,
            type=None,
            value=None,
            color=None,
            font_size=None,
            opacity=None,
    ):
        """
        设置跑马灯设置

        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        :param type: 0 关闭 1固定值 2 昵称
        :param value: 跑马灯
        :param color: 颜色
        :param font_size: 直播跑马灯字体大小
        :param opacity: 直播跑马灯不透明度
        """
        return self._post(
            '/openapi/live_setting/setLiveHorseLamp',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'type': type,
                'value': value,
                'color': color,
                'font_size': font_size,
                'opacity': opacity,
            }),
        )

    def add_notice(
            self,
            content,
            link,
            product_type=0,
    ):
        """
        添加公告模板

        :param content: 内容
        :param link: 链接
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/addNotice',
            optionaldict({
                'partner_id': self.partner_id,
                'content': content,
                'link': link,
                'product_type': product_type,
            }),
        )

    def get_notice_list(
            self,
            page=1,
            page_size=20,
            query=None,
            product_type=0,
    ):
        """
        获取公告列表

        :param page: 分页参数
        :param page_size: 每页返回条数
        :param query: 关键字查询
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/getNoticeList',
            optionaldict({
                'partner_id': self.partner_id,
                'page': page,
                'page_size': page_size,
                'query': query,
                'product_type': product_type,
            }),
        )

    def delete_notice_batch(
            self,
            ids,
            product_type=0,
    ):
        """
        删除公告

        :param ids: 逗号（,）分开的id
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/deleteNoticeBatch',
            optionaldict({
                'partner_id': self.partner_id,
                'ids': ids,
                'product_type': product_type,
            }),
        )

    def add_quiz(
            self,
            attachment,
            is_force=0,
            product_type=0,
    ):
        """
        添加小测

        :param attachment: 小测模板excel表格（文件不参与签名的计算）
        :param is_force: 是否强制参加
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/addQuiz',
            optionaldict({
                'partner_id': self.partner_id,
                'is_force': is_force,
                'product_type': product_type,
            }),
            files=optionaldict({
                'attachment': attachment,
            }),
        )

    def get_quiz_list(
            self,
            page=1,
            page_size=20,
            query=None,
            product_type=0,
    ):
        """
        获取小测模板

        :param page: 分页参数
        :param page_size: 每页返回条数
        :param query: 关键字查询
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/getQuizList',
            optionaldict({
                'partner_id': self.partner_id,
                'page': page,
                'page_size': page_size,
                'query': query,
                'product_type': product_type,
            }),
        )

    def delete_quiz(
            self,
            id,
            product_type=0,
    ):
        """
        删除小测模板

        :param id: id
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/deleteQuiz',
            optionaldict({
                'partner_id': self.partner_id,
                'id': id,
                'product_type': product_type,
            }),
        )

    def set_max_red_package_count(
            self,
            max_count,
            product_type=0,
    ):
        """
        修改红包最大个数限制

        :param max_count: 最大红包限制个数，最大不超过1000
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/setMaxRedPackageCount',
            optionaldict({
                'partner_id': self.partner_id,
                'max_count': max_count,
                'product_type': product_type,
            }),
        )

    def get_max_red_package_count(
            self,
            product_type=0,
    ):
        """
        获取红包最大个数限制

        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/live_setting/getMaxRedPackageCount',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
            }),
        )
