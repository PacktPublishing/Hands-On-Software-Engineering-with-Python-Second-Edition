# Image/container names
IMAGE_NAME = fastapi-example
CONTAINER_NAME = $(IMAGE_NAME)-container

# Build: copy sources + generate requirements + docker build
build:
	@echo "Running docker build"
	docker build -f Dockerfile -t $(IMAGE_NAME) app

# Run container
run:
	docker run --rm \
		--name $(CONTAINER_NAME) \
		--network host \
		-e MYSQL_HOST=127.0.0.1 \
		-e MYSQL_PORT=3306 \
		-e MYSQL_USER=hms-service-user \
		-e MYSQL_PASS=hms-service-password \
		-e MYSQL_DB=HMS_DEV \
		$(IMAGE_NAME)

rebuild: build run
