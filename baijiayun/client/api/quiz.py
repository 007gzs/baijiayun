# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from .base import BaseAPI


class Quiz(BaseAPI):
    """
    测验
    """

    def assign_room_paper(
            self,
            paper_ids,
            room_id,
            product_type=0,
    ):
        """
        小测关联直播间

        :param paper_ids: 逗号分开的试卷id
        :param room_id: 教室号
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/quiz/assignRoomPaper',
            optionaldict({
                'partner_id': self.partner_id,
                'paper_ids': paper_ids,
                'room_id': room_id,
                'product_type': product_type,
            }),
        )

    def get_room_quiz_list(
            self,
            room_id,
            product_type=0,
    ):
        """
        查看教室小测

        :param room_id: 教室号
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/quiz/getRoomQuizList',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'product_type': product_type,
            }),
        )

    def batch_delete_room_paper(
            self,
            room_id,
            paper_ids,
            product_type=0,
    ):
        """
        删除教室小测

        :param room_id: 教室号
        :param paper_ids: 逗号分开的id
        :param product_type: 1:大班课，2，小班课，3：双师，4，企业直播（单一产品线账号不需要传此参数）
        """
        return self._post(
            '/openapi/quiz/batchDeleteRoomPaper',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'paper_ids': paper_ids,
                'product_type': product_type,
            }),
        )
