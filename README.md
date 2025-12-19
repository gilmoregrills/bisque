# bisque

> if you turned over various contractions of beets and soulseek in your head enough you'd arrive at the same name

Hacky API wrapper for `beets` built on top of the [`linuxserver/beets`]() image. All it does is accept requests from [`slskd`]() on the `/import` path, pick out the download directory name, and pass that to `beet import --quiet`.

## Caveats:
- You should ensure the `config.yaml` included in the directory you mount to the `/config` path is complete, because no command-line arguments except `--quiet` will be passed.
  - In particular you might want to set the `quiet_fallback` option to `asis` if you're generally importing music from good sources with reliable tags.
- Your beets config needs to be in `/config/config.yaml`, which it probably already is.
- Your `slskd` download directory and your `bisque` downloads directory should use the same path (they probably both already use `/downloads`).

## Examples

### Example `docker-compose.yaml` file:

> note: if you're already using the beets container image then bisque should work as a drop-in replacement

The `/config` directory should contain your `beets` `config.yaml`, which should ideally point to your library database in the same `/config` directory.

```yaml
services:
  beets:
    image: ghcr.io/gilmoregrills/bisque:<VERSION>
    container_name: bisque
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - /path/to/config:/config
      - /path/to/music:/music
      - /path/to/downloads:/downloads
    ports:
      - 8074:8074
    restart: unless-stopped
```

### Example `beets` config:

```yaml
directory: /music # gotta use the path inside the docker container that we mount above
library: /config/library.db # likewise here, it should be /config not /path/to/config
import:
  move: yes
permissions:
  file: 777
  dir: 777
quiet_fallback: asis
plugins: web fetchart lyrics
fetchart:
  auto: yes
  lastfm_key: <REDACTED>
  sources:
    - filesystem
    - coverart
    - itunes
    - amazon
    - albumart
    - lastfm
lyrics:
  auto: no
  synced: yes
  sources:
    - lrclib
```

### Example `slskd` webhook config:

```yaml
integration:
  webhooks:
    slskd_to_bisque:
      on:
        - DownloadDirectoryComplete
      call:
        url: https://bisque.nas.eelgirl.biz
```

## notes/docs (for my reference):
- https://github.com/slskd/slskd/blob/master/src/slskd/Events/Types/Events.cs
- https://github.com/slskd/slskd/blob/master/docs/config.md
- https://hub.docker.com/r/linuxserver/beets/
