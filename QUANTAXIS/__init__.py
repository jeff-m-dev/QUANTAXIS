#coding :utf-8
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
QUANTAXIS

Quantitative Financial Strategy Framework

by yutiansut    

2017/4/8
"""
# fetch methods

from QUANTAXIS.QAFetch import (QA_fetch_get_stock_day, QA_fetch_get_trade_date,
                               QA_fetch_get_stock_indicator, QA_fetch_get_stock_realtime)
from QUANTAXIS.QAFetch.QAQuery import QA_fetch_trade_date, QA_fetch_stock_day, QA_fetch_stocklist_day, QA_fetch_index_day
from QUANTAXIS.QASpider import (QA_spider_select_spider, QA_spider_start_spider,
                                QA_spider_end_spider)



# save
from QUANTAXIS.QASU.main import (QA_SU_save_stock_list, QA_SU_save_stock_day, QA_SU_save_stock_info,
                                 QA_SU_save_stock_day_init,  QA_SU_save_trade_date, QA_SU_update_stock_day)
from QUANTAXIS.QASU.save_backtest import (
    QA_SU_save_account_message, QA_SU_save_backtest_message,QA_SU_save_account_to_csv)
from QUANTAXIS.QASU.save_tushare import (
    QA_save_stock_day_all, QA_SU_save_trade_date_all)


from QUANTAXIS.QASU.user import (QA_user_sign_in, QA_user_sign_up)
# event driver

# market

from QUANTAXIS.QAMarket import (QA_QAMarket_bid, QA_Market)

# Account,Risk,Portfolio

from QUANTAXIS.QAARP import QA_Account, QA_Portfolio, QA_Risk
# Backtest
from QUANTAXIS.QABacktest.QABacktest import QA_Backtest, QA_Backtest_simple
from QUANTAXIS.QABacktest.QAAnalysis import QA_backtest_analysis_start

# Util
from QUANTAXIS.QAUtil.QAType import (
    QA_util_ensure_date, QA_util_ensure_dict, QA_util_ensure_ms, QA_util_ensure_timeSerires)
from QUANTAXIS.QAUtil import (QA_util_sql_mongo_setting, QA_util_cfg_initial, QA_util_realtime, QA_util_id2date, QA_util_is_trade,
                              QA_util_date_stamp, QA_util_time_stamp, QA_util_ms_stamp,
                              QA_util_log_debug, QA_util_log_expection, QA_util_log_info,
                              QA_start_initial, QA_Setting, QA_util_get_date_index, QA_util_get_index_date, QA_util_get_real_date)

from QUANTAXIS.QAIndicator import *
from QUANTAXIS.QASQL import qasql, qacold
# CMD and Cli
import QUANTAXIS.QACmd

from QUANTAXIS.QACmd import QA_cmd
import argparse
QA_util_log_info('Welcome to QUANTAXIS, the Version is 0.3.9-beta-dev20')



def main():
    QA_cmd()
