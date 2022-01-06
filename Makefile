install:
	pip install --user --upgrade .
	rm -rf build clima_anom.egg-info	

uninstall:
	pip uninstall clima_anom -y

publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf dist build clima_anom.egg-info
