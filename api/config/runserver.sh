#! /bin/sh
./wait-for-it.sh postgres:5432 -t 60
./wait-for-it.sh elasticsearch:9200 -t 60
./wait-for-it.sh kibana:5601 -t 60
./wait-for-it.sh logstash:9600 -t 60


python load_games.py

gunicorn app:app -c gunicorn_config.py


 