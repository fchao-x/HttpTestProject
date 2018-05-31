# coding: utf-8
import re

class headers:
	"""docstring for headers"""
	def __init__(self, request):
		self.request = request

	def get_request_headers(self):
		re_server = re.compile(r'^SERVER_[PROTOCOL|PORT]$')
		re_others = re.compile(r'^[PATH|QUERY|REQUEST|HTTP|CONTENT|REMOTE]_.+$')

		request_headers = {}
		for header in self.request.META:
			if re_server.match(header) or re_others.match(header):
				request_headers[header] = self.request.META[header]
		return request_headers

