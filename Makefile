PACKAGES="import_monster"

all: install-all black clean

black:
	@black ${PACKAGES}

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -f `find . -type f -name '@*' `
	@rm -f `find . -type f -name '#*#' `
	@rm -f `find . -type f -name '*.orig' `
	@rm -f `find . -type f -name '*.rej' `
	@rm -rf `find . -type d -name '.pytest_cache' `

	@rm -rf .tox
	@rm -f .develop
	@rm -f .flake

install-dev:
	@pip install -r requirements-dev.txt

install-package:
	@pip install -r requirements.txt

install-all: install-dev install-package
