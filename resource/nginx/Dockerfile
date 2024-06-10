FROM nginx:latest

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

COPY wait.sh /wait.sh
RUN chmod +x /wait.sh

EXPOSE 80

# Custom entrypoint 설정
ENTRYPOINT ["/wait.sh"]
