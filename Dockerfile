FROM python:3

RUN git clone https://github.com/rafal-draws/conclusions-blog.git /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ENV DJANGO_SECRET='$(python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")'

RUN python3 /app/conclusions/manage.py collectstatic 

RUN python3 /app/conclusions/manage.py makemigrations

RUN python3 /app/conclusions/manage.py migrate

RUN apt-get update && apt-get install -y nginx

RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-enabled/

COPY start.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh

EXPOSE 80
EXPOSE 443

CMD ["/usr/local/bin/start.sh"]