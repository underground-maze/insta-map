runserver:
	venv/bin/python manage.py runserver 0.0.0.0:8010

pep8:
	venv/bin/pep8 --exclude=*migrations*,*settings_local.py* --max-line-length=119 --show-source  insta/

pyflakes:
	venv/bin/pylama --skip=*migrations* -l pyflakes insta/

lint:
	make pep8
	make pyflakes

test:
	venv/bin/python manage.py test insta -v 2

recollect:
	python manage.py collectstatic --noinput

ci_test:
	python manage.py test insta -v 2
	pep8 --exclude=*migrations*,*settings_local.py* --max-line-length=119 --show-source  insta/
	pylama --skip=*migrations* -l pyflakes insta/

celery:
	venv/bin/celery --app=insta.celery:app worker --loglevel=INFO
