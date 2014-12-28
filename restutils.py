# --------------------------------------- #
# Global utility functions for REST calls #
# --------------------------------------- #

__author__ = 'mturatti'

import requests


def put_resource(url, params, headers):
    print("++ put_resource: " + url)
    r = requests.put(url, params=params, headers=headers)
    print(r.status_code)
    return r


def post_resource(url, json):
    print("+++ post_resource: " + url)
    r = requests.post(url, json=json)
    print(r.status_code)
    return r


def get_resource(url, params):
    print("+++ get_resource: " + url)
    r = requests.get(url, params=params)
    print(r.status_code)
    return r


def count_documents(request):
    print("+++ count_documents")
    count = int(request.json()['_returned'])
    print(count)
    return count


def delete_resource(url):
    print("++ delete_resource: " + url)
    r1 = requests.get(url)
    assert r1.status_code == 200
    etag = r1.json()['_etag']
    headers = {'If-Match': etag}
    print("headers: " + str(headers))
    r2 = requests.delete(url, headers=headers)
    print(r2.status_code)
    return r2
