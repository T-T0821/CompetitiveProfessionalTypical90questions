sudo service docker start
docker compose -f "docker-compose.yml" up -d --build
docker exec -it python3 bash