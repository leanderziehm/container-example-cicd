# Run


## Podman named
```
podman run -p 8321:8321 --restart=always ghcr.io/leanderziehm/container-example-cicd:latest

```


podman run -p 8321:8321 --name container-example-cicd --restart=always ghcr.io/leanderziehm/container-example-cicd:latest



## Podman simple
```
podman run -p 8321:8321 ghcr.io/leanderziehm/container-example-cicd:latest
```



##  Docker 
```
docker run -p 8321:8321 ghcr.io/leanderziehm/container-example-cicd:latest
```
