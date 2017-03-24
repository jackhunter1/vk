#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
PY_V = sys.version_info.major
if PY_V == 3:
    import http.client as HTTP
else:
    import httplib as HTTP


def user_get(id_, fields):
    conn = HTTP.HTTPSConnection("api.vk.com")
    conn.request("GET", '/method/users.get?user_id=' + id_ + '&fields=' + fields + '&v=5.62')
    resp = conn.getresponse()
    data_ = json.loads(resp.read())['response'][0]
    for i in data_:
        print(i)

    return data_


def audio_get(id_, fields):
    conn = HTTP.HTTPConnection('api.vk.com')
    conn.request('GET', '/method/audio.get?owner_id=' + id_ + '&v=5.62')
    resp = conn.getresponse()
    data_ = resp.read()
    return data_
#print(user_get('63028253', 'bdate,home_town,career,counters,crop_photo,domain'))


print(audio_get('63028253', ''))
