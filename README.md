
## Build Docker Image
Build docker image from root folder path
```sh
docker image build . --file docker/Dockerfile.<service> --tag <docker-image-name>:<docker-image-tag> --no-cache 
```

Run docker image with your own arguments
```sh
docker run --env-file envs/<env-file>.env <docker-image-name>:<docker-image-tag> 
```


docker run -v /path/to/csv/folder:/app/input -v /path/to/output/folder:/app/output csv_processor
