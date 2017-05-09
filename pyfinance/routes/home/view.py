# coding=utf8
from __future__ import unicode_literals

from ..baseview import BaseView

class HomeViews(BaseView):

    def __init__(self, request):
        super(HomeViews, self).__init__(request)

    def home(self):
        """
        會員首頁
        :return:
        """
        return {}