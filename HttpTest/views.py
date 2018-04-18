# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re

def getAllHeaders(request):
	re_http = re.compile(r'^HTTP_.+$')
	re_content_type = re.compile(r'^CONTENT_TYPE$')
	re_content_length = re.compile(r'^CONTENT_LENGTH$')

	request_headers = {}
	for header in request.META:
		if re_http.match(header) or re_content_type.match(header) or re_content_length.match(header):
			request_headers[header] = request.META[header]
	return request_headers

def index(request):
	item_list = []

	f = open('HttpTest/static/menu/item_list.txt', r'r')
	for line in f.readlines:
		if len(line.strip(' ')) != 0:
			item = '<a class="memu_list" href="' + itme + '.html" >' + item + '</a>'
			item_list.append(item)
		else:
			pass
	rander(request, 'menu.html', {'item_list': item_list})
	return render(request, 'base.html')

def menu(request):
	item_list = []

	f = open('HttpTest/static/menu/item_list.txt', r'r')
	for line in f.readlines:
		if len(line.strip(' ')) != 0:
			item = '<a class="memu_list" href="' + itme + '.html" >' + item + '</a>'
			item_list.append(item)
		else:
			pass

	return render(request, 'menu.html', {'item_list': item_list})

@csrf_exempt #禁用CSRF机制
def postTest(request):
	request_headers = getAllHeaders(request)
	return HttpResponse("<pre>%s</pre>" % request_headers)
