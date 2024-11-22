FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY ssl_key.key /etc/nginx/ssl/ssl_key.key
COPY ssl_crt.crt /etc/nginx/ssl/ssl_crt.crt
COPY nginx.conf /etc/nginx/conf.d
