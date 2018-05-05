FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/ssl
ADD ./nginx/ssl/ /etc/nginx/ssl
RUN mkdir /static/
ADD ./code/static/ /static/
COPY ./nginx/sites-enabled /etc/nginx/conf.d
