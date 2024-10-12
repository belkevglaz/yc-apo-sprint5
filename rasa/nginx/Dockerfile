FROM nginx:alpine

ADD nginx.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /var/cache/nginx && \
    chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /etc/nginx && \
    chown -R nginx:nginx /var/log/nginx && \
    chown -R nginx:nginx /usr/share/nginx

RUN sed -i 's|/var/run/nginx.pid;|/tmp/nginx.pid;|g' /etc/nginx/nginx.conf

USER nginx

ENTRYPOINT ["nginx", "-g", "daemon off;"]

EXPOSE 8080