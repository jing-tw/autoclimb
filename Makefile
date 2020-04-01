clean:
	rm -fr .tox
	python3 -Bc "for p in __import__('pathlib').Path('.').rglob('*.py[co]'): p.unlink()"
	python3 -Bc "for p in __import__('pathlib').Path('.').rglob('__pycache__'): p.rmdir()"
	#py3clean -v .
