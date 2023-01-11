from argparse import ArgumentParser
from bs4 import BeautifulSoup as BS
from base64 import b64decode
from pathlib import Path
from json import loads
from contextlib import suppress
from colorama import Fore, Style


class Parser():
	def parse_args() -> object:
		parser = ArgumentParser(description='burrito v0.1', epilog='Created by ld3k0fv')

		parser.add_argument('-u', '--url', dest='url', action='store', type=str, required=False, help='The target URL to use (skips all others)')
		parser.add_argument('-c', '--cookies', dest='cookies', action='extend', nargs='+', required=False, help='The cookies to use')
		parser.add_argument('-f', '--filename', dest='filename', action='store', type=str, required=True, help='The file to use')
		parser.add_argument('-hv', '--http-version', dest='http_version', action='store', type=str, choices=['1.1', '2'], default='1.1', help='The HTTP version to use (default: 1.1)')
		parser.add_argument('-p', '--proxies', dest='proxies', action='extend', nargs='+', required=False, help='The proxy to use')
		parser.add_argument('-m', '--methods', dest='methods', action='extend', nargs='+', required=True, help='The HTTP methods to use')

		return parser.parse_args()

	def parse_proxies(args: object) -> dict:
		proxies = {}

		if args.proxies is None:
			return None

		print(f'[{Fore.CYAN}*{Style.RESET_ALL}] Parsing specified proxies...')

		for i, proxy in enumerate(args.proxies, start=1):
			http_protocol = proxy.split('://')[0]
			proxies[f'{http_protocol}://'] = proxy

			print(f'\t{Fore.CYAN}{i}{Style.RESET_ALL}) {http_protocol} -> {proxy}')

		return proxies

	def parse_cookies(args: object) -> dict:
		cookies = {}

		if args.cookies is None:
			return None

		print(f'[{Fore.CYAN}*{Style.RESET_ALL}] Parsing specified cookies...')

		for i, cookie in enumerate(args.cookies, start=1):
			name, value = cookie.split('=')
			cookies[name] = value

			print(f'\t{Fore.CYAN}{i}{Style.RESET_ALL}) {name} -> {value}')

		return cookies

	def parse_requests(args: object) -> list:
		print(f'[{Fore.CYAN}*{Style.RESET_ALL}] Parsing requests file...')

		if Path(args.filename).is_file():
			print(f'\t{Fore.GREEN}\u2713{Style.RESET_ALL}) File {Fore.CYAN}{args.filename}{Style.RESET_ALL} exists, parsing...')
		else:
			print(f'\t{Fore.RED}\u2717{Style.RESET_ALL}) File {Fore.CYAN}{args.filename}{Style.RESET_ALL} does not exist, exiting...')
			exit(0)

		with open(args.filename, 'r') as fin:
			xml = fin.read()

		soup = BS(xml, 'xml')
		requests = soup.find_all('item')

		print(f'\t{Fore.GREEN}\u2713{Style.RESET_ALL}) Successfully parsed {Fore.CYAN}{len(requests)}{Style.RESET_ALL} requests.\n')

		return requests

	def parse_request_body(request: object) -> tuple:
		body = b64decode(request.find_all('request')[0].text).split(b'\r\n\r\n')[-1].decode()

		with suppress(Exception):
			body = loads(body)

			return None, body

		return body, None