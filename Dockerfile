FROM rasa/rasa:2.8.2
ADD . /app/
USER root
RUN chmod -R 777 /app
USER 1001
RUN rasa train
ENTRYPOINT ["/app/start_services.sh"]