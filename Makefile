install:
	#install commads
	pip install --upgrade pip &&\
		pip install -r requirements.txt\
		python -m textblob.download_corpora

format:
	#format code # formating tool
	black *.py mylib/*.py
lint:
	#flake8 or #pylint. # lining tool
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main test_*.py
	
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker
	#docker run -p 127.0.0.1:8080:8080 768e64fd91c1
deploy:
	#deploy
all: install lint test deploy