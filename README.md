# airflow-101

Repositório para estudo do airflow

* Docker criado baseado no [tutorial](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#docker-compose-yaml)
* Exemplo de API da [pokeapi](https://pokeapi.co/)

## Para executar

* clone o repo
* execute as configurações

```bash
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up airflow-init
```

* execute os serviços

```bash
docker-compose up
```