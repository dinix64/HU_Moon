FROM python:3.7-alpine
RUN pip install flask
RUN pip install requests
COPY app.py /app/app.py
EXPOSE 8080

WORKDIR /app

ENTRYPOINT [ "flask" ]
CMD [ "run","--host=0.0.0.0","--port=8080" ]
