.PHONY: help clean dist upload

help:
	@echo "Allowed targets:"
	@echo "- help:       this text"
	@echo "- clean:      clean up"
	@echo "- dist:      create Python distribution"
	@echo "- upload:    upload to PyPI"

clean:
	rm -rf build dist django_auth_http_basic.egg-info .coverage .coverage_html .tox

dist:
	python setup.py sdist

upload:
	twine upload -p `pass www/python.org|head -n 1` dist/*
