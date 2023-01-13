from httpx import Client as HTTPxClient
from parser import Parser
from request import Request
from colorama import Fore, Style
from datetime import datetime
from match import Match


class Client():
	def __init__(self: object, args: object) -> None:
		http2 = args.http_version == '2'
		proxies = Parser.parse_proxies(args)

		self.client = HTTPxClient(http2=http2, proxies=proxies)
		self.cookies = Parser.parse_cookies(args)

	def replay_requests(self: object, args: object, requests: list) -> None:
		for request_xml in requests:
			request = Request(request_xml)

			self.replay_request(args, request)

	def replay_request(self: object, args: object, request: object) -> None:		
		if request.skip(args):
			return

		print(f'[{Fore.GREEN}{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}{Style.RESET_ALL}][{Fore.GREEN}{request.method}{Style.RESET_ALL}] {request.url}')
		getattr(self, f'do_{request.method}')(args, request)

	def do_GET(self: object, args: object, request: object) -> None:
		response = self.client.get(request.url, cookies=self.cookies)

		if not Match.match(args, response):
			print(f'\tStatus: {Fore.RED}Filtered{Style.RESET_ALL}')
			return

		print(f'\tStatus: {Fore.GREEN}Matched{Style.RESET_ALL}')
		print(f'\tStatus Code: {Fore.CYAN}{response.status_code}{Style.RESET_ALL} <-> {Fore.CYAN}{request.status_code}{Style.RESET_ALL}')
		print(f'\tLength: {Fore.CYAN}{response.num_bytes_downloaded}{Style.RESET_ALL} <-> {Fore.CYAN}{request.length}{Style.RESET_ALL}')
		print(f'\tResponse: {response.content}\n')

	def do_POST(self: object, args: object, request: object) -> None:
		response = self.client.post(request.url, cookies=self.cookies, data=request.data, json=request.json)

		if not Match.match(args, response):
			print(f'\tStatus: {Fore.RED}Filtered{Style.RESET_ALL}')
			return

		print(f'\tStatus: {Fore.GREEN}Matched{Style.RESET_ALL}')
		print(f'\tStatus Code: {Fore.CYAN}{response.status_code}{Style.RESET_ALL} <-> {Fore.CYAN}{request.status_code}{Style.RESET_ALL}')
		print(f'\tLength: {Fore.CYAN}{response.num_bytes_downloaded}{Style.RESET_ALL} <-> {Fore.CYAN}{request.length}{Style.RESET_ALL}')
		print(f'\tResponse: {response.content}\n')