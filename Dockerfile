FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
RUN mkdir /etc/nginx/ssl
ADD ./nginx/ssl/ /etc/nginx/ssl
RUN mkdir /static/
ADD ./code/static/ /static/
ADD ./nginx/sites-enabled/ /etc/nginx/sites-enabled/
