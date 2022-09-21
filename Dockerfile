FROM tiangolo/uwsgi-nginx:python3.10
RUN apk --update add bash nano
COPY . /var/www/taxapi
WORKDIR /var/www/taxapi
RUN pip install -r requirements.txt
RUN python3 manage.py db init
RUN python3 manage.py db migrate
RUN python3 manage.py db upgrade
CMD ["python3", "manage.py", "run"]
