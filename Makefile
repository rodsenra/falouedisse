CWD="`pwd`"
HOME_PROJECT ?= $(CWD)
CODE=$(HOME_PROJECT)/src
NEW_PYTHONPATH=$(CODE):$(PYTHONPATH)

clean:
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -delete

install:
	@echo "Installing dependencies..."
	@pip install -r $(HOME_PROJECT)/requirements.txt

tests: clean pep8
	@echo "Running pep8 and tests..."
	@nosetests -s -v --tests=$(HOME_PROJECT)/tests   --with-xunit

pep8:
	@echo "Checking source-code PEP8 compliance"
	@-pep8 $(HOME_PROJECT)/src --ignore=E501,E126,E127,E128
	@-pep8 $(HOME_PROJECT)/tests --ignore=E501,E126,E127,E128
