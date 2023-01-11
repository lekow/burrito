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
		return self.is_not_target(args) or self.invalid_method(args)

	def is_not_target(self: object, args: object) -> bool:
		return args.url and not self.url.startswith(args.url)

	def invalid_method(self: object, args: object) -> bool:
		return self.method not in args.methods