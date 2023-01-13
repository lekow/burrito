class Match():
	def match(args: object, response: object) -> bool:
		return Match.match_status_code(args, response)

	def match_status_code(args: object, response: object) -> bool:
		filter_status_code = Match.filter_status_code(args, response)

		if not args.match_code and not filter_status_code:
			return True

		return args.match_code and str(response.status_code) in args.match_code

	def filter_status_code(args: object, response: object) -> bool:
		return args.filter_code and str(response.status_code) in args.filter_code