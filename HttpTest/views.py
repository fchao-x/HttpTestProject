# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re

class headers:
    """docstring for headers"""
    def __init__(self, request):
        self.request = request

    def get_request_headers(self):
        re_server = re.compile(r'^SERVER_((PROTOCOL)|(PORT))$')
        re_others = re.compile(r'^((PATH)|(QUERY)|(REQUEST)|(HTTP)|(CONTENT)|(REMOTE))_.+$')

        request_headers = {}
        for header in self.request.META:
            if re_server.match(header) or re_others.match(header):
                request_headers[header] = self.request.META[header]
        return request_headers


def get_menu(item_list_file_name):
    item_list = []
    f = open(item_list_file_name, 'r')
    for line in f.readlines():
        if len(line.strip()) != 0:
            item_list.append(line.strip())
        else:
            pass
    return item_list


def index(request):
    context = {'item_list': get_menu('HttpTest/static/menu/item_list.txt')}
    return render(request, 'base.html', context)


def url_test(request):
    context = {'item_list': get_menu('HttpTest/static/menu/item_list.txt'), 'title': 'URL Test'}
    return render(request, 'URL.html', context)


@csrf_exempt  # 禁用CSRF机制
def post_test(request):
    request_headers = headers(request)
    return HttpResponse("<pre>%s</pre>" % request_headers.get_request_headers())
