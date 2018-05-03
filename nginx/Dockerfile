FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
RUN mkdir /etc/nginx/ssl
ADD ./ssl/ /etc/nginx/ssl
RUN mkdir /static/
ADD ./static/ /static/
ADD ./sites-enabled/ /etc/nginx/sites-enabled/
