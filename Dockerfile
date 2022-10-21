# start from an official image
# FROM python:3.7-alpine
FROM nickgryg/alpine-pandas
# FROM python:3.7.6-buster
# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

############# Build pack
# Pillow
RUN apk update \
    && apk add --virtual build-deps gcc musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

# Pandas Numpy Scipy
#RUN apk update && apk add gcc libc-dev \
#    && apk add gfortran openblas-dev lapack-dev --repository \ #http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \
#    && echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/ \ #testing" >> /etc/apk/repositories \
#    && apk add --update --no-cache --force-broken-world \ 
#    py3-numpy py3-pandas@testing \
#    && pip --default-timeout=1200 install six==1.16.0 \
#    && pip --default-timeout=1200 install pandas \
#    && pip --default-timeout=1200 install nltk==3.6.7 \
#    && pip --default-timeout=1200 install numpy==1.21.6 \
#    && pip --default-timeout=1200 install scipy

########### install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/
RUN export PIPENV_INSTALL_TIMEOUT=1200
COPY /app/requirements.txt .
RUN pip --default-timeout=1200 install -r requirements.txt
# RUN pip --default-timeout=1200 install sqlparse
# RUN pip --default-timeout=1200 install typing_extensions
RUN pip --default-timeout=1200 install pipenv && pipenv install --system

# copy our project code
COPY . /opt/services/djangoapp/src
RUN cd app && python manage.py collectstatic --no-input -v 2

# expose the port 8000
EXPOSE 80

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "app", "--bind", ":80", "projet_rafgo.wsgi:application"]