FROM lscr.io/linuxserver/beets:2.3.1

COPY ./src/ /app/
RUN pip3 install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
ENTRYPOINT ["python3", "/app/server.py"]
