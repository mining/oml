.PHONY: environment
environment:
	@python setup.py install
	@git clone https://github.com/avelino/mining.git
	@pip install -r mining/requirements.txt
	@pip install numexpr==2.3
	@python mining/setup.py develop
	@mv mining/mining/mining.sample.ini mining/mining/mining.ini
