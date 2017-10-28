

coverage:
	coverage run --source yycli -m pytest test
	cuv graph
