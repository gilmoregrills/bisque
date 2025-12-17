# bisque

> if you turned over various contractions of beets and soulseek in your head enough you'd arrive at the same name

Webserver/API wrapper for beets built on top of the [`linuxserver/beets`]() image. All it does is accept requests from [`slskd`]() on the `/import` path, pick out the download directory name, and pass that to `beet import --quiet`.

Caveats:
- You should ensure the `config.yaml` included in the directory you mount to the `/config` path is complete, because no command-line arguments except `--quiet` will be passed.
  - In particular you might want to set the `quiet_fallback` option to `asis` if you're generally importing music from good sources with reliable tags.
- Your `slskd` download directory and your `bisque` downloads directory should use the same path (they probably both already use `/downloads`).

Example `docker-compose.yaml` file including caddy setup and domain:

```yaml
services:
  beets:
    image: ???
    container_name: bisque
    labels:
      caddy: bisque.nas.eelgirl.biz
      caddy.import: inttls
      caddy.reverse_proxy: "{{upstreams 8074}}"
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /nas/beets/config:/config
      - /nas/data/music:/music
      - /nas/data/downloads:/downloads
    ports:
      - 8074:8074
    networks:
      - caddy
    restart: unless-stopped

networks:
  caddy:
    external: true
```

Example `slskd` webhook config:

```yaml
integration:
  webhooks:
    slskd_to_bisque:
      on:
        - DownloadDirectoryComplete
      call:
        url: https://bisque.nas.eelgirl.biz
```
