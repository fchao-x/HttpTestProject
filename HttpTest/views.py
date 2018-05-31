# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re


def get_all_headers(request):
    re_http = re.compile(r'^HTTP_.+$')
    re_content_type = re.compile(r'^CONTENT_TYPE$')
    re_content_length = re.compile(r'^CONTENT_LENGTH$')

    request_headers = {}
    for header in request.META:
        if re_http.match(header) or re_content_type.match(header) or re_content_length.match(header):
            request_headers[header] = request.META[header]
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
    request_headers = get_all_headers(request)
    return HttpResponse("<pre>%s</pre>" % request_headers)
