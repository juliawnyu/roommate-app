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

all_tests: lint unit

unit: FORCE
	pytest $(PYTESTFLAGS)

lint: FORCE
	$(LINTER) $(*.py)

%.py: FORCE
	pytest -s tests/test_$*.py

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt

docs: FORCE
	cd $(API_DIR); make docs
