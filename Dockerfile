# Create base image
FROM  python:3.9-alpine3.13
LABEL maintainer = "developer"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tem/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000 
ARG DEF=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tem/requirements.txt && \
    # if Development only the requirements.dev.text will install
    if [ $DEV = "true"]; \
        then /py/bin/pip install -r /tem/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

# USER django-user log the image in django-user user account
USER django-user
