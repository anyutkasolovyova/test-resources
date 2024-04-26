# test-resources

## Start postgres
```shell
docker run --name my-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgress -d postgres:16.2
docker start my-postgres
```

## Kill ports
```shell
sudo lsof -i :5432
sudo kill -9 561
```

## Connect to postgres using Docker
```shell
docker exec -it my-postgres bash
psql -U postgres
```
