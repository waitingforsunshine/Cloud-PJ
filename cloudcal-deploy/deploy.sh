#!/bin/bash
cd ~/CLOUD-PJ/cloudcal-deploy
docker-compose pull webapp
docker-compose up -d
docker system prune -f
