FROM alpine:latest

RUN apk --no-cache add curl

COPY todo-cron.sh /todo-cron.sh

RUN chmod +x /todo-cron.sh

ENTRYPOINT ["/todo-cron.sh"]
