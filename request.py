from parser import Parser


class Request():
	def __init__(self: object, request: object) -> None:
		self.url = request.find('url').text
		self.method = request.find('method').text
		self.status_code = request.find('status').text
		self.response_headers = Parser.parse_response_headers(request)
		self.length = self.response_headers.get('Content-Length')
		self.data, self.json = Parser.parse_request_body(request)

	def skip(self: object, args: object) -> bool:
		return self.is_not_match_url(args) or self.filter_url(args) or self.invalid_method(args)

	def is_not_match_url(self: object, args: object) -> bool:
		return args.match_url is not None and args.match_url and not self.url.startswith(args.match_url)

	def filter_url(self: object, args: object) -> bool:
		return args.filter_url is not None and self.url.startswith(args.filter_url)

	def invalid_method(self: object, args: object) -> bool:
		return self.method not in args.methods