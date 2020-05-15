# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import datetime

from optionaldict import optionaldict

from .base import BaseAPI


class VideoData(BaseAPI):
    """
    视频数据
    """

    def get_used_flow(
            self,
            video_id,
            start_date,
            end_date,
    ):
        """
        查询指定ID视频一段时间内使用的流量
        查询指定ID的视频一段时间内使用的总流量。 注：流量的统计不是实时的，每天统计一次。

        :param video_id: 视频ID
        :param start_date: 查询起始日期，时间格式为yyyy-mm-dd，如：2017-08-01
        :param end_date: 查询结束日期，时间格式为yyyy-mm-dd，如：2017-08-01
        """
        if isinstance(start_date, datetime.date):
            start_date = start_date.strftime('%Y-%m-%d')
        if isinstance(end_date, datetime.date):
            end_date = end_date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/video_data/getUsedFlow',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'start_date': start_date,
                'end_date': end_date,
            }),
            result_processor=lambda x: x['flow']
        )

    def get_video_play_record(
            self,
            video_id,
            start_time,
            end_time,
            page=1,
            page_size=100,
    ):
        """
        获取指定视频观看记录
        该接口用于获取指定回放视频一段时间内的的详细播放记录，每次播放都会有一条记录。

        :param video_id: 点播视频ID
        :param start_time: 查询起始时间，格式如：2017-09-08 00:30:00。
        :param end_time: 查询结束时间，格式如：2017-09-08 23:59:59。查询时间不能跨天
        :param page: 页码，从1开始，默认值是1
        :param page_size: 每页获取的记录条数，默认100，最大值不能超过1000
        """
        if isinstance(start_time, datetime.datetime):
            start_time = start_time.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(end_time, datetime.datetime):
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
        return self._post(
            '/openapi/video_data/getVideoPlayRecord',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'start_time': start_time,
                'end_time': end_time,
                'page': page,
                'page_size': page_size,
            }),
        )

    def export_video_report_batch(
            self,
            start_time,
            end_time,
            product_type=0,
            page=1,
            page_size=100,
    ):
        """
        获取账号所有视频观看记录
        该接口用于获取账号下所有视频的详细播放记录（包括点播和回放），每次播放都会有一条记录。

        :param start_time: 查询起始时间，格式如：2017-09-08 00:30:00。
        :param end_time: 查询结束时间，格式如：2017-09-08 23:59:59。查询时间不能跨天
        :param product_type: 1:教育直播，2，小班课，3：双师，4，企业直播,5,点播账号
        :param page: 页码，从1开始，默认值是1
        :param page_size: 每页获取的记录条数，默认100，最大值不能超过1000
        """
        if isinstance(start_time, datetime.datetime):
            start_time = start_time.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(end_time, datetime.datetime):
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
        return self._post(
            '/openapi/video_data/exportVideoReportBatch',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'start_time': start_time,
                'end_time': end_time,
                'page': page,
                'page_size': page_size,
            }),
        )

    def get_video_play_count_rank(
            self,
            start_date,
            end_date,
            product_type=0,
    ):
        """
        获取播放量排行
        该接口用于获取一段时间内，播放量前100的视频，包含视频id和播放次数

        :param start_date: 查询起始日期，时间格式为yyyy-mm-dd，如：2017-08-01
        :param end_date: 查询结束日期，时间格式为yyyy-mm-dd，如：2017-08-01
        :param product_type: 1:教育直播，2，小班课，3：双师，4，企业直播,5,点播账号
        """
        if isinstance(start_date, datetime.date):
            start_date = start_date.strftime('%Y-%m-%d')
        if isinstance(end_date, datetime.date):
            end_date = end_date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/video_data/getVideoPlayCountRank',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'start_date': start_date,
                'end_date': end_date,
            }),
            result_processor=lambda x: x['play_rank']
        )

    def get_video_daily_play_count(
            self,
            video_id,
            start_date,
            end_date,
    ):
        """
        获取指定ID视频播放量
        该接口用于获取一段时间内，指定视频ID每天的播放量，包含日期和播放次数

        :param video_id: 视频ID
        :param start_date: 查询起始日期，时间格式为yyyy-mm-dd，如：2017-08-01
        :param end_date: 查询结束日期，时间格式为yyyy-mm-dd，如：2017-08-01
        """
        if isinstance(start_date, datetime.date):
            start_date = start_date.strftime('%Y-%m-%d')
        if isinstance(end_date, datetime.date):
            end_date = end_date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/video_data/getVideoDailyPlayCount',
            optionaldict({
                'partner_id': self.partner_id,
                'video_id': video_id,
                'start_date': start_date,
                'end_date': end_date,
            }),
            result_processor=lambda x: x['play_count']
        )

    def get_partner_daily_play_count(
            self,
            start_date,
            end_date,
            product_type=0,
    ):
        """
        获取账号视频播放量
        该接口用于获取一段时间内，当前账号每天的播放量，包含日期和播放次数

        :param start_date: 查询起始日期，时间格式为yyyy-mm-dd，如：2017-08-01
        :param end_date: 查询结束日期，时间格式为yyyy-mm-dd，如：2017-08-01
        :param product_type: 1:教育直播，2，小班课，3：双师，4，企业直播，5,点播账号
        """
        if isinstance(start_date, datetime.date):
            start_date = start_date.strftime('%Y-%m-%d')
        if isinstance(end_date, datetime.date):
            end_date = end_date.strftime('%Y-%m-%d')
        return self._post(
            '/openapi/video_data/getPartnerDailyPlayCount',
            optionaldict({
                'partner_id': self.partner_id,
                'product_type': product_type,
                'start_date': start_date,
                'end_date': end_date,
            }),
            result_processor=lambda x: x['play_count']
        )

    def get_playback_play_record(
            self,
            room_id,
            start_time,
            end_time,
            session_id=None,
            page=1,
            page_size=100,
    ):
        """
        获取指定回放视频观看记录
        该接口用于获取指定回放视频一段时间内的的详细播放记录，每次播放都会有一条记录。

        :param room_id: 回放教室号
        :param start_time: 查询起始时间，格式如：2017-09-08 00:30:00。
        :param end_time: 查询结束时间，格式如：2017-09-08 23:59:59。查询时间不能跨天
        :param session_id: 序列号（针对长期房间才会用到）
        :param page: 页码，从1开始，默认值是1
        :param page_size: 每页获取的记录条数，默认100，最大值不能超过1000
        """
        if isinstance(start_time, datetime.datetime):
            start_time = start_time.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(end_time, datetime.datetime):
            end_time = end_time.strftime('%Y-%m-%d %H:%M:%S')
        return self._post(
            '/openapi/video_data/getPlaybackPlayRecord',
            optionaldict({
                'partner_id': self.partner_id,
                'room_id': room_id,
                'session_id': session_id,
                'start_time': start_time,
                'end_time': end_time,
                'page': page,
                'page_size': page_size,
            }),
        )
