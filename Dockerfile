FROM lscr.io/linuxserver/beets:2.3.1

COPY ./src/ /app/
RUN apk add --no-cache gcc python3-dev \
&& /lsiopy/bin/pip3 install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
CMD ["/lsiopy/bin/python", "/app/server.py"]
