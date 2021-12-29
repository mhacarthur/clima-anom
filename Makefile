install:
	pip install --user --upgrade .
	rm -rf build clima_anom.egg-info	

uninstall:
	pip uninstall clima_anom -y

run:
	python /home/adriano/clima-anom/examples/elputin.py

publish:
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf dist build clima_anon.egg-info
