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
	return render(request, 'index.html')

@csrf_exempt #禁用CSRF机制
def postTest(request):
	request_headers = getAllHeaders(request)
	return HttpResponse("<pre>%s</pre>" % request_headers)
