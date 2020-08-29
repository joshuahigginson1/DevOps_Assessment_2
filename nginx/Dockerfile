FROM nginx:latest

LABEL version="1.0"
LABEL description="Melodie - NGINX Container."

EXPOSE 80

WORKDIR /

COPY nginx.conf /etc/nginx/nginx.conf

RUN sudo systemctl reload nginx