FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY ssl_cert.crt /etc/nginx/ssl/
COPY ssl_cert.key /etc/nginx/ssl/
COPY nginx.conf /etc/nginx/conf.d
