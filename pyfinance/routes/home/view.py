# coding=utf8
from __future__ import unicode_literals
import os
import shutil
from ..baseview import BaseView
from ...crawler.crawler import get_csv, get_yahoo, merge_csv_and_yahoo

class HomeViews(BaseView):

    def __init__(self, request):
        super(HomeViews, self).__init__(request)

    def home(self):
        """
        會員首頁
        :return:
        """
        google_trend = self.request_params.get('google_trend')
        stock_number = self.request_params.get('stock_number')
        # 下載csv
        get_csv(google_trend)

        # 修改檔名
        download_file = self.settings.get('chrome_default_download_folder')+'multiTimeline.csv'
        new_file = self.settings.get('chrome_default_download_folder')+google_trend+'.csv'
        os.rename(download_file, new_file)
        # 移動檔案
        move_file = self.settings.get('csv_folder')+google_trend+'.csv'
        shutil.move(new_file, move_file)

        # 從Yahoo下載 股市 資料
        yahoo_stock_number = '{0}.TW'.format(stock_number)
        yahoo_stock_table = get_yahoo(yahoo_stock_number)

        # 合併google trend 和 股票股價 表格
        merge_data = merge_csv_and_yahoo(move_file, yahoo_stock_table)
        merge_data_png = merge_data.plot(kind='line', subplots=True)
        merge_data_png.savefig('foo.png')

        return {}