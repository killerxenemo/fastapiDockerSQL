#deployment example fastapi for docker

docker build -t fastapi-db .
docker run -d -p 8000:8000 fastapi-db
docker compose up --build
