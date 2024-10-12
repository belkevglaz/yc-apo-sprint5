#!/bin/bash

docker cp nlu.yml rasa:/rasa/data/
docker cp stories.yml rasa:/rasa/data/
docker cp rules.yml rasa:/rasa/data/

docker exec -it rasa sh -c "cd /rasa && rasa train"
docker restart rasa
docker logs -f rasa