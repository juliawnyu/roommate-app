LINTER = flake8
API_DIR = server
DB_DIR = db
REQ_DIR = .
PYTESTFLAGS = -vv --verbose --tb=short --cov=$(PKG) --cov-branch --cov-report term-missing

FORCE:

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin master

tests: lint unit

unit: FORCE
	pytest $(PYTESTFLAGS)

lint: FORCE
	$(LINTER) $(*.py)

%.py: FORCE
	pytest -s tests/test_$*.py

docs: FORCE
	make docs
