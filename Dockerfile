FROM lscr.io/linuxserver/beets:2.3.1

COPY ./src/ /app/
RUN apk add --no-cache gcc python3-dev python3-dev linux-headers py3-psutil
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app
CMD ["/lsiopy/bin/python", "/app/server.py"]
