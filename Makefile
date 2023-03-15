test-coverage:
	poetry run coverage run -m pytest .
	poetry run coverage report -m

lint-black:
	black --check .

fix-black:
	black .

build-docs:
	cd docs; \
	poetry run make clean; \
	poetry run sphinx-build -b html source/ build/html;

publish:
	rm dist -r; \
	poetry build; \
	twine upload dist/*