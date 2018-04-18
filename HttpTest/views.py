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

def getMenu(item_list_file_name):
	item_list = []
	f = open(item_list_file_name, r'r')
	for line in f.readlines():
		if len(line.strip()) != 0:
			item_list.append(line.strip())
		else:
			pass
	return item_list

def index(request):

	context = {}
	context['item_list'] = getMenu('HttpTest/static/menu/item_list.txt')
	return render(request, 'base.html', context)

def urlTest(request):
	title = 'URL Test'
	return render(request, 'URL.html', {'title': title} )

@csrf_exempt #禁用CSRF机制
def postTest(request):
	request_headers = getAllHeaders(request)
	return HttpResponse("<pre>%s</pre>" % request_headers)
