class Match():
	def match(args: object, response: object) -> bool:
		return Match.match_status_code(args, response) and Match.match_length(args, response)

	def match_status_code(args: object, response: object) -> bool:
		filter_status_code = Match.filter_status_code(args, response)

		if not args.match_code and not filter_status_code:
			return True

		return args.match_code and str(response.status_code) in args.match_code

	def match_length(args: object, response: object) -> bool:
		filter_length = Match.filter_length(args, response)

		if not args.match_length and not filter_length:
			return True

		return args.match_length and str(response.num_bytes_downloaded) in args.match_length

	def filter_status_code(args: object, response: object) -> bool:
		return args.filter_code and str(response.status_code) in args.filter_code

	def filter_length(args: object, response: object) -> bool:
		return args.filter_length and str(response.num_bytes_downloaded) in args.filter_length