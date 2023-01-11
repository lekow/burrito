def print_and_log(message: str, log: object=None) -> None:
	print(message)

	if log:
		log.writelines(f'{message}\n')