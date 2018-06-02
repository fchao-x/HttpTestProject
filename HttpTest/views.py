# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re

class headers:
    """Functions:
        get_request_info()   返回请求"""

    def __init__(self, request):
        self.request = request

<<<<<<< HEAD
    def get_request_info(self):
        re_server = re.compile(r'^SERVER_((PROTOCOL)|(PORT))')
=======
    def get_request_headers(self):
        re_server = re.compile(r'^SERVER_((PROTOCOL)|(PORT))$')
>>>>>>> 698ebe9d7b21285a6953a970808b7a0bdb3623bf
        re_others = re.compile(r'^((PATH)|(QUERY)|(REQUEST)|(HTTP)|(CONTENT)|(REMOTE))_.+$')

        request_headers = {}
        for header in self.request.META:
            if re_server.match(header) or re_others.match(header):
                request_headers[header] = self.request.META[header]
        return request_headers
        #return self.request.META


def get_menu(item_list_file_name):

    f = open(item_list_file_name, 'r')

    item_list = {}
    for line in f.readlines():
        if len(line.strip()) != 0:
            items = line.split(',')
            item_list[items[0].strip()] = []
            for item in items:
                if item != items[0]:
                    item_list[items[0].strip()].append(item.strip())
    return item_list


def index(request):
    request_headers = headers(request)
    context = { 'menu': get_menu('HttpTest/static/menu/item_list.txt'),
                'request': request_headers.get_request_info() }
    return render(request, 'base.html', context)


def url_test(request):
    context = {'item_list': get_menu('HttpTest/static/menu/item_list.txt'), 'title': 'URL Test'}
    return render(request, 'URL.html', context)


@csrf_exempt  # 禁用CSRF机制
def post_test(request):
    request_headers = headers(request)
    return HttpResponse("<pre>%s</pre>" % request_headers.get_request_info())

    #return HttpResponse("<pre>%s</pre>" % get_menu('HttpTest/static/menu/item_list.txt'))
