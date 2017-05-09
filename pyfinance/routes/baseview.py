# coding=utf8
from __future__ import unicode_literals

import logging

class BaseView(object):

    FormFactory = None

    def __init__(self, request, logger=None):
        """
        基礎view 設定
        :param request:
        :param logger:
        :return:
        """
        # 抓取logger設定
        self.logger = logger or logging.getLogger(__name__)

        # 抓取所有的請求相關資訊
        self.request = request

        # 記錄Request
        self.logger.info('[%s] %s - %s', self.request.method,
                         self.request.route_name, self.request.real_ip)

        # 抓取參數
        self.request_params = self.request.params

        # 抓取系統設定值
        self.settings = self.request.registry.settings

        # 回傳標頭設定
        self.request.response.headerlist.extend(
            (
                (str('Access-Control-Allow-Origin'), str('*')),
                # (str('Content-Type'), str('application/json')),
            )
        )

        # 回傳語言編碼設定
        self.request.response.charset = str('utf8')

