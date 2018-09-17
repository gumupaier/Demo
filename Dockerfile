FROM python:3.5

COPY . /work

WORKDIR /work
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple/

ENTRYPOINT ["/work/script/init_db.sh"]


CMD ["python", "/work/dev/db_tools/manage.py", "makemigrations"]

#CMD gunicorn -k gevent -b "0.0.0.0:8866" -w 3 sgcc_server.wsgi