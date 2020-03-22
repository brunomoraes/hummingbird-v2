FROM python:3.7-stretch as base

FROM base as build

COPY src/requirements.txt ./requirements.txt
COPY requirements_local.txt ./requirements_local.txt
RUN pip install --no-cache-dir -r ./requirements.txt -r ./requirements_local.txt

FROM base as release

ARG RUN_ENVIRONMENT
ENV FLASK_ENV=${RUN_ENVIRONMENT}
ENV ENV=${RUN_ENVIRONMENT}

EXPOSE 5000

WORKDIR /app

RUN useradd app
USER app

COPY . /app/

COPY --from=build /usr/local/lib/ /usr/local/lib/
COPY --from=build /usr/local/bin /usr/local/bin




CMD python app/src/main.py

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]