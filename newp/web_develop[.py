#！ /uer/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

#自定义url转换器
class ListConverter(BaseConverter):
    def __init__(self, url_map, separator='+'):
        super(ListConverter, self).__init__(url_map)
        self.separator = urllib.parse.unquote(separator)

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(BaseConverter.to_url(value) for value in values)

app.url_map.converters["list"] = ListConverter


@app.route('/list/<list:page_names>/')
def list1(page_names):
    return 'separator:{} {}'.format("+", page_names)


@app.route('/list2/<list(separator=u"|"):page_names>/')
def list2(page_names):
    return 'separator:{} {}'.format('|', page_names)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)