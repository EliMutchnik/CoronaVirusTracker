FROM python:3.7-slim

ARG app_dir=/app

ADD app ${app_dir}
RUN pip3 install -r ${app_dir}/requirements.txt

ENTRYPOINT python3.7 /app/app.py