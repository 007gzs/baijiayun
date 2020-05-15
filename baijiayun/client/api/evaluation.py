# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from .base import BaseAPI


class Evaluation(BaseAPI):
    """
    评价
    """

    def get_evaluation_list(
            self,
            status=None,
            page=1,
            page_size=20,
    ):
        """
        获取课后评价模板列表
        该接口用于获取课后评价模板列表（备注：仅支持在pro环境的账号）

        :param status:
        :param page:
        :param page_size:
        """
        return self._post(
            '/openapi/evaluation/getEvaluationList',
            optionaldict({
                'partner_id': self.partner_id,
                'status': status,
                'page': page,
                'page_size': page_size,
            }),
        )

    def bind_room_evaluation(
            self,
            room_id,
            evaluate_id,
    ):
        """
        关联教室评价模板
        该接口用于关联教室评价模板（备注：仅支持在pro环境的账号）

        :param room_id:
        :param evaluate_id: 评论模板id
        """
        return self._post(
            '/openapi/evaluation/bindRoomEvaluation',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'evaluate_id': evaluate_id,
            }),
        )

    def update_room_evaluation(
            self,
            room_id,
            evaluate_id,
    ):
        """
        更换教室评价模板
        该接口用于更换教室评价模板（备注：仅支持在pro环境的账号）

        :param room_id:
        :param evaluate_id: 评论模板id
        """
        return self._post(
            '/openapi/evaluation/updateRoomEvaluation',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'evaluate_id': evaluate_id,
            }),
        )
