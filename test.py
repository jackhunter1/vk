#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
PY_V = sys.version_info.major
if PY_V == 3:
    import http.client as HTTP
else:
    import httplib as HTTP


def user_request(id_, method_, fields):
    conn = HTTP.HTTPSConnection("api.vk.com")
    conn.request("GET", "/method/" + method_ + '?user_id=' + id_ + '&fields=' + fields + '&v=5.62')
    resp = conn.getresponse()
    data_ = json.loads(resp.read())['response'][0]
    for i in data_:
        print(i)
    print(data_['home_town'])
    return data_


print(user_request('63028253', 'users.get', 'bdate,home_town'))
