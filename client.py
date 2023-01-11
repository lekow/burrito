from httpx import Client as HTTPxClient
from parser import Parser
from request import Request
from colorama import Fore, Style
from datetime import datetime


class Client():
	def __init__(self: object, args: object) -> None:
		http2 = args.http_version == '2'
		proxies = Parser.parse_proxies(args)

		self.client = HTTPxClient(http2=http2, proxies=proxies)
		self.cookies = Parser.parse_cookies(args)

	def replay_requests(self: object, args: object, requests: list) -> None:
		for request_xml in requests:
			request = Request(request_xml)

			if request.skip(args):
				continue

			self.replay_request(args, request)

	def replay_request(self: object, args: object, request: object) -> None:
		print(f'[{Fore.GREEN}{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}{Style.RESET_ALL}][{Fore.GREEN}{request.method}{Style.RESET_ALL}] {request.url}')
		getattr(self, f'do_{request.method}')(request)

	def do_GET(self: object, request: object) -> None:
		response = self.client.get(request.url, cookies=self.cookies)

		print(f'\tStatus Code: {Fore.CYAN}{response.status_code}{Style.RESET_ALL} <-> {Fore.CYAN}{request.status_code}{Style.RESET_ALL}')
		print(f'\tLength: {Fore.CYAN}{len(response.content)}{Style.RESET_ALL} <-> {Fore.CYAN}{request.length}{Style.RESET_ALL}')
		print(f'\tResponse: {response.content}\n')

	def do_POST(self: object, request: object) -> None:
		response = self.client.post(request.url, cookies=self.cookies, data=request.data, json=request.json)

		print(f'\tStatus Code: {Fore.CYAN}{response.status_code}{Style.RESET_ALL} <-> {Fore.CYAN}{request.status_code}{Style.RESET_ALL}')
		print(f'\tLength: {Fore.CYAN}{len(response.content)}{Style.RESET_ALL} <-> {Fore.CYAN}{request.length}{Style.RESET_ALL}')
		print(f'\tResponse: {response.content}\n')