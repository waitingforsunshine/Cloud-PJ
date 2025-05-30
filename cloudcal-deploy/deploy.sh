#!/bin/bash
cd ~/cloud-computing-qi-mpj/cloudcal-deploy
docker-compose pull webapp
docker-compose up -d
docker system prune -f
