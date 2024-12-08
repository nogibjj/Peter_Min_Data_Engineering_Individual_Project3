format:
	black *.py

lint:
	ruff check *.py

refactor: format lint 