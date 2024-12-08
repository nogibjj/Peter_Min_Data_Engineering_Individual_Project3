format:
	black *.py

lint:
	ruff check *.py

install:
	pip3 install --upgrade pip && pip3 install -r requirements.txt

refactor: format lint 