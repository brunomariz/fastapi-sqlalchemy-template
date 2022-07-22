# Local .compose.env
if [ -f .compose.env ]; then
    # Load Environment Variables
    export $(cat .compose.env | grep -v '#' | sed 's/\r$//' | awk '/=/ {print $1}' )
fi

# Stop running containers
docker-compose down
# Remove stopped containers
docker system prune
# Remove image 
docker rmi -f ${COMPOSE_WEB_IMAGE}
# Build new image and start containers
docker-compose --env-file .compose.env up -d

# # Run db container
# docker run -d \
# 	--name lab_engsoft_db \
# 	-p 5543:5432 \
#     -v ${PWD}/scripts:/lab_scripts \
# 	-e POSTGRES_PASSWORD=secret \
# 	-e POSTGRES_DB=lab_engsoft \
# 	-e POSTGRES_USER=aluno \
# 	postgres