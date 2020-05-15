# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from optionaldict import optionaldict

from .base import BaseAPI


class Doc(BaseAPI):
    """
    文档
    """
    def upload_doc(
            self,
            attachment,
            room_id=None,
            ppt_animation=0,
    ):
        """
        直播课件文档上传
        上传图片或文档，可指定关联到某教室。支持的文档类型有： '.doc', '.ppt', '.pdf', '.pptx', '.docx','.jpg', '.jpeg', '.png', '.gif'

        :param attachment: 要上传的文件（文件不参与签名的计算）
        :param room_id: 教室号，如果传了教室号则文档自动绑定到该教室，不传则不绑定
        :param ppt_animation: 是否使用动效PPT，只针对PPT有效,1为动效
        """
        return self._post(
            '/openapi/doc/uploadDoc',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'ppt_animation': ppt_animation,
            }),
            files=optionaldict({
                'attachment': attachment,
            }),
        )

    def bind_doc(
            self,
            room_id,
            fid,
    ):
        """
        关联文档到教室
        将指定文档关联到指定教室

        :param room_id: 教室号
        :param fid: 文档资源号
        """
        return self._post(
            '/openapi/doc/bindDoc',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'fid': fid,
            }),
        )

    def list_doc(
            self,
            room_id,
    ):
        """
        获取指定教室内已上传的文档列表
        获取教室内已上传的文档

        :param room_id: 教室号
        """
        return self._post(
            '/openapi/doc/listDoc',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
            }),
        )

    def list_all_doc(
            self,
            type,
    ):
        """
        获取账号下上传的所有文档
        获取账号下已上传的所有文档

        :param type: 可选值 all：所有文档 room:教室里上传的文件 api:从api接口上传的文档
        """
        return self._post(
            '/openapi/doc/listAllDoc',
            optionaldict({
                'partner_id': self.partner_id,
                'type': type,
            }),
        )

    def remove_doc(
            self,
            room_id,
            fid,
    ):
        """
        移除教室内文档
        移除教室内已上传的文档

        :param room_id: 教室号
        :param fid: 文档ID
        """
        return self._post(
            '/openapi/doc/removeDoc',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'fid': fid,
            }),
            result_processor=lambda x: x['fid']
        )

    def upload_h5_by_url(
            self,
            h5_doc_url,
            room_id=None,
    ):
        """
        使用url上传h5课件
        上传一个h5 课件的 url，可以选择绑定教室。

        :param h5_doc_url: h5 课件的地址(请使用 https://开头的地址)
        :param room_id: 教室号，如果传了教室号则文档自动绑定到该教室，不传则不绑定
        """
        return self._post(
            '/openapi/doc/uploadH5ByUrl',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'h5_doc_url': h5_doc_url,
            }),
        )

    def bind_doc_multi(
            self,
            room_ids,
            fid,
    ):
        """
        关联文档到多个教室
        将指定文档关联到多个教室

        :param room_ids: 教室ID,逗号分割数组
        :param fid: 文件资源ID
        """
        return self._post(
            '/openapi/doc/bindDocMulti',
            optionaldict({
                'partner_id': self.partner_id,
                'room_ids': room_ids,
                'fid': fid,
            }),
        )
