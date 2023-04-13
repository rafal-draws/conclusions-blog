FROM python:3

WORKDIR /app

RUN git clone https://github.com/rafal-draws/conclusions-blog.git .

RUN pip install -r requirements.txt

RUN DJANGO_SECRET = $(python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")\
    && echo "DJANGO_SECRET=${DJANGO_SECRET}" >> /etc/environment 

RUN python3 conclusions/conclusions/manage.py collectstatic

RUN python3 conclusions/conclusions/manage.py makemigrations

RUN python3 conclusions/conclusions/manage.py migrate

RUN apt-get update && apt-get install -y nginx
RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-enabled/

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]