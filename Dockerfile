FROM lscr.io/linuxserver/beets:2.3.1

COPY ./src/ /app/
RUN /lsiopy/bin/pip3 install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
RUN ["/lsiopy/bin/python", "/app/server.py"]
