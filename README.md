# docker-ab-testing

### Setup of the docker environment

```bash
docker network create docker-ab-testing
docker network create -d overlay --attachable docker-ab-testing
docker pull nginx:latest
docker pull python:latest
```

### Logfile tailing

```bash
docker logs nginx -f | tee /tmp/$(date +%s)_nginx.out
```

### Reload configuration file from within the nginx

```bash
docker kill -s HUP nginx
```

### Remove a container

```bash
docker container rm app-v1 -f
docker container rm app-v2 -f
docker container rm nginx -f
```