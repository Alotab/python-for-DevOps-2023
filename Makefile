install:
	#install commads
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
			pip install -e .
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 or #pylint
	#pylint --disable=R,C *.py mylib/*.py
test:
	#test
	#python -m pytest -vv --cov=mylib test_logic.py
	python -m pytest --import-mode=test_logic.py
build:
	#build container
deploy:
	#deploy
all: install lint test deploy