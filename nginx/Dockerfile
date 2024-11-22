FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY ssl_cert.crt /etc/nginx/ssl/ssl_cert.crt
COPY ssl_cert.key /etc/nginx/ssl/ssl_cert.key
file /etc/nginx/ssl/ssl_cert.key
COPY nginx.conf /etc/nginx/conf.d
