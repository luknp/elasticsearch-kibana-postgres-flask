# elasticsearch-kibana-postgres-flask

A simple Elastic stack (ELK) on Docker with prepared for development Flask api service and the Postgres DB

## Example run

Create .env file based on .env.default and modify its content according to your needs

```sh
mv .env.default .env
```

Launch containers

```sh
docker-compose up -d
```

## Example shutdown

Close the containers

```sh
docker-compose down
```
