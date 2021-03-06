# -*- coding: utf-8 -*-
from datasource.huobi_kline import HuobiKline
from api.huobi_api import HuobiAPI_LTC_BTC


class HuobiBtcKline1day(HuobiKline):
    def config(self):
        self.configure = {
            "name": "huobi_btc_kline_1day",  # Required. Your strategy need this to get data.

            "query_config":{
                "api": HuobiAPI_LTC_BTC().stock(market="CNY").btc_kline_100_json,
            },
        }


EXPORT = HuobiBtcKline1day
