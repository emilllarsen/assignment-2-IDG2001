[▪](https://www.youtube.com/watch?v=rIrNIzy6U_g) [100+ Docker Concepts you Need to Know (youtube.com) (8m)](https://www.youtube.com/watch?v=rIrNIzy6U_g)




- DNS server, mapping service names to URLs

  - E.g., “db:5001” maps to port 5001 at the service “db”

  - mongodb://db:27017


- Best practice: Isolate containers using networks

- Types

  - bridge (default or user-defined), host, none, and more


docker network create -d bridge my-net


docker network rm my-net




- Used for persistent storage


- Bind mounts are just a “link” to host CWD

- Volumes is its own location


- Volumes are preferred in most cases


- Volumes are like USB flash drives




###### ▪ docker run (command)

docker run --rm -p 5001:8080 --restart always catsymptote/dockerdemo

###### ▪ docker-compose (yaml-file)


name: app
services:
dockerdemo:
ports:
- 5001:8080
restart: always
image: catsymptote/dockerdemo




- You can always use a tool to convert between them. Like composerize

[▪](https://www.composerize.com/) [https://www.composerize.com/](https://www.composerize.com/)




[▪](https://github.com/docker/awesome-compose) [https://github.com/docker/awesome-compose](https://github.com/docker/awesome-compose)

[▪](https://docs.docker.com/compose/samples-for-compose/) [https://docs.docker.com/compose/samples-for-compose/](https://docs.docker.com/compose/samples-for-compose/)




services:
minecraft:
image: itzg/minecraft-server
ports:
- "25565:25565"
environment:
EULA: "TRUE"
deploy:
resources:
limits:
memory: 1.5G
volumes:
- "~/minecraft_data:/data"




- Load balancing


- Caching


- docker scale

   - Allows for launching multiple containers




- Docker scale


- Docker swarm and Kubernetes (k8s)

  - Dynamically controls a bunch of Docker

containers

  - Complex, but does a lot for you, and is portable

  - Exists k8s services, which can do a lot for you

    - KaaS? K8aaS? Idk




- Logging

   - Push-based, event-based, logging daemons

   - Capacity

   - Storing durations




systems


- Makes competition




possible to compete with Adobe on a
application basis?


- If not, is that a problem?




