clean:
	pip uninstall clima_anom -y
	rm -rf build clima_anon.egg-info
install:
	pip install --user --upgrade .
run:
	python /home/adriano/clima-anom/examples/elputin.py